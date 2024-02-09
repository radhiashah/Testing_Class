# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface

_Include the initializer, 


public properties, and public methods with all parameters, return values, and side-effects._

```python


class MusicCollection():
    # User-facing properties:
    #   name: dictionary

    def __init__(self):
        self.music = []
        pass # No code here yet

    def add_track(self, track):
        self.music.append(track)= []
        pass # No code here yet

    def get_tracklist(self):
        return self.music
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# It will give an empty MusicCollection if nothing added yet
# Next one, will add track to MusicCollection
# When the tracks are added, we can view lists of all track added

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


"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
