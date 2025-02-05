"""
Copyright 2025 by Sergei Belousov

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import logging
from typing import Optional, Union, List, Iterable
from collections.abc import Sequence
from urllib.parse import urlparse, parse_qs

from .globals_ import HTTP_CLIENT, logger
from .json_extractor import extract_ytcfg, extract_initial_data
from .deferred_generator_list import DeferredGeneratorList

class Playlist(Sequence):
    """
    A YouTube playlist object. Parses the page's HTML and extracts video links.
    """

    def __init__(self, url: str, client: str = "WEB") -> None:
        self._input_url = url
        self.client = client

        self._html: Optional[str] = None
        self._ytcfg: Optional[dict] = None
        self._initial_data: Optional[dict] = None

        self._playlist_id: Optional[str] = None
        self._video_urls: Optional[DeferredGeneratorList] = None

    def __repr__(self) -> str:
        return f"<Playlist: {self.playlist_id}>"

    def __len__(self) -> int:
        return len(self.video_urls)

    def __getitem__(self, i: Union[int, slice]) -> Union[str, List[str]]:
        return self.video_urls[i]

    @property
    def playlist_id(self) -> str:
        if self._playlist_id is not None:
            return self._playlist_id
        parsed = urlparse(self._input_url)
        qs = parse_qs(parsed.query)
        self._playlist_id = qs.get("list", [""])[0]
        return self._playlist_id

    @property
    def playlist_url(self) -> str:
        return f"https://www.youtube.com/playlist?list={self.playlist_id}"

    @property
    def html(self) -> str:
        if self._html is None:
            self._html = HTTP_CLIENT.get(self.playlist_url)
        return self._html

    @property
    def ytcfg(self) -> dict:
        if self._ytcfg is None:
            self._ytcfg = extract_ytcfg(self.html)
        return self._ytcfg

    @property
    def initial_data(self) -> dict:
        if self._initial_data is None:
            self._initial_data = extract_initial_data(self.html)
        return self._initial_data

    @property
    def video_urls(self) -> DeferredGeneratorList:
        if self._video_urls is None:
            self._video_urls = DeferredGeneratorList(self._video_urls_generator())
        return self._video_urls

    def _video_urls_generator(self) -> Iterable[str]:
        """
        Parse the real playlist structure from 'initial_data',
        checking for 'richGridRenderer' or fallback 'sectionListRenderer'.
        Yields full watch URLs.
        """
        data = self.initial_data
        logger.debug("Parsing playlist to yield video links...")

        try:
            # The root tabs structure
            tabs = data["contents"]["twoColumnBrowseResultsRenderer"]["tabs"]
            # Typically the first tab
            tab_0 = tabs[0]["tabRenderer"]["content"]

            if "richGridRenderer" in tab_0:
                items = tab_0["richGridRenderer"]["contents"]
                for it in items:
                    # might be 'richItemRenderer' or 'continuationItemRenderer'
                    if "richItemRenderer" in it:
                        content_obj = it["richItemRenderer"]["content"]
                        if "playlistVideoRenderer" in content_obj:
                            vid = content_obj["playlistVideoRenderer"]["videoId"]
                            yield f"https://www.youtube.com/watch?v={vid}"
                    elif "continuationItemRenderer" in it:
                        # If needed, we can do continuation here
                        pass

            elif "sectionListRenderer" in tab_0:
                # older structure
                sec_list = tab_0["sectionListRenderer"]["contents"]
                for section_obj in sec_list:
                    if "itemSectionRenderer" not in section_obj:
                        continue
                    contents_arr = section_obj["itemSectionRenderer"].get("contents", [])
                    for block in contents_arr:
                        if "playlistVideoListRenderer" in block:
                            videos_array = block["playlistVideoListRenderer"].get("contents", [])
                            for v in videos_array:
                                if "playlistVideoRenderer" in v:
                                    vid = v["playlistVideoRenderer"]["videoId"]
                                    yield f"https://www.youtube.com/watch?v={vid}"
                        elif "richGridRenderer" in block:
                            items2 = block["richGridRenderer"].get("contents", [])
                            for it2 in items2:
                                if "richItemRenderer" in it2:
                                    cont2 = it2["richItemRenderer"]["content"]
                                    if "playlistVideoRenderer" in cont2:
                                        vid2 = cont2["playlistVideoRenderer"]["videoId"]
                                        yield f"https://www.youtube.com/watch?v={vid2}"
                        # possibly more logic if we see 'continuationItemRenderer'

            else:
                logger.warning("No recognized playlist structure found.")

        except KeyError as e:
            logger.error(f"Error parsing playlist JSON structure: {e}")
            return
        # If needed, continuation logic with InnerTube can be implemented here.
