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
import json
import logging
from bs4 import BeautifulSoup
from typing import Optional

logger = logging.getLogger(__name__)

def extract_json_object(text: str, start: int) -> Optional[str]:
    """
    Extract a well-formed JSON object from 'text', starting at 'start' index,
    accounting for nested braces/strings. Return substring or None.
    """
    if start < 0 or start >= len(text) or text[start] != "{":
        return None

    open_braces = 0
    in_string = False
    i = start
    while i < len(text):
        char = text[i]
        if char == '"' and (i == start or text[i - 1] != "\\"):
            in_string = not in_string
        if not in_string:
            if char == "{":
                open_braces += 1
            elif char == "}":
                open_braces -= 1
                if open_braces == 0:
                    return text[start : i + 1]
        i += 1
    return None

def extract_ytcfg(html: str) -> dict:
    """
    Finds <script> containing 'ytcfg.set({ ... })' and extracts that JSON.
    """
    soup = BeautifulSoup(html, "html.parser")
    for script in soup.find_all("script"):
        if script.string and "ytcfg.set(" in script.string:
            text = script.string
            start = text.find("ytcfg.set(") + len("ytcfg.set(")
            end = text.find(");", start)
            js = text[start:end].strip()
            try:
                return json.loads(js)
            except Exception as e:
                logger.error("Failed to parse ytcfg JSON", exc_info=e)
    return {}

def extract_initial_data(html: str) -> dict:
    """
    Finds <script> containing 'ytInitialData' and extracts that JSON.
    """
    soup = BeautifulSoup(html, "html.parser")
    for script in soup.find_all("script"):
        if script.string and "ytInitialData" in script.string:
            text = script.string
            if "var ytInitialData =" in text:
                start = text.find("var ytInitialData =") + len("var ytInitialData =")
                end = text.find(";", start)
                js = text[start:end].strip()
                try:
                    return json.loads(js)
                except Exception as e:
                    logger.error("Failed to parse ytInitialData", exc_info=e)
            elif 'window["ytInitialData"] =' in text:
                start = text.find('window["ytInitialData"] =') + len('window["ytInitialData"] =')
                end = text.find(";", start)
                js = text[start:end].strip()
                try:
                    return json.loads(js)
                except Exception as e:
                    logger.error("Failed to parse window[ytInitialData]", exc_info=e)
    return {}
