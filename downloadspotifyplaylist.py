from __future__ import unicode_literals
import mutagen
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import mutagen.id3
from mutagen.id3 import ID3
import youtube_dl, os, string, sys
from track import Track
from spotifyToYoutube import getTracksWithoutThoseNamedInString, searchYoutube


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
        print("\nSearching and downloading songs...")
        for track in tracks:
            songUrl = searchYoutube(track.titleString())
            if songUrl is not None:
                print('\nDownloading '+track.titleString())
                os.system('youtube-dl -x --output "'+track.titleString()+'.%(ext)s" --audio-format mp3 '+songUrl)

                # metatagging
                mp3file = MP3(track.titleString() + '.mp3', ID3=EasyID3)
                print(mp3file)

                mp3file['artist'] = [track.artist]
                mp3file['title'] = [track.title]
                mp3file['album'] = [track.album]
                mp3file.save()
        
    print("\nFinished!\n")
