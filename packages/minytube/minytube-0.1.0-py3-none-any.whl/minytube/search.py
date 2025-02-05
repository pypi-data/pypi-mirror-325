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
from typing import Optional, Any, List, Dict, Tuple

from .filter_ import Filter
from .innertube import InnerTube
from .youtube import YouTube
from .playlist import Playlist
from .channel import Channel
from .globals_ import logger

class Search:
    """
    Perform a YouTube search using the internal API (InnerTube).
    Returns videos, playlists, channels, etc.
    """

    def __init__(self, query: str, client: str = "WEB", filters: Optional[dict] = None) -> None:
        self.query = query
        self.client = client
        self._innertube_client = InnerTube(client=self.client)

        self._initial_results: Optional[dict] = None
        self._results: Dict[str, List[Any]] = {}
        self._current_continuation: Optional[str] = None

        self.filter_params: Optional[bytes] = None
        if filters:
            flt = Filter()
            flt.set_filters(filters)
            self.filter_params = flt.get_filters_params()

    def _fetch_and_parse(self, continuation: Optional[str] = None) -> Tuple[Dict[str, List[Any]], Optional[str]]:
        data = None
        if self.filter_params and not continuation:
            # передаём params только в первом запросе
            data = {"params": self.filter_params}

        raw_json = self._innertube_client.search(self.query, continuation=continuation, data=data)

        try:
            sections = raw_json["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"][
                "contents"
            ]
        except KeyError:
            # maybe it's a continuation
            sections = raw_json["onResponseReceivedCommands"][0]["appendContinuationItemsAction"]["continuationItems"]

        item_renderer = None
        continuation_renderer = None
        for s in sections:
            if "itemSectionRenderer" in s:
                item_renderer = s["itemSectionRenderer"]
            if "continuationItemRenderer" in s:
                continuation_renderer = s["continuationItemRenderer"]

        next_cont = None
        if continuation_renderer:
            next_cont = continuation_renderer["continuationEndpoint"]["continuationCommand"]["token"]

        results: Dict[str, List[Any]] = {}
        if item_renderer:
            videos: List[YouTube] = []
            shorts: List[YouTube] = []
            playlists: List[Playlist] = []
            channels: List[Channel] = []
            raw_list = item_renderer.get("contents", [])

            for block in raw_list:
                # skip certain blocks
                if any(k in block for k in ["shelfRenderer", "radioRenderer", "horizontalCardListRenderer",
                                            "didYouMeanRenderer", "backgroundPromoRenderer"]):
                    continue
                if block.get("searchPyvRenderer", {}).get("ads"):
                    continue

                if "playlistRenderer" in block:
                    pid = block["playlistRenderer"]["playlistId"]
                    playlists.append(Playlist(f"https://www.youtube.com/playlist?list={pid}", client=self.client))

                if "channelRenderer" in block:
                    cid = block["channelRenderer"]["channelId"]
                    channels.append(Channel(f"https://www.youtube.com/channel/{cid}", client=self.client))

                if "reelShelfRenderer" in block:
                    for x in block["reelShelfRenderer"]["items"]:
                        if "reelItemRenderer" in x:
                            vid = x["reelItemRenderer"]["videoId"]
                        else:
                            vid = x["shortsLockupViewModel"]["onTap"]["innertubeCommand"]["reelWatchEndpoint"]["videoId"]
                        shorts.append(YouTube(f"https://www.youtube.com/watch?v={vid}"))

                if "videoRenderer" in block:
                    vid = block["videoRenderer"]["videoId"]
                    videos.append(YouTube(f"https://www.youtube.com/watch?v={vid}"))

            results["videos"] = videos
            results["shorts"] = shorts
            results["playlist"] = playlists
            results["channel"] = channels

        return results, next_cont

    def _get_results(self) -> None:
        res, cont = self._fetch_and_parse()
        self._current_continuation = cont
        self._results["videos"] = res.get("videos", [])
        self._results["shorts"] = res.get("shorts", [])
        self._results["playlist"] = res.get("playlist", [])
        self._results["channel"] = res.get("channel", [])

    @property
    def videos(self) -> List[YouTube]:
        if not self._results:
            self._get_results()
        return self._results.get("videos", [])

    @property
    def shorts(self) -> List[YouTube]:
        if not self._results:
            self._get_results()
        return self._results.get("shorts", [])

    @property
    def playlist(self) -> List[Playlist]:
        if not self._results:
            self._get_results()
        return self._results.get("playlist", [])

    @property
    def channel(self) -> List[Channel]:
        if not self._results:
            self._get_results()
        return self._results.get("channel", [])

    @property
    def all(self) -> List[Any]:
        """
        Combine all results in one list.
        """
        if not self._results:
            self._get_results()
        combined: List[Any] = []
        for arr in self._results.values():
            combined.extend(arr)
        return combined

    def get_next_results(self) -> None:
        """
        If there's a continuation, load more items, appending them to self._results.
        """
        if self._current_continuation:
            r, cont = self._fetch_and_parse(self._current_continuation)
            self._current_continuation = cont
            self._results["videos"].extend(r.get("videos", []))
            self._results["shorts"].extend(r.get("shorts", []))
            self._results["playlist"].extend(r.get("playlist", []))
            self._results["channel"].extend(r.get("channel", []))
        else:
            self._get_results()
