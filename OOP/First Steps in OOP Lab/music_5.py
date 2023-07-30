class Music:
    def __init__(self, tittle, artist, lyrics):
        self.artist = artist
        self.title = tittle
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}'

    def play(self) -> str:
        return self.lyrics


song = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())
