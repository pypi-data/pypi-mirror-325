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
import requests
from requests import Response
import logging
from typing import Optional

from .disk_cache import DiskCache

logger = logging.getLogger(__name__)

class RequestsHttpClient:
    """
    HTTP client using requests.Session for keep-alive and optional DiskCache.
    """

    def __init__(self, cache: Optional[DiskCache] = None) -> None:
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Mozilla/5.0"})
        self.cache = cache

    def get(self, url: str) -> str:
        """
        Perform a GET request, returning the text content.
        Use disk cache if present.
        """
        if self.cache:
            cached_content = self.cache.get(url)
            if cached_content is not None:
                return cached_content

        resp: Response = self.session.get(url)
        resp.raise_for_status()
        text_content = resp.text

        if self.cache:
            self.cache.set(url, text_content)

        return text_content
