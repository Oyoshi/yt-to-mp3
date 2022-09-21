import os
from pytube import YouTube
import pytube.request
from pytube.cli import on_progress

# TODO - move to some config
pytube.request.default_range_size = 32768

# TODO - move to a logger class
turquoise = "\033[38;2;00;255;200m"
default = "\033[39m"


class YouTubeVideoToMp3Converter:
    def __init__(self, playlists) -> None:
        self.playlists = playlists

    def execute(self) -> None:
        for playlist_name, video_ids in self.playlists.items():
            print(f"\nDownloading playlist {playlist_name}")
            for video_id in video_ids:
                self.download_video(playlist_name, video_id)

    def download_video(self, playlist_name, video_id) -> None:
        url = self.build_video_url(video_id)
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"Converting {yt.title}", turquoise)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=f"./{playlist_name}/")
        base, _ = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
        print(default, f"\nFinished converting: {yt.title}")

    def build_video_url(self, video_id) -> str:
        return f"https://youtu.be/{video_id}"
