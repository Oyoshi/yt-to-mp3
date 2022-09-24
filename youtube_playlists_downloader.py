from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


class YouTubePlaylistsDownloader:
    def __init__(self, config) -> None:
        self.config = config

    def execute(self):
        if not self.config.all:
            return None
        credentials = self.get_credentials()
        youtube = build("youtube", "v3", credentials=credentials)
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

    def get_credentials(self):
        flow = InstalledAppFlow.from_client_secrets_file(
            "client_secrets.json",
            scopes=["https://www.googleapis.com/auth/youtube.readonly"],
        )
        flow.run_local_server(port=8080, prompt="consent")
        return flow.credentials

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
