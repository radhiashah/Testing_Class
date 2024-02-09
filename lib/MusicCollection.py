class MusicCollection():
    
    def __init__(self):
        self.music = []

    def add_track(self, track):
        self.music.append(track)

    def get_tracklist(self):
        return self.music