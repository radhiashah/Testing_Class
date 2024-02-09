from lib.MusicCollection import *
import pytest

def test_music_collection_instantiates_with_tracklist():
    music_collection = MusicCollection()

    actual = music_collection.get_tracklist()
    expected = []

    assert actual == expected

def test_music_collection_add_track():
    music_collection = MusicCollection()
    music_collection.add_track("RadhiaSong")

    actual = music_collection.get_tracklist()
    expected = ["RadhiaSong"]

    assert actual == expected

def test_music_collection_add_more_tracks():
    music_collection = MusicCollection()
    music_collection.add_track("RadhiaSong")
    music_collection.add_track("MatiSong")

    actual = music_collection.get_tracklist()
    expected = ["RadhiaSong", "MatiSong"]

    assert actual == expected
