"""A video class."""

from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
        """Video constructor."""
        self._title = video_title
        self._video_id = video_id

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(video_tags)

    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self._video_id

    @property
    def tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self._tags

class Playlist:
    """A class used to represent a playlist."""

    def __init__(self, play_title: str, playlist_items: Sequence[str]):
        """Video constructor."""
        self._play_title = play_title

        # Turn the songs into a tuple here so it's unmodifiable,
        # in case the caller changes the 'playlist_songs' they passed to us
        self._items = tuple(playlist_items)

    @property
    def play_title(self) -> str:
        """Returns the title of a playlist."""
        return self._play_title

    @property
    def items(self) -> Sequence[str]:
        """Returns the list of songs of a playlist."""
        return self._items