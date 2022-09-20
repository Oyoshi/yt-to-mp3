#!/usr/bin/python3
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


class YouTubePlaylistsDownloader:
    def __init__(self):
        credentials = self.get_credentials()
        self.youtube = build("youtube", "v3", credentials=credentials)

    def get_credentials(self):
        flow = InstalledAppFlow.from_client_secrets_file(
            "client_secrets.json",
            scopes=["https://www.googleapis.com/auth/youtube.readonly"],
        )
        flow.run_local_server(port=8080, prompt="consent")
        return flow.credentials

    def execute(self):
        result = {}
        mine_playlists = self.get_mine_playlists()
        for playlist in mine_playlists:
            playlist_name = playlist["snippet"]["title"]
            playlist_id = playlist["id"]
            videos = [
                video["contentDetails"]["videoId"]
                for video in self.get_all_videos(playlist_id)
            ]
            result[playlist_name] = videos
        return result
        # yt_url = f"https://youtu.be/{video_id}"

    def get_mine_playlists(self):
        request = self.youtube.playlists().list(part="snippet", mine=True)
        response = request.execute()
        return response["items"]

    def get_all_videos(self, playlist_id):
        request = self.youtube.playlistItems().list(
            part="contentDetails", playlistId=playlist_id
        )
        response = request.execute()
        return response["items"]


def main():
    downloader = YouTubePlaylistsDownloader()
    print(downloader.execute())


if __name__ == "__main__":
    main()
