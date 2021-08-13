"""A video playlist class."""

from TRY2.video_playlist import Playlist


class PlaylistLibrary:
    def __init__(self):
        self._playlist = {}

    def __contains__(self, playlist_name: str):
        return playlist_name.lower() in self._playlist

    def create(self, name:str):
        if name in self:
            return 0
        else:
            self._playlist[name.lower()] = Playlist(name)
            return 1

    def get_all_playlists(self):
        return sorted(self._playlist.values(), key=str)

    def __getitem__(self, playlist_name):
        """Overloading __getitem__ will allow us to use the [] operator for
        the VideoPlaylistLibrary. e.g. we can do playlist_library[playlistname]
        to retrieve a playlist from the library.

        Here, we do the lookup in lowercase, because the playlist name should
        not be case sensitive.
        """
        if playlist_name in self.get_all_playlists():
            return self._playlist[playlist_name]
        else:
            return 0