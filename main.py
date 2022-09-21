#!/usr/bin/python3
from youtube_playlists_downloader import YouTubePlaylistsDownloader
from youtube_video_to_mp3_converter import YouTubeVideoToMp3Converter


def main():
    playlists_downloader = YouTubePlaylistsDownloader()
    playlists = playlists_downloader.execute()
    converter = YouTubeVideoToMp3Converter(playlists)
    converter.execute()


if __name__ == "__main__":
    main()
