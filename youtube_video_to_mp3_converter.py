from pytube import YouTube

# from pytube.cli import on_progress
from logger import on_progress, log
import pytube.request
import os

# override default value to display progress bar
# otherwise chunk size is less than default_range_size
# and on_progress is being called only at the end
pytube.request.default_range_size = 32768


class YouTubeVideoToMp3Converter:
    def __init__(self, playlists) -> None:
        self.playlists = playlists

    def execute(self) -> None:
        for playlist_name, video_ids in self.playlists.items():
            log(f"\nDownloading playlist {playlist_name}\n")
            for video_id in video_ids:
                self.download_video(playlist_name, video_id)

    def download_video(self, playlist_name, video_id) -> None:
        url = self.build_video_url(video_id)
        yt = YouTube(url, on_progress_callback=on_progress)
        log(f"Converting {yt.title}")
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=f"./{playlist_name}/")
        base, _ = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
        log(f"\nFinished converting: {yt.title}\n")

    def build_video_url(self, video_id) -> str:
        return f"https://youtu.be/{video_id}"
