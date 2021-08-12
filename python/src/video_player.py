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
        playlists = self._video_library.get_all_playlists()
        names = []
        for playlist in playlists:
            names.append(playlist.play_title)
        if playlist_name.upper() in (name.upper() for name in names):
            print('Cannot create playlist: A playlist with the same name already exists')
        else:
            file = open("playlists.txt", "a+", newline='')
            file.seek(0)
            if len(file.readlines()) == 0:
                line = str(playlist_name + '|')
            else:
                line = str("\n" + playlist_name + '|')
            file.seek(0)
            file.write(line)
            file.close()
            self._video_library.__init__()
            print("Successfully created new playlist:", playlist_name)



    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        file = open("playlists.txt", "r")
        file.seek(0)
        data = file.readlines()
        lines = []
        for line in data:
            line = line.split('|')
            lines.append(line)
        if len(data) == 0:
            print('Cannot add video to', playlist_name + ': Playlist does not exist')
        else:
            names = []
            for i in range (0, len(lines)):
                names.append(lines[i][0])
            if playlist_name.upper() not in (name.upper() for name in names):
                print('Cannot add video to', playlist_name + ': Playlist does not exist')
            elif self._video_library.get_video(video_id) == None:
                print('Cannot add video to', playlist_name + ': Video does not exist')
            else:
                for name in range (0, len(names)):
                    if names[name].upper() == playlist_name.upper():
                        play_index = name
                if video_id in lines[play_index][1]:
                    print('Cannot add video to', playlist_name, ': Video already added')
                else:
                    lines[i][0] = str(names[i])
                    file = open("playlists.txt", "r+")
                    for j in range(0, len(lines)):
                        if j == play_index:
                            if len(lines[j][1]) == 0:
                                line = str(lines[j][0] + "|" + video_id)
                            else:
                                lines[j][1].strip('\n')
                                line = str(lines[j][0] + "|" + lines[j][1] + ',' + video_id)
                        else:
                            line = (lines[j][0] + "|" + lines[j][1])
                        file.write(line)
                    video = self._video_library.get_video(video_id)
                    print('Added video to', playlist_name, ':', video.title)
        file.close()


    def show_all_playlists(self):
        """Display all playlists."""
        playlists = self._video_library.get_all_playlists()
        names = []
        if len(playlists) == 0:
            print('No playlists exist yet')
        else:
            for i in range(0, len(playlists)):
                names.append(playlists[i].play_title)
            print('Showing all playlists:')
            names.sort()
            for name in names:
                print(name)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        file = open("playlists.txt", "r")
        file.seek(0)
        data = file.readlines()
        lines = []
        for line in data:
            line = line.split('|')
            lines.append(line)
        names= []

        for i in range (0, len(lines)):
            names.append(lines[i][0])
            if playlist_name.upper() == lines[i][0].upper():
                play_index = i
        if playlist_name.upper() not in (name.upper() for name in names):
            print('Cannot show playlist', playlist_name + ': Playlist does not exist')
        else:
            print('Showing playlist:', names[play_index])
            if len(lines[play_index][1]) == 0:
                print('No videos here yet')
            else:
                items = lines[play_index][1].split(',')
                for item in items:
                    if items is None:
                        print('No videos here yet')
                    else:
                        video = self._video_library.get_video(item)
                        tags = []
                        if tags is not None:
                            for tag in video.tags:
                                tags.append(str(tag))
                        print((str(video.title) + ' (' + str(video.video_id) + str(') [') +str(' '.join(tags))  + str(']')))
        file.close()

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        file = open("playlists.txt", "r")
        file.seek(0)
        data = file.readlines()
        lines = []
        for line in data:
            line = line.split('|')
            lines.append(line)
        names= []
        for i in range (0, len(lines)):
            names.append(lines[i][0])
        playlist = self._video_library.get_playlist(playlist_name)
        if playlist_name.upper() not in (name.upper() for name in names):
            print('Cannot remove video from', playlist_name + ': Playlist does not exist')
        elif self._video_library.get_video(video_id) == None:
            print('Cannot remove video from:', playlist_name + ': Video does not exist')

        else:
            for name in range (0, len(names)):
                if names[name].upper() == playlist_name.upper():
                    play_index = name
            if video_id not in lines[play_index][1]:
                print('Cannot remove video from', playlist_name, ': Video is not in playlist')
            else:
                lines[i][0] = str(names[i])
                file = open("playlists.txt", "w")
                for j in range(0, len(lines)):
                    if j == play_index:
                        lines[j][1].strip('\n')
                        items = lines[j][1].split(',')
                        videos = []
                        for k in range(0, len(items)):
                            if items[k] != video_id:
                                videos.append(items[k])
                        line = str(lines[j][0] + "|" + str(','.join(videos)))
                    else:
                        line = (lines[j][0] + "|" + lines[j][1])
                    file.write(line)
                video = self._video_library.get_video(video_id)
                print('Removed video from', playlist_name, ':', video.title)
        file.close()


    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        file = open("playlists.txt", "r")
        file.seek(0)
        data = file.readlines()
        lines = []
        for line in data:
            line = line.split('|')
            lines.append(line)
        names= []
        for i in range (0, len(lines)):
            names.append(lines[i][0])
        playlist = self._video_library.get_playlist(playlist_name)
        if playlist_name.upper() not in (name.upper() for name in names):
            print('Cannot clear playlist', playlist_name + ': Playlist does not exist')
        else:
            for name in range (0, len(names)):
                if names[name].upper() == playlist_name.upper():
                    play_index = name
            else:
                lines[i][0] = str(names[i])
                file = open("playlists.txt", "w")
                for j in range(0, len(lines)):
                    if j == play_index:
                        line = str(lines[j][0] + "|")
                    else:
                        line = (lines[j][0] + "|" + lines[j][1])
                    file.write(line)

                print('Successfully removed all videos from', playlist_name)
        file.close()

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        file = open("playlists.txt", "r")
        file.seek(0)
        data = file.readlines()
        lines = []
        for line in data:
            line = line.split('|')
            lines.append(line)
        names= []
        for i in range (0, len(lines)):
            names.append(lines[i][0])
        playlist = self._video_library.get_playlist(playlist_name)
        if playlist_name.upper() not in (name.upper() for name in names):
            print('Cannot delete playlist', playlist_name + ': Playlist does not exist')
        else:
            for name in range (0, len(names)):
                if names[name].upper() == playlist_name.upper():
                    play_index = name
            else:
                lines[i][0] = str(names[i])
                file = open("playlists.txt", "w")
                for j in range(0, len(lines)):
                    if j != play_index:
                        line = (lines[j][0] + "|" + lines[j][1])
                    file.write(line)

                print('Successfully deleted playlist', playlist_name)
        file.close()

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        videos= self._video_library.get_all_videos()
        found_videos = []
        for video in videos:
            if search_term.upper() in video.title.upper():
                found_videos.append(video.video_id)
        if len(found_videos) == 0:
            print('No search results for', search_term)
        else:
            found_videos = sorted(found_videos)
            print('Here are the results for', search_term + ':')
            for i in range(0,len(found_videos)):
                video = self._video_library.get_video(found_videos[i])
                tags = []
                if tags is not None:
                    for tag in video.tags:
                        tags.append(str(tag))
                print(str(i + 1) + ')', str(video.title) + ' (' + str(video.video_id) + str(') [') +str(' '.join(tags))  + str(']'))
            print('Would you like to play any of the above? If yes, specify the number of the video.')
            print('If your answer is not a valid number, we will assume it\'s a no.')
            answer = input('')
            try:
                answer = int(answer)
                if (answer - 1) <= len(found_videos):
                    video_id = found_videos[answer - 1]
                    VideoPlayer.play_video(self, video_id)
            except ValueError:
                pass



    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        videos= self._video_library.get_all_videos()
        found_videos = []
        for video in videos:
            if video_tag.upper() in (tag.upper() for tag in video.tags):
                found_videos.append(video.video_id)
        if len(found_videos) == 0:
            print('No search results for', video_tag)
        else:
            found_videos = sorted(found_videos)
            print('Here are the results for', video_tag + ':')
            for i in range(0,len(found_videos)):
                video = self._video_library.get_video(found_videos[i])
                tags = []
                if tags is not None:
                    for tag in video.tags:
                        tags.append(str(tag))
                print(str(i + 1) + ')', str(video.title) + ' (' + str(video.video_id) + str(') [') +str(' '.join(tags))  + str(']'))
            print('Would you like to play any of the above? If yes, specify the number of the video.')
            print('If your answer is not a valid number, we will assume it\'s a no.')
            answer = input('')
            try:
                answer = int(answer)
                if (answer - 1) <= len(found_videos):
                    video_id = found_videos[answer - 1]
                    VideoPlayer.play_video(self, video_id)
            except ValueError:
                pass

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
