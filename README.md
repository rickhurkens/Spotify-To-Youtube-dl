# Spotify To Youtube ▶
A simplistic way to find songs from a Spotify playlist on YouTube and download them in the highest available quality.<br>
<b><i>IMPORTANT:</i> Please check the issue saulojoab has pinned <a href="https://github.com/saulojoab/Spotify-To-Youtube/issues">here</a>.</b>

# How does it work? 😮
All you gotta do is insert your <b> >>PUBLIC<< </b> <a href="http://www.spotify.com">Spotify</a> playlist URL or ID when prompted, then the app will automatically search all songs from that playlist on <a href="http://youtube.com">YouTube</a> and return the URLs. Youtube-dl will download them. Check below for instructions on how to make it work:

# Prerequisites:
youtube-dl<br>
ffmpeg<br>
mutagen easyid3

# How to use it?
1 - To use the script, you gotta register your app on both the Spotify and YouTube API services.<br>
2 - When you finish doing that, <b>create a JSON file</b> named <i>"config.json"</i> on the project's main folder.<br>
3 - The <i>config.json</i> file <b>must have</b> the following format:
```js
{
    "spotify":
    {
        "client_id": "your_spotify_client_id",
        "client_secret": "your_spotify_client_secret"
    },
    "youtube":
    {
        "api_key": "your_youtube_api_key",
        "client_id": "your_youtube_client_id",
        "client_secret": "your_youtube_client_secret"
    }
}
```

# What did you use to make it? :thinking:
I used the following libraries:<br>
  - <a href="https://github.com/plamere/spotipy">Spotipy (For handling the Spotify API)</a>
  - <a href="https://github.com/rohitkhatri/youtube-python">YouTube Python (For handling the YouTube API)</a>
  - <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">Beautiful Soup (For the YouTube alternative search)</a>
  - <a href="https://github.com/ytdl-org/youtube-dl">youtube-dl (For the youtube download)</a>
  - <a href="https://github.com/quodlibet/mutagen/blob/master/mutagen/easyid3.py">Mutagen EasyID3 (For the metadata tagging)</a><br><br>

# Why did you make it?
Studying purpouses, and it might actually be useful to someone. I think <a href="http://discord.app">Discord</a> bots could use that to queue songs and stuff. 

# Contribute?
This project needs:
  - Handling of errors
  - Output of logs
  - Refactoring