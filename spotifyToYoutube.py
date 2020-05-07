#coding: utf-8
import json
# System stuff
import pathlib
# Spotify library.
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# URL conversions.
import urllib.request
import bs4
# Youtube stuff.
import youtube

# Opening our JSON configuration file (which has our tokens).
with open(pathlib.Path(__file__).parent / 'config.json', encoding='utf-8-sig') as json_file:
    APIs = json.load(json_file)

def getTracks(playlistId):
    return getTracksWithoutThoseNamedInString(playlistId, "")

def getTracksWithoutThoseNamedInString(playlistId, string):

    # Creating and authenticating our Spotify app.
    client_credentials_manager = SpotifyClientCredentials(APIs["spotify"]["client_id"], APIs["spotify"]["client_secret"])
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Getting a playlist.
    playlist = spotify.user_playlist(user="",playlist_id=playlistId)
    print("\nDownloading playlist '" + playlist["name"] + "'")

    # Getting the tracks.
    results = playlist["tracks"]

    trackList = {};
    # For each track in the playlist
    for i in playlist["tracks"]["items"]:
        track = i["track"]
        title = track["name"]

        # For each artist in the track.
        artistName = ""
        for index, artist in enumerate(track["artists"]):
            artistName += (artist["name"])
            # If it isn't the last artist.
            if (track["artists"].__len__() - 1 != index):
                artistName += ", "

        titleString = artistName + " - " + title
        # If this song title is already in current directory, do nothing
        if (titleString in string):
            print("Not downloading because of title match: " + titleString)
            continue
        
        # Adding the track to the list.
        trackList[titleString] = {"artist": artistName, "title": title}

    return trackList;


def searchYoutubeAlternative(songName):
    # YouTube will block you if you query too many songs using this search.
    textToSearch = songName
    query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = bs4(html, 'html.parser')
    for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
        print('https://www.youtube.com' + vid['href'])

def searchYoutube(songName):
    api = youtube.API(client_id=APIs["youtube"]["client_id"],
              client_secret=APIs["youtube"]["client_secret"],
              api_key=APIs["youtube"]["api_key"]);
    video = api.get('search', q=songName, maxResults=1, type='video', order='relevance');
    if (len(video["items"]) <  1):
        print("Could not find youtube video for " + songName)
        return None
    return("https://www.youtube.com/watch?v="+video["items"][0]["id"]["videoId"]);

if (__name__ == "__main__"):
    tracks = getTracks(str(input("Insert Spotify playlist URL: ")));
    print("Searching songs...");
    songs = [];
    for i in tracks:
        songs.append(searchYoutube(i));
    print("Search finished!");

    print("URL LIST: ");
    for i in songs:
        print(i);
