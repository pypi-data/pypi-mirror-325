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
import concurrent.futures
import logging
from typing import List, Optional

from .http_client import RequestsHttpClient

logger = logging.getLogger(__name__)

class MultiFetcher:
    """
    Helper for parallel downloading multiple URLs via ThreadPoolExecutor.
    """

    def __init__(self, http_client: RequestsHttpClient, max_workers: int = 10) -> None:
        self.http_client = http_client
        self.max_workers = max_workers

    def fetch_all(self, urls: List[str]) -> List[str]:
        """
        Fetch each URL concurrently, returning results in the same order.
        """
        results: List[Optional[str]] = [None] * len(urls)

        def worker(idx: int, u: str) -> str:
            return self.http_client.get(u)

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_index = {}
            for i, url in enumerate(urls):
                fut = executor.submit(worker, i, url)
                future_to_index[fut] = i

            for fut in concurrent.futures.as_completed(future_to_index):
                i = future_to_index[fut]
                try:
                    results[i] = fut.result()
                except Exception as e:
                    logger.error(f"Error fetching {urls[i]}: {e}")
                    results[i] = ""

        return [r if r is not None else "" for r in results]
