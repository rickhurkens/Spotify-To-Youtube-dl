class Track:

    def __init__(self, artist, title, album):
        self.artist = artist
        self.title = title
        self.album = album

    def titleString(self):
        return self.artist + " - " + self.title