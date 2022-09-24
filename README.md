# yt-to-mp3

## About

Console application to download videos from __YouTube__ and convert them into __mp3__. It allows you to do couple of thing:

1.  download one or more __YouTube video(s)__ and convert them into __mp3__ files
2.  download one or more full __YouTube playlist(s)__ and convert each video into __mp3__ file
3.  download all your playlists (even private) - requires credentials from __Google__ authentication process [OAuth 2.0](https://developers.google.com/identity/protocols/oauth2)

For more options just take a look at help from the __CLI__: `python ./main.py --help`.

I'm not sure if it's 100% legal :trollface:.

## Demo

![Videos and Playlists](demos/demo_videos_playlists.gif)

## Prerequisites

1.  Optionally create [venv](https://docs.python.org/3/library/venv.html) 
2.  Install dependencies: `pip install -r requirements.txt`
3.  Generate OAuth 2.0 CLient ID in the [Google Cloud Platform Console](https://support.google.com/cloud/answer/6158849?hl=en)
4.  Download secrets as a json inside project folder and rename it to `client_secrets.json`
