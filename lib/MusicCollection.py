class MusicCollection:
    def __init__(self):
        self.music = []

    def add_track(self, track):
        self.music.append(track)

    def get_tracklist(self):
        return self.music

music_collection = MusicCollection()
music_collection.add_track("RadhiaSong")
music_collection.add_track("MatiSong")

# print(music_collection.get_tracklist)