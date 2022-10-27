#!/usr/bin/python3
from argparse import ArgumentParser
from youtube_my_playlists_downloader import YouTubeMyPlaylistsDownloader
from youtube_video_to_mp3_converter import YouTubeVideoToMp3Converter


def main():
    args_parser = create_args_parser()
    config = args_parser.parse_args()
    playlists_downloader = YouTubeMyPlaylistsDownloader(config)
    my_playlists = playlists_downloader.execute()
    converter = YouTubeVideoToMp3Converter(config, my_playlists)
    converter.execute()


def create_args_parser():
    args_parser = ArgumentParser(
        description="Convert YT video into mp3", allow_abbrev=False
    )
    args_parser.add_argument(
        "-v", "--videos", nargs="+", help="list of urls or video ids"
    )
    args_parser.add_argument(
        "-p", "--playlists", nargs="+", help="list of urls or playlist ids"
    )
    args_parser.add_argument(
        "-a", "--all", action="store_true", help="convert my all playlists"
    )
    args_parser.add_argument(
        "-d",
        "--dir",
        help="destination directory for converted videos",
    )
    return args_parser


if __name__ == "__main__":
    main()
