from __future__ import unicode_literals
from spotifyToYoutube import getTracksWithoutThoseNamedInString, searchYoutube
import youtube_dl, os, string, sys


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}


if (__name__ == "__main__"):
    playlistId = sys.argv[1] if len(sys.argv) > 1 else str(input("Insert Spotify playlist URL: "))
    if ("spotify.com" in playlistId):
        playlistId = playlistId.split("/playlist/")[1]

    filenames = "".join(os.listdir())
    tracks = getTracksWithoutThoseNamedInString(playlistId, filenames)

    if len(tracks) > 0:
        print("Searching and downloading songs...")
        for trackTitle,trackData in tracks.items():
            songUrl = searchYoutube(trackTitle)
            if songUrl is not None:
                print('\nDownloading '+trackTitle)
                os.system('youtube-dl -x --output "'+trackTitle+'.%(ext)s" --audio-format mp3 '+songUrl)

        # TODO: possibly use from mutagen.easyid3 import EasyID3 for metatagging
        # then we'd need to create an object with also artist (String) and title (String)

    print("\nFinished!\n")
