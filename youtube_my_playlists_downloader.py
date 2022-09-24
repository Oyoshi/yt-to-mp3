from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import os
import pickle


class YouTubeMyPlaylistsDownloader:
    def __init__(self, config) -> None:
        self.config = config
        self.credentials = None

    def execute(self):
        if not self.config.all:
            return None
        self.set_credentials()
        youtube = build("youtube", "v3", credentials=self.credentials)
        result = {}
        mine_playlists = self.get_my_playlists(youtube)
        for playlist in mine_playlists:
            playlist_name = playlist["snippet"]["title"]
            playlist_id = playlist["id"]
            videos = [
                video["contentDetails"]["videoId"]
                for video in self.get_all_videos(youtube, playlist_id)
            ]
            result[playlist_name] = videos
        return result

    def set_credentials(self):
        self.try_load_credentials_from_file()
        if not self.credentials or not self.credentials.valid:
            if (
                self.credentials
                and self.credentials.expired
                and self.credentials.refresh_token
            ):
                self.fetch_refresh_token()
            else:
                self.fetch_new_credentials()

    def try_load_credentials_from_file(self):
        if os.path.exists("token.pickle"):
            with open("token.pickle", "rb") as token:
                self.credentials = pickle.load(token)

    def fetch_refresh_token(self):
        self.credentials.refresh(Request())

    def fetch_new_credentials(self):
        flow = InstalledAppFlow.from_client_secrets_file(
            "client_secrets.json",
            scopes=["https://www.googleapis.com/auth/youtube.readonly"],
        )
        flow.run_local_server(port=8080, prompt="consent")
        self.credentials = flow.credentials

    def get_my_playlists(self, youtube):
        request = youtube.playlists().list(part="snippet", mine=True)
        response = request.execute()
        return response["items"]

    def get_all_videos(self, youtube, playlist_id):
        request = youtube.playlistItems().list(
            part="contentDetails", playlistId=playlist_id
        )
        response = request.execute()
        return response["items"]
