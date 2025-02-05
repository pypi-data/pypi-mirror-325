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
from typing import Optional

from .globals_ import HTTP_CLIENT, logger

class InnerTube:
    """
    Minimal interface to YouTube internal API for browsing and searching.
    """

    def __init__(self, client: str = "WEB") -> None:
        self.client = client
        self.api_url = "https://www.youtube.com/youtubei/v1"
        self.api_key: Optional[str] = None

    def set_api_key(self, api_key: str) -> None:
        self.api_key = api_key

    def browse(self, continuation: str) -> dict:
        url = f"{self.api_url}/browse?key={self.api_key}" if self.api_key else f"{self.api_url}/browse"
        data = {
            "context": {
                "client": {
                    "clientName": self.client,
                    "clientVersion": "2.20201021.03.00"
                }
            },
            "continuation": continuation
        }
        resp = HTTP_CLIENT.session.post(url, json=data)
        resp.raise_for_status()
        return resp.json()

    def search(self, query: str, continuation: Optional[str] = None, data: Optional[dict] = None) -> dict:
        url = f"{self.api_url}/search?key={self.api_key}" if self.api_key else f"{self.api_url}/search"
        payload: dict = {
            "context": {
                "client": {
                    "clientName": self.client,
                    "clientVersion": "2.20201021.03.00"
                }
            },
            "query": query
        }
        if continuation:
            payload["continuation"] = continuation
        if data:
            payload.update(data)

        resp = HTTP_CLIENT.session.post(url, json=payload)
        resp.raise_for_status()
        return resp.json()
