"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self, name:str):
        self._name = name
        self._videos = []

    @property
    def name(self):
        return self._name

    @property
    def videos(self):
        return tuple(self._videos)

    def __str__(self):
        return self._name

    def add_vid(self, video_id):
        if video_id in self:
            return 0
        else:
            self._videos.append(video_id)
            return 1

    def remove_vid(self, video_id):
        if video_id in self:
            self._videos.remove(video_id)
            return 0
        else:
            return 1

    def __contains__(self, video):
        return video in self._videos