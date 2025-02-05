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
import json
from bs4 import BeautifulSoup
from typing import Optional

from .globals_ import HTTP_CLIENT, logger
from .json_extractor import extract_json_object

class YouTube:
    """
    Represents a single YouTube video page.
    Capable of extracting subtitles info from HTML.
    """

    def __init__(self, url: str) -> None:
        self.url = self._normalize_url(url)
        self._html: Optional[str] = None

    def __repr__(self) -> str:
        return f"<YouTube video: {self.url}>"

    def _normalize_url(self, url: str) -> str:
        if url.startswith("/"):
            return "https://www.youtube.com" + url
        return url

    @property
    def html(self) -> str:
        if self._html is None:
            self._html = HTTP_CLIENT.get(self.url)
        return self._html

    def get_subtitles_info(self) -> dict:
        soup = BeautifulSoup(self.html, "html.parser")
        for script in soup.find_all("script"):
            if script.string and "ytInitialPlayerResponse" in script.string:
                text = script.string
                json_text: Optional[str] = None

                if "ytInitialPlayerResponse =" in text:
                    start = text.find("ytInitialPlayerResponse =") + len("ytInitialPlayerResponse =")
                    first_brace = text.find("{", start)
                    json_text = extract_json_object(text, first_brace)
                elif 'window["ytInitialPlayerResponse"] =' in text:
                    start = text.find('window["ytInitialPlayerResponse"] =') + len('window["ytInitialPlayerResponse"] =')
                    first_brace = text.find("{", start)
                    json_text = extract_json_object(text, first_brace)

                if json_text is None:
                    logger.error("Failed to extract JSON from ytInitialPlayerResponse.")
                    continue
                try:
                    player_response = json.loads(json_text)
                except Exception as e:
                    logger.error("Error parsing ytInitialPlayerResponse", exc_info=e)
                    continue

                captions = player_response.get("captions")
                if not captions:
                    logger.info("No subtitles found in player's data.")
                    return {}

                tracklist = captions.get("playerCaptionsTracklistRenderer", {})
                tracks = tracklist.get("captionTracks", [])
                subs_info = {}
                for trk in tracks:
                    lang_code = trk.get("languageCode", "")
                    name_ = trk.get("name", {}).get("simpleText", "")
                    base_url = trk.get("baseUrl", "")
                    subs_info[lang_code] = {
                        "name": name_,
                        "url": base_url
                    }
                return subs_info
        logger.error("No ytInitialPlayerResponse found in HTML.")
        return {}
