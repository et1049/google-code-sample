"""A video library class."""

from .video import Video
from .video import Playlist
from pathlib import Path
import csv


# Helper Wrapper around CSV reader to strip whitespace from around
# each item.
def _csv_reader_with_strip(reader):
    yield from ((item.strip() for item in line) for line in reader)


class VideoLibrary:
    """A class used to represent a Video Library."""

    def __init__(self):
        """The VideoLibrary class is initialized."""
        self._videos = {}
        with open(Path(__file__).parent / "videos.txt") as video_file:
            reader = _csv_reader_with_strip(
                csv.reader(video_file, delimiter="|"))
            for video_info in reader:
                title, url, tags = video_info
                self._videos[url] = Video(
                    title,
                    url,
                    [tag.strip() for tag in tags.split(",")] if tags else [],
                )
        self._playlists = {}
        with open(Path(__file__).parent / "playlists.txt") as playlist_file:
            reader = _csv_reader_with_strip(
                csv.reader(playlist_file, delimiter="|"))
            for playlist_info in reader:
                title, items = playlist_info
                self._playlists[title] = Playlist(
                    title,
                    [item.strip() for item in items.split(",")] if items else [],
                )

    def get_all_videos(self):
        """Returns all available video information from the video library."""
        return list(self._videos.values())

    def get_video(self, video_id):
        """Returns the video object (title, url, tags) from the video library.

        Args:
            video_id: The video url.

        Returns:
            The Video object for the requested video_id. None if the video
            does not exist.
        """
        return self._videos.get(video_id, None)

    def get_all_playlists(self):
        """Returns all available playlist information from the video library."""
        return list(self._playlists.values())

    def get_playlist(self, playlist_title):
        """Returns the playlist object (title, items) from the video library.

        Args:
            playlist_title: The playlist title.

        Returns:
            The Playlist object for the requested playlist_title. None if the video
            does not exist.
        """
        return self._playlists.get(playlist_title, None)