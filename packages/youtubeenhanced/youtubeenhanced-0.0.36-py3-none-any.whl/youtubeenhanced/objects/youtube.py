# TODO: I think this file doesn't have to control repeated ids. Review this!
from youtubeenhanced.utils.youtube_api import YoutubeAPI
from youtubeenhanced.objects.youtube_video import YoutubeVideo
from youtubeenhanced.enums import Quality, Language
from yta_general_utils.programming.output import Output
from yta_general_utils.file.enums import FileTypeX
from yta_general_utils.file.reader import FileReader
from yta_general_utils.dataclasses import FileReturn
from random import randint
from typing import Union

import requests


# Very interesting: https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#download-options

class Youtube:
    """
    An object to interact with Youtube platform. This object integrates Youtube
    Data v3 API connection and other libraries to let you do everything with
    Youtube platform.

    [ ? ] If Youtube Data V3 API is not working, you can use this: https://yt.lemnoslife.com/noKey/YOUR_REQUEST
    [ ? ] Here you can check parameters: https://developers.google.com/youtube/v3/docs/search/list?hl=es-419#usage
    """
    __instance = None

    def __new__(cls, ignore_repeated = True):
        if not Youtube.__instance:
            Youtube.__instance = object.__new__(cls)
        
        return Youtube.__instance

    def __init__(self, ignore_repeated = True):
        if not hasattr(self, 'ignore_ids'):
            if not YoutubeAPI.is_youtube_token_valid():
                print('Youtube token is not valid. Please, login to get a new valid token.')
                YoutubeAPI.start_youtube_auth_flow()

            self.service = YoutubeAPI.create_youtube_service()
            # This is to avoid using the same video again in the whole video. This can be
            # modified to avoid repeated videos only in each segment
            self.ignore_ids = []
            self.ignore_repeated = ignore_repeated

    def activate_ignore_repeated(self):
        self.ignore_repeated = True

    def deactivate_ignore_repeated(self):
        self.ignore_repeated = False

    def add_ignored_id(self, ignore_id):
        # TODO: Maybe do any more check?
        if ignore_id not in self.ignore_ids:
            self.ignore_ids.append(ignore_id)

    def search(
        self,
        query: str,
        max_results: int = 25,
        channel_id: str = None
    ):
        """
        Searchs the videos according to 'query'
        keywords and returns an array with the
        results (empty if no results)
        """
        try:
            response_videos_list = self.service.search().list(
                part = 'snippet',
                channelId = channel_id,
                maxResults = max_results,
                order = 'relevance',  # This is the most interesting by far, using the youtube search engine
                type = 'video',
                q = query
            ).execute()
        except Exception as e:
            print(e)
            # We try the collaborative known alternative that should work
            params = f'part=snippet&channelId={channel_id}&maxResults={str(max_results)}&order=relevance&type=video&q={query}&alt=json'
            no_key_url = f'https://yt.lemnoslife.com/noKey/search?{params}'

            try:
                response_videos_list = requests.get(no_key_url).json()
            except Exception as e:
                print(e)
                return []

        if response_videos_list['pageInfo']['totalResults'] == 0:
            return []
        
        return response_videos_list['items']
    
    def get_video(
        self,
        query: str,
        channel_id: str,
        do_choose_randomly: bool = False
    ) -> YoutubeVideo:
        """
        Makes a search and returns the first or a random YoutubeVideo object with that
        found video.
        """
        youtube_videos = self.search(query, 25, channel_id)

        if len(youtube_videos) == 0:
            return None
        
        if self.ignore_repeated and len(self.ignore_ids) > 0:
            index = 0
            while index < len(youtube_videos):
                video = youtube_videos[index]
                if video['id']['videoId'] in self.ignore_ids:
                    del youtube_videos[index]
                    index -= 1
                index += 1

        if len(youtube_videos) == 0:
            return None
        
        url = 'https://www.youtube.com/watch?v=' + youtube_videos[randint(0, len(youtube_videos) - 1)]['id']['videoId']
        if do_choose_randomly:
            url = 'https://www.youtube.com/watch?v=' + youtube_videos[0]['id']['videoId']

        return YoutubeVideo(url)

    def download_video(
        self,
        query: str,
        channel_id: str,
        do_choose_randomly: bool = False,
        do_include_audio: bool = False,
        output_filename: Union[str, None] = None
    ) -> Union[None, FileReturn]:
        """
        Looks for the videos matching provided 'query' of the 'channel_id' and selects and
        downloads the first one (the most relevant according to query) or a random (if 
        'do_choose_randomly' is True).

        This method forces the download to FULL HD quality (1920x1080).

        This method returns the locally stored 'output_filename' (that could change due to video
        extension), or None if something went wrong.
        """
        youtube_video = self.get_video(query, channel_id, do_choose_randomly)

        if not youtube_video:
            return None
        
        output_filename = Output.get_filename(output_filename, FileTypeX.VIDEO)

        output_filename = youtube_video.download(Quality.FULL_HD, output_filename)
        if do_include_audio:
            output_filename = youtube_video.download_with_audio(Quality.FULL_HD, Language.DEFAULT, output_filename)

        if self.ignore_repeated:
            self.add_ignored_id(youtube_video.id)

        return FileReturn(
            FileReader.parse_filename(output_filename),
            FileTypeX.VIDEO,
            output_filename
        )
    
    def download_audio(
        self,
        query: str,
        channel_id: str,
        do_choose_randomly: bool = False,
        output_filename: Union[str, None] = None
    ) -> Union[None, FileReturn]:
        """
        Looks for the videos matching provided 'query' of the 'channel_id' and selects and
        downloads the first one (the most relevant according to query) or a random (if 
        'choose_random' is True).

        This method forces the download to DEFAULT LANGUAGE (the first one in the list).

        This method returns the locally stored 'output_filename' (that could change due to video
        extension), or None if something went wrong.
        """
        youtube_video = self.get_video(query, channel_id, do_choose_randomly)

        if not youtube_video:
            return None
        
        if self.ignore_repeated:
            self.add_ignored_id(youtube_video.id)

        output_filename = Output.get_filename(output_filename, FileTypeX.AUDIO)

        return youtube_video.download_audio(Language.DEFAULT, output_filename)