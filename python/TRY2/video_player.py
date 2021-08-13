"""A video player class."""

from TRY2.video_library import VideoLibrary
from TRY2.video_state import PlayState, VideoState
from TRY2.video_playlist import Playlist
from . import video_playlist_library

import random

"""PLAY funny_dogs_video_id"""


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._playback = VideoState()
        self._playlist = video_playlist_library.PlaylistLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        for vids_in_order in self._video_library.get_all_videos():
            print(vids_in_order)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        if video is None:
            print("Cannot play video: Video does not exist")
        else:
            if self._playback._state != PlayState.stopped:
                self.stop_video()
            self._playback.play(video_id)
            print(f"Playing video: {video.title}")

    def stop_video(self):
        """Stops the current video."""
        video = self._playback.vid_playing()
        if video == 0:
            print(f"Cannot stop video: No video is currently playing")
        else:
            videoID = self._video_library.get_video(video)
            print(f"Stopping video: {videoID.title}")
            self._playback.stop()

    def play_random_video(self):
        """Plays a random video from the video library."""
        if self._playback._state != PlayState.stopped:
            self.stop_video()
        video_id = random.choice(self._video_library.get_all_videos()).video_id
        self.play_video(video_id)

    def pause_video(self):
        """Pauses the current video."""
        video = self._playback.vid_playing()
        if self._playback.check_playing() == 0:
            print(f"Cannot pause video: No video is currently playing")
        elif self._playback._state == PlayState.paused:
            print(f"Video already paused: {self._video_library.get_video(video).title}")
        else:
            print(f"Pausing video: {self._video_library.get_video(video).title}")
            self._playback.pause()

    def continue_video(self):
        """Resumes playing the current video."""
        restart = self._playback.restart()
        video = self._playback.vid_playing()
        if restart == 0:
            print("Cannot continue video: No video is currently playing")
        elif restart == 1:
            print("Cannot continue video: Video is not paused")
        elif restart == 2:
            print(f"Continuing video: {self._video_library.get_video(video).title}")
            self._playback.play(self._video_library.get_video(video).video_id)

    def show_playing(self):
        """Displays video currently playing."""
        if self._playback._state == PlayState.stopped:
            print("No video is currently playing")
        elif self._playback._state == PlayState.paused:
            print(f"Currently playing: {self._video_library.get_video(self._playback.vid_playing())} - PAUSED")
        elif self._playback._state == PlayState.playing:
            print(f"Currently playing: {self._video_library.get_video(self._playback.vid_playing())}")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if self._playlist.create(playlist_name) == 0:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self._playlist.create(playlist_name)
            print(f"Successfully created new playlist: {playlist_name}")


    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if playlist_name not in self._playlist:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
        elif self._video_library.get_video(video_id) is None:
            print(f"Cannot add video to {playlist_name}: Video does not exist")
        elif video_id in self._video_library:
            print(f"Cannot add video to {playlist_name}: Video already added")
        else:
            playlist = self._playlist[playlist_name]
            video = self._video_library[video_id]
            playlist.add_vid(video)
            print(f"Added video to {playlist_name}: {video.title}")

        """elif Playlist(playlist_name).add_vid(video_id) == 0:
            print(f"Cannot add video to {playlist_name}: Video already added")
        else:
            playlist = self._playlist[playlist_name]
            video = self._video_library[video_id]
            playlist.add_vid(video)
            print(f"Added video to {playlist_name}: {video.title}")"""

    def show_all_playlists(self):

        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
