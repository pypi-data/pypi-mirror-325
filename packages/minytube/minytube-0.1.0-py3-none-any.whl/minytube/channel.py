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
from urllib.parse import urlparse

from .playlist import Playlist

logger = logging.getLogger(__name__)

class Channel(Playlist):
    """
    A YouTube Channel, treated similarly to a playlist but with different URLs (about, videos, etc.).
    """

    def __init__(self, url: str, client: str = "WEB") -> None:
        super().__init__(url, client)
        parsed = urlparse(url)
        self.channel_uri = parsed.path
        self.channel_url = f"https://www.youtube.com{self.channel_uri}"

    def __repr__(self) -> str:
        return f"<Channel: {self.channel_uri}>"

    @property
    def channel_name(self) -> str:
        """
        Example: parse channel name from self.initial_data or HTML.
        """
        try:
            md = self.initial_data["metadata"]["channelMetadataRenderer"]
            return md["title"]
        except Exception:
            return ""
