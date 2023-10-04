import os

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class Video:
    """Класс для видео с YouTube"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)


    def __init__(self, video_id: str) -> None:
        """Конструктором класса Video."""
        self.video_id: str = video_id

        try:
            video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                        id=self.video_id
                                                        ).execute()
            if not video_response['items']:
                raise ValueError("Incorrect Video ID")

            self.title: str = video_response['items'][0]['snippet']['title']
            self.view_count: int = video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = video_response['items'][0]['statistics']['likeCount']
            self.comment_count: int = video_response['items'][0]['statistics']['commentCount']

        except (HttpError, ValueError) as e:
            print(f"Error: {e}")
            self.title = None
            self.view_count = None
            self.like_count = None
            self.comment_count = None
        video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                    id=self.video_id
                                                    ).execute()


    def __str__(self):
        """Магический метод (__str__) который выводит название видео"""
        return self.video_title


class PLVideo(Video):
    """Класс для плейлиста с YouTube"""
    def __init__(self, video_id: str, playlist_id: str) -> None:
        """Конструктором класса PLVideo(Video)
        :param playlist_id: id плейлиста
        """
        super().__init__(video_id)
        self.playlist_id: str = playlist_id

