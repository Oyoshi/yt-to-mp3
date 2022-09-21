import os
from pytube import YouTube


class YouTubeVideoToMp3Converter:
    def __init__(self, playlists) -> None:
        self.playlists = playlists

    def execute(self):
        for playlist_name, videos in self.playlists.items():
            video_urls = [self.build_video_url(video_id) for video_id in videos]
            for url in video_urls:
                print(f"Downloading {playlist_name}: {url}")
                yt = YouTube(url)
                video = yt.streams.filter(only_audio=True).first()
                out_file = video.download(output_path=f"./${playlist_name}/")
                base, _ = os.path.splitext(out_file)
                new_file = base + ".mp3"
                os.rename(out_file, new_file)

    def build_video_url(self, video_id) -> str:
        return f"https://youtu.be/{video_id}"
