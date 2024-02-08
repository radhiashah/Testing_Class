
# Testing- Class Design Recipe


## 1. Describe the Problem

""""


As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


""""



 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._




```python




class MusicCollection:
    def __init__(self):
        self.music = []

    def add_track(self, track):
        self.music.append(track)

    def get_tracklist(self):
        return self.tracklist






```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

# It will give an empty MusicCollection if nothing added yet
# Next one, will add track to MusicCollection
# When tracks added, can view list of all tracks added

def test_music_collection_instantiates_with_tracklist():
    music_collection = MusicCollection()

    actual = music_collection.get_tracklist
    expected = []

    assert actual == expected

def test_music_collection_add_track():
    music_collection = MusicCollection()
    music_collection.add_track("RadhiaSong")

    actual = music_collection.get_tracklist
    expected = ["RadhiaSong"]

    assert actual == expected

def test_music_collection_add_more_tracks():
    music_collection = MusicCollection()
    music_collection.add_track("RadhiaSong")
    music_collection.add_track("MatiSong")

    actual = music_collection.get_tracklist
    expected = ["RadhiaSong", "MatiSong"]

    assert actual == expected

    def tracks_listened_to()



"""





_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

