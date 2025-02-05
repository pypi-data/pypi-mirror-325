# minytube

![minytube](https://img.shields.io/badge/python-3.7%2B-blue.svg) ![License](https://img.shields.io/badge/license-Apache%202.0-green)

**minytube** is a lightweight Python library for searching videos, extracting subtitles, and analyzing YouTube content without the need for the official API.

## Features

- 🔍 Search for videos, playlists, and channels
- 📜 Extract and process subtitles
- 🚀 Cache data for fast access
- ⚡ Minimal dependencies

## Installation

You can install the library via `pip`:

```sh
pip install git+https://github.com/bes-dev/minytube.git
```

## Usage

### Video Search

```python
from minytube import Search

search = Search("Python tutorial")
for video in search.videos[:5]:
    print(video.url)
```

### Extracting Subtitles

```python
from minytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
subtitles = yt.get_subtitles_info()

for lang, info in subtitles.items():
    print(f"Language: {lang}, URL: {info['url']}")
```

### Working with Playlists

```python
from minytube import Playlist

playlist = Playlist("https://www.youtube.com/playlist?list=PLx0sYbCqOb8QTF1DCJVkBzX7YV1LGwWzS")
for video_url in playlist[:5]:
    print(video_url)
```

### Working with Channels

```python
from minytube import Channel

channel = Channel("https://www.youtube.com/c/PythonDeveloper")
print(f"Channel: {channel.channel_name}")
```

## Requirements

- Python 3.7+
- `requests` >= 2.32.3
- `beautifulsoup4` >= 4.13.0

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.

## Contact

- Author: Sergei Belousov (aka BeS)
- GitHub: [bes-dev/minytube](https://github.com/bes-dev/minytube)
