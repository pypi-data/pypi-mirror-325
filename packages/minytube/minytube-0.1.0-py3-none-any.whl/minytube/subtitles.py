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
import xml.etree.ElementTree as ET
from html import unescape
from typing import List

from dataclasses import dataclass

from .globals_ import HTTP_CLIENT

logger = logging.getLogger(__name__)

@dataclass
class SubtitleLine:
    start: float
    dur: float
    text: str

def seconds_to_timestamp(seconds: float) -> str:
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int(round((seconds - int(seconds)) * 1000))
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

class SubtitleTrack:
    """
    Represents a single track of subtitles for a given video (url is XML).
    """

    def __init__(self, language: str, name: str, url: str) -> None:
        self.language = language
        self.name = name
        self.url = url

    def download(self) -> str:
        logger.debug(f"Downloading subtitles from {self.url}")
        return HTTP_CLIENT.get(self.url)

    def parse(self) -> List[SubtitleLine]:
        xml_text = self.download()
        try:
            root = ET.fromstring(xml_text)
        except Exception as e:
            logger.error("Error parsing subtitle XML", exc_info=e)
            return []

        lines: List[SubtitleLine] = []
        for elem in root.findall("text"):
            try:
                start = float(elem.attrib.get("start", "0"))
                dur = float(elem.attrib.get("dur", "0"))
                txt = elem.text or ""
                txt = unescape(txt)
                lines.append(SubtitleLine(start=start, dur=dur, text=txt))
            except Exception as exc:
                logger.error("Error parsing a single subtitle line", exc_info=exc)
        return lines

    def to_srt(self) -> str:
        lines = self.parse()
        blocks: List[str] = []
        for i, line in enumerate(lines, start=1):
            start_ts = seconds_to_timestamp(line.start)
            end_ts = seconds_to_timestamp(line.start + line.dur)
            block = f"{i}\n{start_ts} --> {end_ts}\n{line.text}\n"
            blocks.append(block)
        return "\n".join(blocks)

    def to_plain(self) -> str:
        lines = self.parse()
        return "\n".join(line.text for line in lines)

    def save(self, filename: str, fmt: str = "srt") -> None:
        if fmt.lower() == "srt":
            content = self.to_srt()
        elif fmt.lower() == "plain":
            content = self.to_plain()
        else:
            lines = self.parse()
            content = "\n".join(line.text for line in lines)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
