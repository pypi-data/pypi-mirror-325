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
import os
import hashlib
import logging

logger = logging.getLogger(__name__)

class DiskCache:
    """
    A simple disk-based cache for storing HTTP GET responses.
    - Keyed by SHA256(url)
    - No expiration logic here: if the file exists, we treat it as valid.
    """

    def __init__(self, cache_folder: str = "http_cache") -> None:
        self.cache_folder = cache_folder
        os.makedirs(self.cache_folder, exist_ok=True)

    def _filename_for_url(self, url: str) -> str:
        h = hashlib.sha256(url.encode("utf-8")).hexdigest()
        return os.path.join(self.cache_folder, f"{h}.txt")

    def get(self, url: str) -> str | None:
        filepath = self._filename_for_url(url)
        if os.path.exists(filepath):
            logger.debug(f"[CACHE] Hit for URL: {url}")
            with open(filepath, "r", encoding="utf-8") as f:
                return f.read()
        return None

    def set(self, url: str, content: str) -> None:
        filepath = self._filename_for_url(url)
        logger.debug(f"[CACHE] Save content for URL: {url}")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
