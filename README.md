# yt-playlist
A YouTube playlist downloader. Requires [Python 3.11+](https://www.python.org/downloads/), [pytube](https://github.com/nficano/pytube), and [ffmpeg](https://www.ffmpeg.org/) to work.

This script will download the audio of every song in a YouTube playlist, then convert the audio to mp3. To use, place it in the folder in which you want to download the playlist.

I am not actively monitoring this but I'll merge any updates that anyone else wants to make.

## Packages and versions
- pytube==12.1.0

## Installation
1. git clone ``https://github.com/voladdd/yt-playlist.git`` or download the source code
2. navigate to the folder
3. create python virtual environment and activate it:
``python -m venv .venv ``
``.venv\Scripts\activate``
4. do ``pip install -r requirements.txt`` to install the package from requirements.txt
5. do ``py yt-playlist-download.py``
6. enjoy!

## Usage
- ``Put playlists urls you wish to download at playlists-urls-to-download.txt file: `` - playlist from youtube only
    - e.g. ``https://www.youtube.com/playlist?list=OLAK5uy_lbX9HmX4ZrMSrS5wpDonp-EFy4IrhQeCc``
