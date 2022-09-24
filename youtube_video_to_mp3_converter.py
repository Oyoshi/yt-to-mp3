from pytube import YouTube, Playlist
from logger import on_progress, log
import pytube.request
import os

# override default value to display progress bar
# otherwise chunk size is less than default_range_size
# and on_progress is being called only at the end
pytube.request.default_range_size = 32768


class YouTubeVideoToMp3Converter:
    def __init__(self, config, my_playlists) -> None:
        self.config = config
        self.my_playlists = my_playlists

    def execute(self) -> None:
        if self.config.videos:
            for video in self.config.videos:
                self.convert_video(video)
        if self.config.playlists:
            for playlist_url in self.config.playlists:
                playlist = Playlist(playlist_url)
                self.convert_playlist(playlist.video_urls, playlist.title)
        if self.my_playlists:
            for playlist_name, video_ids in self.my_playlists.items():
                self.convert_playlist(video_ids, playlist_name)

    def convert_playlist(self, videos, playlist_name) -> None:
        log(f"\nDownloading playlist {playlist_name}\n")
        for video in videos:
            self.convert_video(video, playlist_name)

    def convert_video(self, video, playlist_name=None) -> None:
        url = video if video.startswith("http") else self.build_video_url(video)
        yt = YouTube(url, on_progress_callback=on_progress)
        log(f"\nConverting {yt.title}")
        video = yt.streams.filter(only_audio=True).first()
        output_path = self.config.dir if self.config.dir else "./"
        output_path = f"{output_path}/{playlist_name}" if playlist_name else output_path
        out_file = video.download(output_path=output_path)
        base, _ = os.path.splitext(out_file)
        os.rename(out_file, f"{base}.mp3")
        log(f"\nFinished converting: {yt.title}\n")

    def build_video_url(self, video_id) -> str:
        return f"https://youtu.be/{video_id}"
