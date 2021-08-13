import enum


class PlayState(enum.Enum):
    stopped = 0
    paused = 1
    playing = 2


class VideoState:
    def __init__(self):
        self._state = PlayState.stopped
        self._video = None

    def play(self, video_id):
        self._state = PlayState.playing
        self._video = video_id

    def check_playing(self):
        if self._video is None:
            vid_playing = 0
        else:
            vid_playing = 1
        return vid_playing

    def stop(self):
        """if somethings playing..."""
        if self.check_playing() == 1:
            self._state = PlayState.stopped
            self._video = None
            return 0
        else:
            return 1

    def vid_playing(self):
        if self.check_playing() == 1:
            return self._video
        else:
            return 0

    def pause(self):
        if self.check_playing() == 1:
            self._state = PlayState.paused
        return 0

    def restart(self):
        if self.check_playing() == 0:
            return 0
        else:
            if self._state != PlayState.paused:
                return 1
            self._state = PlayState.playing
            return 2
