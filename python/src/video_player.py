"""A video player class."""

from .video_library import VideoLibrary
import random
global video_playing
video_playing = ""
global video_paused
video_paused = ""




class VideoPlayer:
    """A class used to represent a Video Player."""
    def __init__(self):
        self._video_library = VideoLibrary()

    def clear(self):
        global video_playing                    # Clears the variables between tests
        global video_paused
        video_playing = ''
        video_paused = ''

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        videos = self._video_library.get_all_videos()
        all_videos = []

        for video in videos:
            tags = []
            for tag in video.tags:
                tags.append(str(tag))
            all_videos.append((str(video.title) + ' (' + str(video.video_id) + str(') [') +str(' '.join(tags))  + str(']')))
            all_videos.sort(key = lambda list: list[0])
        print("Here's a list of all available videos:")
        for item in all_videos:
            print(item)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        global video_playing
        global video_paused
        if self._video_library.get_video(video_id) == None:
            print('Cannot play video: Video does not exist')
        else:
            if video_playing != '':
                print("Stopping video:", self._video_library.get_video(video_playing).title)
                video_playing = ''
                video_paused = ''
            if video_paused != '':
                print("Stopping video:", self._video_library.get_video(video_paused).title)
                video_playing = ''
                video_paused = ''
            video = self._video_library.get_video(video_id)
            print("Playing video:", video.title)
            video_playing = video.video_id
            video_paused = ''

    def stop_video(self):
        """Stops the current video."""
        global video_playing
        global video_paused
        if video_playing == '':
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video:", self._video_library.get_video(video_playing).title)
            video_playing = ''
            video_paused = ''

    def play_random_video(self):
        """Plays a random video from the video library."""
        videos = list(self._video_library.get_all_videos())
        choices = []
        for video in videos:
            choices.append(video.video_id)
        video_id = random.choice(choices)
        global video_playing
        global video_paused
        if self._video_library.get_video(video_id) == None:
            print('Cannot play video: Video does not exist')
        else:
            if video_playing != '':
                print('Stopping video:', self._video_library.get_video(video_playing).title)
                video_playing = ''
                video_paused = ''
            video = self._video_library.get_video(video_id)
            print("Playing video:", video.title)
            video_playing = video.video_id



    def pause_video(self):
        """Pauses the current video."""
        global video_playing
        global video_paused
        if video_paused != '':
            video = self._video_library.get_video(video_paused)
            print('Video already paused:', video.title)
        elif video_playing == '':
            print('Cannot pause video: No video is currently playing')
        else:
            video = self._video_library.get_video(video_playing)
            video_paused = video_playing
            print('Pausing video:', video.title)
            video_playing = ''


    def continue_video(self):
        """Resumes playing the current video."""

        global video_playing
        global video_paused
        if video_playing == '' and video_paused == '':
            print('Cannot continue video: No video is currently playing')
        elif video_paused == '' and video_playing != '':
            print('Cannot continue video: Video is not paused')
        else:
            video = self._video_library.get_video(video_paused)
            print('Continuing video:', video.title)
            video_playing = video_paused
            video_paused = ''

    def show_playing(self):
        """Displays video currently playing."""

        global video_playing
        if video_paused != '':
            video = self._video_library.get_video(video_paused)
            tags = []
            for tag in video.tags:
                tags.append(str(tag))
            print('Currently playing: ' + str(video.title), '(' + str(video.video_id) + str(') [') +str(' '.join(tags))  + str(']'), '- PAUSED')

        elif video_playing == '':
            print('No video is currently playing')

        else:
            video = self._video_library.get_video(video_playing)
            tags = []
            for tag in video.tags:
                tags.append(str(tag))
            print('Currently playing: ' + str(video.title), '(' + str(video.video_id) + str(') [') +str(' '.join(tags))  + str(']'))



    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

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
