from youtubeenhanced.utils.youtube_api import YoutubeAPI
from googleapiclient.http import MediaFileUpload
from datetime import datetime


class YoutubeUploader:
    """
    Class to simplify and encapsulate functionality related to uploading
    videos to Youtube.
    """

    @staticmethod
    def upload_video_to_youtube(
        filename: str,
        name = 'name',
        description = 'description',
        tags = [],
        # TODO: Configure categories as Enums
        category_id = '27'
    ):
        """
        Uploads the provided filename video in our system to the connected Youtube 
        Channel.

        This need the channel to be connected and to have an available token that is
        stored in the 'token files' folder. Read the readme for more information.
        """
        # Set this as False to avoid uploading it to to Youtube
        do_upload = False

        media_file = MediaFileUpload(filename)
        upload_time = (datetime.datetime.now() + datetime.timedelta(days = 10)).isoformat() + '.000Z'
        request_body = {
            'snippet': {
                'title': name,
                'description': description,
                'categoryId': category_id,
                'tags': tags
            },
            'status': {
                'privacyStatus': 'private',
                'publishedAt': upload_time,
                'selfDeclaredMadeForKids': False
            },
            'notifySubscribers': False
        }

        if do_upload:
            service = YoutubeAPI.create_youtube_service()
            response_video_upload = service.videos().insert(
                part = 'snippet,status',
                body = request_body,
                media_body = media_file
            ).execute()
            print(response_video_upload)
            uploaded_video_id = response_video_upload.get('id')
            print(uploaded_video_id)
            print('Video ' + name + ' uploaded to your Youtube Channel.')
        else:
            print('Fake uploaded')