#!/usr/bin/python3
from pytube import Playlist
import os


def main():
    p = Playlist(
        "https://www.youtube.com/playlist?list=PLqgbMHsZiLUDrqIHDH8SDc1D06l5Mwefb"
    )
    print(f"Downloading: {p.title}")
    for video in p.videos:
        out_file = (
            video.streams.filter(only_audio=True).first().download(output_path=".")
        )
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)


if __name__ == "__main__":
    main()
