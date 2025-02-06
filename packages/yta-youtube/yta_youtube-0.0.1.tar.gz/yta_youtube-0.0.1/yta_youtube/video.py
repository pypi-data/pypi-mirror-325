"""
This has been built by manually checking the information
that the yt-dlp 'extract_info' method gives you. The
values that are set as null are transformed into None 
when parsed in Python, but there are also 'none' values
that are actually strings no indicate, with that string,
something specific that is, by itself, just a string.
"""
from yta_youtube.regex import RegularExpression
from yta_general_utils.file.checker import FileValidator
from yta_general_utils.temp import Temp
from yta_general_utils.constants import Language as YoutubeLanguage
from yta_general_utils.file.enums import SubtitleFileExtension as YoutubeSubtitleFormat
from yta_general_utils.subtitles.parser import SubtitlesParser
from yta_general_utils.subtitles.dataclasses import Subtitles
from yta_general_utils.downloader import Downloader
from yt_dlp import YoutubeDL
from PIL import Image
from typing import Union

import requests


YDL_CONFIG = {
    #'listformats': True,
    'format': 'bestaudio/best',
    #'outtmpl': '%(title)s.%(ext)s', # You can change the PATH as you want
    #'download_archive': 'downloaded.txt',
    'noplaylist': True,   
    'quiet': True,
    'no_warnings': True,
    # 'postprocessors': [{
    #     'key': 'FFmpegExtractAudio',
    #     'preferredcodec': 'mp3',
    #     'preferredquality': '192',
    # }],
    #'progress_hooks': [hook]
}


class YoutubeVideo:
    """
    Class to represent a Youtube video and all its
    information, simplified to make easier working
    with it. This is a base class that will include
    the basic information that can be extracted from
    the public videos and using the awesome yt-dlp
    library.
    """

    id: str
    """
    The public youtube video id (which comes in its
    url).

    This is one example:
    0BjlBnfHcHM
    """
    _data: dict
    """
    The raw data extracted with yt-dlp library. For
    internal use only.
    """
    _youtubedl: YoutubeDL
    """
    Instance of yt-dlp class to be able to extract
    the information we need. For internal use only.
    """

    @property
    def url(self) -> str:
        """
        A shortcut to 'long_url'.
        """
        return self.long_url
    
    @property
    def long_url(self) -> str:
        """
        The public youtube video url in long format.

        This is one example:
        https://www.youtube.com/watch?v=0BjlBnfHcHM
        """
        return f'https://www.youtube.com/watch?v={self.id}'

    @property
    def short_url(self) -> str:
        """
        The public youtube video url in short format.
        Short youtube video urls are transformed into
        long youtube urls when you navigate into them.

        This is one example:
        youtu.be/0BjlBnfHcHM
        """
        return f'youtu.be/{self.id}'
    
    @property
    def data(self) -> dict:
        """
        The raw data extracted with yt-dlp library. Please,
        use any other property instead of this directly or
        the behaviour could be unexpected.

        We've dedicated a lot of effort on simplifying the
        way to interact with all the youtube videos 
        available information :).
        """
        # TODO: This information expires due to an expiration
        # token so, should we refresh it?
        if self._data is None:
            self._data = self._youtubedl.extract_info(self.url, download = False)

        return self._data
    
    @property
    def thumbnail_url(self) -> str:
        """
        The url of the best quality thumbnail.
        """
        return self.data['thumbnail']
    
    @property
    def thumbnail(self) -> Image.Image:
        """
        The best quality thumbnail parsed as a pillow
        image, ready to work with.

        This method will download the image, so use it
        carefully.

        TODO: Is this the best way to proceed? I mean,
        making that simple the ability to download 
        resources? If so, what about storing its name
        """
        # TODO: Make a method to dynamically get a video
        # filename based on its id to be able to store 
        # its files always with the same name so we can
        # persist them at least temporary
        filename = _get_youtube_video_filename(self.id, 'thumbnail.png')

        if not FileValidator.file_exists(filename):
            filename = Downloader.download_image(self.thumbnail_url, filename).filename

        return Image.open(filename)
    
    @property
    def title(self) -> str:
        """
        The original video title which is in its original
        language.
        """
        return self.data['title']
    
    @property
    def description(self) -> str:
        """
        The original video description which is in its
        original language.
        """
        return self.data['description']
    
    @property
    def channel_id(self) -> str:
        """
        The id of the channel that owns this video.
        """
        return self.data['channel_id']
    
    @property
    def channel_url(self) -> str:
        """
        The url of the channel that owns this video.
        """
        return self.data['channel_url']
    
    @property
    def duration(self) -> int:
        """
        The duration of the video in milliseconds.
        """
        return self.data['duration']
    
    @property
    def number_of_views(self) -> int:
        """
        The amount of views.
        """
        return self.data['view_count']
    
    @property
    def is_age_limited(self) -> bool:
        """
        A flag that indicates if the video has an age
        limitation or not.

        TODO: I'm not sure about this
        """
        # "age_limit": 0,
        return self.data['age_limit'] == 0
    
    @property
    def categories(self) -> list[str]:
        """
        The list of categories includes for this video.

        TODO: Maybe map these categories to Enum (?)
        """
        # "categories": [
        #     "Entertainment"
        # ],
        return self.data['categories']
    
    @property
    def tags(self) -> list[str]:
        """
        The list of taggs included on this video.
        """
        return self.data['tags']
    
    @property
    def is_embeddable(self) -> bool:
        """
        A flag that indicates if the video can be 
        embedded or not.
        """
        # "playable_in_embed": true,
        return self.data['playable_in_embed']
    
    @property
    def number_of_comments(self) -> int:
        """
        The amount of comments.
        """
        return self.data['comment_count']
    
    @property
    def number_of_likes(self) -> int:
        """
        The amount of likes.
        """
        return self.data['like_count']
    
    @property
    def channel_name(self) -> str:
        """
        The name of the channel in which this video has
        been uploaded.
        """
        return self.data['channel']
    
    @property
    def channel_number_of_followers(self) -> int:
        """
        The amount of followers of the channel in which
        this video has been uploaded.
        """
        return self.data['channel_follower_count']
    
    @property
    def is_channel_verified(self) -> bool:
        """
        A flag that indicates if the channel in which 
        this video has been uploaded is verified or not.
        """
        # "channel_is_verified": true,
        return self.data['channel_is_verified']
    
    @property
    def uploader_channel_name(self) -> str:
        """
        The name of the channel who uploaded the video.

        TODO: How does this actually work (?)
        """
        return self.data['uploader']
    
    @property
    def uploader_channel_id(self) -> str:
        """
        The id of the channel who uploaded the video, that
        is a name starting with @.
        """
        return self.data['uploader_id']
    
    @property
    def uploader_channel_url(self) -> str:
        """
        The url to the channel who uploaded the video.
        """
        return self.data['uploader_url']
    
    @property
    def upload_date(self) -> str:
        """
        The date in which the video has been uploaded, in
        a YYYYMMDD string format.
        """
        return self.data['upload_date']
    
    @property
    def upload_timestamp(self) -> int:
        """
        The timestamp in which the video has been uploaded,
        in milliseconds.
        """
        return self.data['timestamp']
    
    @property
    def visibility(self) -> str:
        """
        The visibility (also known as availability) of the
        video, that can be 'public', 'hidden' or 'private'.

        TODO: Does it actually work like that? Can I have a
        'private' value? (maybe if I'm logged in).
        TODO: Turn these values into Enum values.
        """
        return self.data['availability']
    
    @property
    def original_url(self) -> str:
        """
        The original url.

        TODO: What is this actually (?)
        """
        return self.data['original_url']
    
    @property
    def full_title(self) -> str:
        """
        The full title.

        TODO: I don't know the difference between this
        title and the normal one.
        """
        return self.data['fulltitle']
    
    @property
    def duration_string(self) -> str:
        """
        The duration string that is shown in the video
        thumbnail and player.
        """
        return self.data['duration_string']
    
    @property
    def file_size(self) -> int:
        """
        The video file size in bytes.

        TODO: Is it actually in bytes (?)
        """
        # "filesize": 21250979,
        return self.data['filesize']
    
    @property
    def file_size_approx(self) -> int:
        """
        The video file size in bytes but approximated.

        TODO: What is this and what is it for (?)
        """
        return self.data['filesize_approx']
    
    @property
    def number_of_audio_channels(self) -> int:
        """
        The number of audio channels.
        """
        return self.data['audio_channels']
    
    @property
    def quality(self) -> float:
        """
        The quality of the video.

        TODO: I don't know how this is expressed
        """
        # "quality": 3.0,
        return self.data['quality']
    
    @property
    def height(self) -> any:
        """
        The height of the video.

        TODO: I don't know how this is expressed
        """
        # "height": null,
        return self.data['height']
    
    @property
    def height(self) -> any:
        """
        The height of the video.

        TODO: I don't know how this is expressed
        """
        # "width": null,
        return self.data['width']
    
    @property
    def language(self) -> str:
        """
        The original video language in the international
        Google naming.

        TODO: Use a Language enum instead.
        """
        # "language": "en",
        return self.data['language']
    
    @property
    def language_preference(self) -> int:
        """
        The language preference expressed in a number.

        TODO: I need to map these values to obtain the 
        real ones and use enum values instead.
        """
        return self.data['language_preference']

    @property
    def extension(self) -> str:
        """
        The extension of the video.

        TODO: Parse and use enum values.
        """
        # "ext": "webm",
        return self.data['ext']
    
    @property
    def video_codec(self) -> str:
        """
        The video codec.

        TODO: Parse as enum values
        TODO: This can be none, so we need an enum
        represnting that there is no video codec
        TODO: Do we actually need this (?)
        """
        # "vcodec": "none",
        return self.data['vcodec']
    
    @property
    def video_extension(self) -> str:
        """
        The video extension.

        TODO: Parse as enum values
        TODO: This can be none, so we need an enum
        represnting that there is no video extension
        TODO: Do we actually need this (?)
        """
        # "video_ext": "none",
        
        return self.data['video_ext']
    
    @property
    def audio_codec(self) -> str:
        """
        The audio codec.

        TODO: Parse as enum values.
        TODO: This can be none, so we need an enum
        represnting that there is no audio codec
        TODO: Do we actually need this (?)
        """
        # "acodec": "opus",
        return self.data['acodec']
    
    @property
    def audio_extension(self) -> str:
        """
        The audio extension.

        TODO: Parse as enum values.
        TODO: This can be none, so we need an enum
        represnting that there is no audio extension
        TODO: Do we actually need this (?)
        """
        # "audio_ext": "webm",
        return self.data['audio_ext']

    @property
    def container(self) -> str:
        """
        TODO: I have no idea about what this is
        """
        return self.data['container']
    
    @property
    def protocol(self) -> str:
        """
        The protocol used in this video.

        TODO: Do we actually need this (?)
        """
        return self.data['protocol']
    
    @property
    def video_bit_rate(self) -> float:
        """
        The video bit rate.

        TODO: Do we actually need this (?)
        """
        return float(self.data['vbr'])
    
    @property
    def audio_bit_rate(self) -> float:
        """
        The audio bit rate

        TODO: Do we actually need this (?)
        """
        return float(self.data['abr'])
    
    @property
    def aspect_ratio(self) -> any:
        """
        The aspect ratio of the video.

        TODO: How does it work? It can be 'none'
        """
        return self.data['aspect_ratio']

    @property
    def format(self) -> str:
        """
        The format of the video.

        TODO: I don't know what this is for
        """
        return self.data['format']

    # TODO: The most importants here below 
    @property
    def most_viewed_scenes(self) -> Union[list[dict], None]:
        """
        A list with the most viewed scenes and the time
        in which each of them happen.

        This is based on the user views and it is not
        available in all the videos. If it is not 
        availabile, its value is None.

        This array, if available, is ordered from the 
        most viewed to the less viewed scenes.

        "heatmap": [
            {
                "start_time": 0.0,
                "end_time": 13.65,
                "value": 1.0
            },
            {...}
        ]

        TODO: Parse with a @dataclass maybe (?)
        """
        # Apparently, Youtube chooses 100 different most
        # viewed scenes (or at least with long videos), 
        # so each scene lasts: video_duration / 100
        return (
            sorted(self.data['heatmap'], key = lambda scene: scene['value'], reverse = True)
            if self.data['heatmap'] is not None else
            None
        )
    
    @property
    def has_most_viewed_scenes(self) -> bool:
        """
        A flag that indicates if the video has most viewed
        scenes or not.
        """
        return self.most_viewed_scenes is not None
    
    @property
    def chapters(self) -> any:
        """
        I don't know how it works, I need a working example.

        TODO: This can be null, not none
        """
        # "chapters": null,
        return self.data['chapters']
    
    @property
    def has_chapters(self) -> bool:
        """
        A flag that indicates if the video has chapters or
        not.
        """
        return self.data['chapters']

    @property
    def _automatic_subtitles(self) -> Union[dict, None]:
        """
        The automatic subtitles of this video. For internal
        use only.
        """
        return self.data['automatic_captions']
    
    @property
    def has_automatic_subtitles(self) -> bool:
        """
        A flag that indicates if this video has automatic
        subtitles or not.
        """
        return self._automatic_subtitles is not None

    @property
    def automatic_subtitles_languages(self) -> list[str]:
        """
        A list containing all the available automatic 
        subtitles languages. Perfect to choose the desired
        language and download the corresponding automatic
        subtitles.

        TODO: Use Language enum values better

        "ar": [
            {
                "url": "DOWNLOAD_URL_OMITTED",
                "ext": "vtt",
                "protocol": "m3u8_native"
            },
            {
                "ext": "json3",
                "url": "DOWNLOAD_URL_OMITTED",
                "name": "Arabic"
            },
            {...}
        ]
        """
        # TODO: What if no automatic subtitles? Is it None (?)
        # TODO: The option with 'protocol' attribute can be
        # omitted
        return list(self._automatic_subtitles.keys())
    
    @property
    def _subtitles(self) -> Union[dict, None]:
        """
        The subtitles of this video. For internal use only.
        """
        return self.data['subtitles']
    
    @property
    def has_subtitles(self) -> bool:
        """
        A flag that indicates if this video has subtitles
        or not.
        """
        return self._subtitles is not None
    
    @property
    def subtitles_languages(self) -> list[str]:
        """
        A list containing all the available subtitles
        languages. Perfect to choose the desired language
        and download the corresponding subtitles.

        TODO: Use Language enum values better

        "ar": [
            {
                "ext": "json3",
                "url": "DOWNLOAD_URL_OMITTED",
                "name": "Arabic"
            },
            {
                "ext": "srv1",
                "url": "DOWNLOAD_URL_OMITTED",
                "name": "Arabic"
            },
            {...}
        ]
        """
        # TODO: What if no automatic subtitles? Is it None (?)
        return list(self._subtitles.keys())
    
    def get_automatic_subtitles(
        self,
        language: YoutubeLanguage,
        format: YoutubeSubtitleFormat
    ) -> Union[Subtitles, None]:
        """
        Obtain, if available, the automatic subtitles for
        the given 'language' and in the 'format' provided.

        The automatic subtitles are stored always with the
        same format, so if they have been downloaded
        previously they will be returned instantly.
        """
        if not self.has_automatic_subtitles():
            # No automatic subtitles for any language available
            return None
        
        language = YoutubeLanguage.to_enum(language)
        format = YoutubeSubtitleFormat.to_enum(format).value
        
        language = (
            list(self._automatic_subtitles.keys())[0] 
            if language == YoutubeLanguage.DEFAULT else
            language.value
        )

        subtitles_info = next(
            (
                subtitles_type
                for subtitles_type in self._automatic_subtitles.get(language, [])
                if subtitles_type['ext'] == format
            ),
            None
        )

        if subtitles_info is None:
            # No subtitles available for that language and format
            return None
        
        filename = f'automatic_subtitles_{language}.{format}'

        if self._get_file(filename) is None:
            Downloader.download_file(subtitles_info, filename)

        return SubtitlesParser.parse_from_filename(filename)

    def get_subtitles(
        self,
        language: YoutubeLanguage,
        format: YoutubeSubtitleFormat
    ) -> Union[Subtitles, None]:
        """
        Obtain, if available, the subtitles for the given
        'language' and in the 'format' provided.

        The subtitles are stored always with the same 
        format, so if they have been downloaded previously
        they will be returned instantly.
        """
        if not self.has_subtitles():
            # No subtitles for any language available
            return None
        
        language = YoutubeLanguage.to_enum(language)
        format = YoutubeSubtitleFormat.to_enum(format).value
        
        language = (
            list(self._subtitles.keys())[0] 
            if language == YoutubeLanguage.DEFAULT else
            language.value
        )

        subtitles_info = next(
            (
                subtitles_type
                for subtitles_type in self._subtitles.get(language, [])
                if subtitles_type['ext'] == format
            ),
            None
        )

        if subtitles_info is None:
            # No subtitles available for that language and format
            return None
        
        filename = f'subtitles_{language}.{format}'

        if self._get_file(filename) is None:
            Downloader.download_file(subtitles_info, filename)

        return SubtitlesParser.parse_from_filename(filename)


    def __init__(
        self,
        id: str,
    ):
        """
        Initialize a YoutubeVideo instance with the given
        'id' if the given 'id' is a valid id and of an
        available youtube video.
        """
        if not RegularExpression.YOUTUBE_VIDEO_ID.parse(id):
            raise Exception('The provided "id" is not a valid id.')
        
        if not _is_youtube_video_available_from_id(id):
            raise Exception('The provided "id" is not of an available youtube video.')
        
        self.id = id
        # We need to initialize the yt-dlp instance to be able
        # to obtain the information we need
        self._youtubedl = YoutubeDL(YDL_CONFIG)

    @staticmethod
    def init_from_url(url: str) -> 'YoutubeVideo':
        """
        Initialize a YoutubeVideo instance with the given
        youtube video 'url' if valid and from an available
        video.
        """
        id = _get_youtube_video_id_from_url(url)

        if id is None:
            raise Exception('The provided "url" is not a valid youtube video url.')
        
        return YoutubeVideo(id)
    
    def _get_file(self, filename: str) -> Union[str, None]:
        """
        Get the file with the given 'filename' for this
        youtube video if existing, and return its full
        filename or None if it doesn't exist.
        """
        filename = _get_youtube_video_filename(self.id, filename)

        return filename if FileValidator.file_exists(filename) else None



def _get_youtube_video_filename(id: str, filename: str) -> str:
    """
    Get the real filename according to the given
    youtube video 'id' and the desired 'filename'.
    This includes the full path to this file. 
    """
    return Temp.create_custom_filename(f'{id}_{filename}')

def _get_youtube_video_id_from_url(url: str) -> Union[str, None]:
    """
    Extracts the video id from the given video 'url'.

    This is one example of a valid youtube url:
    https://www.youtube.com/watch?v=0BjlBnfHcHM
    """
    if (
        not RegularExpression.YOUTUBE_VIDEO_SHORT_URL.parse(url) and
        not RegularExpression.YOUTUBE_VIDEO_LONG_URL.parse(url)
    ):
        return None

    return RegularExpression.YOUTUBE_VIDEO_ID_PART_IN_URL.get_matching_group(url, 4)

def _is_youtube_video_available_from_id(id: str) -> bool:
    """
    Check if the youtube video with the given 'id' is
    available or not by looking for its thumbnail.
    """
    # This is, apparently, another alternative, and the
    # one that yt-dlp uses for its default 'thumbnail'
    # attribute:
    # https://i.ytimg.com/vi/{id}/mqdefault.jpg
    return requests.get(f'http://img.youtube.com/vi/{id}/mqdefault.jpg').status_code != 404