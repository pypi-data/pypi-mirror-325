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
from typing import Any, Dict
logger = logging.getLogger(__name__)

class Filter:
    """
    Build search filters in a simplified proto-like structure.
    """

    def __init__(self) -> None:
        self.filters = {
            "upload_date": None,
            "type": None,
            "duration": None,
            "features": [],
            "sort_by": None
        }

    def set_filters(self, filter_dict: dict) -> None:
        for category, val in filter_dict.items():
            if category == "features":
                if isinstance(val, list):
                    self.filters["features"].extend(val)
                else:
                    self.filters["features"].append(val)
            else:
                self.filters[category] = val

    def clear_filters(self) -> None:
        for cat in self.filters:
            if cat == "features":
                self.filters[cat] = []
            else:
                self.filters[cat] = None

    def get_filters_params(self) -> bytes:
        combined: Dict[int, Any] = {}
        if self.filters["sort_by"]:
            combined.update(self.filters["sort_by"])
        combined[2] = {}
        if self.filters["type"]:
            combined[2].update(self.filters["type"])
        if self.filters["duration"]:
            combined[2].update(self.filters["duration"])
        if self.filters["features"]:
            for feat in self.filters["features"]:
                combined[2].update(feat)
        if self.filters["upload_date"]:
            combined[2].update(self.filters["upload_date"])
        combined[2] = dict(sorted(combined[2].items()))
        logger.debug(f"Combined filters: {combined}")
        encoded = str(combined).encode("utf-8")
        logger.debug(f"Encoded filter: {encoded}")
        return encoded
