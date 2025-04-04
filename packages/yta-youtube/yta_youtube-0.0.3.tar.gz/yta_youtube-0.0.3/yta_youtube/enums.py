"""
This has been deducted by manually extracting 
different videos information and analyzing it.

Audio formats are written like this:
# -1.0 is dubbed
# 2.0 is low
# 3.0 is medium

Video formats are written like this:
# 5.0 is 240p
# 6.0 is 360p
# 7.0 is 480p
# 8.0 is 720p
# 9.0 is 1080p
"""
from yta_general_utils.programming.enum import YTAEnum as Enum
from yta_general_utils.file.enums import AudioFileExtension, VideoFileExtension


class AudioFormatQuality(Enum):
    """
    The quality possible values in an audio
    format.
    """
    
    DUBBED = -1.0
    """
    An audio that is actually a dub in the
    specific language, so it is a specific
    file uploaded to be included with the
    video, not the original video audio.
    """
    LOW_DRC = 1.5
    """
    Original video audio in low quality and
    with drc.
    """
    LOW = 2.0
    """
    Original video audio but in low quality.
    """
    MEDIUM_DRC = 2.5
    """
    Original video audio in medium quality
    and with drc.
    """
    MEDIUM = 3.0
    """
    Original video audio but in medium
    quality.
    """
    # These ones below are created by me to be
    # able to handle them dynamically
    HIGHEST = 999
    """
    The best available quality, that guarantees that
    one of the existing qualities will be chosen
    dynamically when processing. This is very useful
    when you prioritize the quality.
    """
    LOWEST = 998
    """
    The lowest available quality, that guarantees that
    one of the existing qualities will be choosen
    dynamically when processing. This is very useful 
    when you prioritize the speed.
    """
    # TODO: Is there any other audio quality (?)

    @property
    def as_key(self) -> str:
        """
        The audio format quality as a string that can
        be used to identify an audio format once it's
        been processed by our system.

        The 'HIGHEST' and 'LOWEST' items cannot be
        transformed into a string because they have
        been created for dynamic quality choosing.
        """
        if self in AudioFormatQuality.special_values():
            # TODO: Make this exception message dynamic
            raise Exception('The HIGHEST and LOWEST qualities cannot use the "as_key" property.')

        return {
            AudioFormatQuality.DUBBED: 'dubbed',
            AudioFormatQuality.LOW_DRC: 'low_drc',
            AudioFormatQuality.LOW: 'low',
            AudioFormatQuality.MEDIUM_DRC: 'medium_drc',
            AudioFormatQuality.MEDIUM: 'medium',
        }[self]

    @staticmethod
    def real_values():
        """
        Obtain all the values that are actually extension
        values and not special and dynamic values to be
        processed in a special way.
        """
        return AudioFormatQuality.get_all() - AudioFormatQuality.special_values()
    
    @staticmethod
    def special_values():
        """
        Obtain all the values that are special an dynamic
        to be processed in a special way.
        """
        return [AudioFormatQuality.HIGHEST, AudioFormatQuality.LOWEST]
    
    @staticmethod
    def formats_ordered_by_quality():
        """
        The audio formats but ordered by quality to get 
        dynamically the best quality format that is
        available.

        You can use this keys, in order, to access to
        the first available extension for our audio
        formats that have been processed.
        """
        return [
            AudioFormatQuality.MEDIUM,
            AudioFormatQuality.MEDIUM_DRC,
            AudioFormatQuality.LOW,
            AudioFormatQuality.LOW_DRC,
            AudioFormatQuality.DUBBED
        ]

class VideoFormatQuality(Enum):
    """
    The quality possible values in a video
    format. The values are the ones that
    youtube use to identify those qualities.
    """

    SUPER_LOW_SD = 0.0
    """
    A quality of 144p. Its corresponding 
    string key is '144'.
    """
    LOW_SD = 5.0
    """
    A quality of 240p. Its corresponding 
    string key is '240'.
    """
    SD = 6.0
    """
    A quality of 360p. Its corresponding
    string key is '360'.
    """
    HIGH_SD = 7.0
    """
    A quality of 480p. Its corresponding
    string key is '480'.
    """
    HD = 8.0
    """
    A quality of 720p. Its corresponding
    string key is '720'.
    """
    FULL_HD = 9.0
    """
    A quality of 1080p. Its corresponding
    string key is '1080'.
    """
    QUAD_HD_2K = 10.0
    """
    A quality of 1440p. Its corresponding
    string key is '1440'.
    """
    ULTRA_HD_4K = 11.0
    """
    A quality of 2160p. Its corresponding
    string key is '2160'.
    """
    ULTRA_HD_8K = 12.0
    """
    A quality of 4320p. Its corresponding
    string key is '4320'.

    # TODO: Not sure if it is 12.0
    """
    # These ones below are created by me to be
    # able to handle them dynamically
    HIGHEST = 999
    """
    The best available quality, that guarantees that
    one of the existing qualities will be chosen
    dynamically when processing. This is very useful
    when you prioritize the quality.
    """
    LOWEST = 998
    """
    The lowest available quality, that guarantees that
    one of the existing qualities will be choosen
    dynamically when processing. This is very useful 
    when you prioritize the speed.
    """
    # TODO: Maybe we need to ask for a video that is
    # available in 4k and obtain its quality value

    @property
    def as_key(self) -> str:
        """
        The video format quality as a string that can
        be used to identify a video format once it's
        been processed by our system.

        The 'HIGHEST' and 'LOWEST' items cannot be
        transformed into a string because they have
        been created for dynamic quality choosing.
        """
        if self in AudioFormatQuality.special_values():
            # TODO: Make this exception message dynamic
            raise Exception('The HIGHEST and LOWEST qualities cannot use the "as_key" property.')

        return {
            VideoFormatQuality.SUPER_LOW_SD: '144',
            VideoFormatQuality.LOW_SD: '240',
            VideoFormatQuality.SD: '360',
            VideoFormatQuality.HIGH_SD: '480',
            VideoFormatQuality.HD: '720',
            VideoFormatQuality.FULL_HD: '1080',
            VideoFormatQuality.QUAD_HD_2K: '1440',
            VideoFormatQuality.ULTRA_HD_4K: '2160',
            VideoFormatQuality.ULTRA_HD_8K: '4320'
        }[self]
    
    @staticmethod
    def real_values():
        """
        Obtain all the values that are actually extension
        values and not special and dynamic values to be
        processed in a special way.
        """
        return VideoFormatQuality.get_all() - VideoFormatQuality.special_values()
    
    @staticmethod
    def special_values():
        """
        Obtain all the values that are special an dynamic
        to be processed in a special way.
        """
        return [VideoFormatQuality.HIGHEST, VideoFormatQuality.LOWEST]

    @staticmethod
    def formats_ordered_by_quality():
        """
        The video formats but ordered by quality to get 
        dynamically the best quality format that is
        available.

        You can use this keys, in order, to access to
        the first available extension for our audio
        formats that have been processed.
        """
        return [
            VideoFormatQuality.ULTRA_HD_8K,
            VideoFormatQuality.ULTRA_HD_4K,
            VideoFormatQuality.QUAD_HD_2K,
            VideoFormatQuality.FULL_HD,
            VideoFormatQuality.HD,
            VideoFormatQuality.HIGH_SD,
            VideoFormatQuality.SD,
            VideoFormatQuality.LOW_SD,
            VideoFormatQuality.SUPER_LOW_SD
        ]

class AudioFormatExtension(Enum):
    """
    The extension possible values in an audio
    format.
    """

    WEBM = AudioFileExtension.WEBM.value
    M4A = AudioFileExtension.M4A.value
    # Yes, they use mp4 extension for dubbed audios, so
    # they only get the audio from that file and they 
    # flag it with 'resolution = "audio only"'
    MP4 = VideoFileExtension.MP4.value
    # Especial value to obtain it dynamically 
    HIGHEST = 'best'
    """
    The best available extension, that guarantees that
    one of the existing extensions will be chosen
    dynamically when processing. This is very useful
    when you prioritize the quality.
    """
    LOWEST = 'lowest'
    """
    The lowest available extension, that guarantees that
    one of the existing extensions will be choosen
    dynamically when processing. This is very useful 
    when you prioritize the speed.
    """

    @staticmethod
    def real_values():
        """
        Obtain all the values that are actually extension
        values and not special and dynamic values to be
        processed in a special way.
        """
        return AudioFormatExtension.get_all() - AudioFormatExtension.special_values()
    
    @staticmethod
    def special_values():
        """
        Obtain all the values that are special an dynamic
        to be processed in a special way.
        """
        return [AudioFormatExtension.HIGHEST, AudioFormatExtension.LOWEST]
    
    @staticmethod
    def formats_ordered_by_quality():
        """
        The audio formats but ordered by quality to get 
        dynamically the best quality format that is
        available.

        You can use this keys, in order, to access to
        the first available extension for our audio
        formats that have been processed.
        """
        return [
            AudioFormatExtension.M4A,
            AudioFormatExtension.MP4,
            AudioFormatExtension.WEBM
        ]

class VideoFormatExtension(Enum):
    """
    The extension possible values in a video
    format.
    """

    MP4 = VideoFileExtension.MP4.value
    WEBM = VideoFileExtension.WEBM.value
    # Especial value to obtain it dynamically below
    HIGHEST = 'best'
    """
    The best available extension, that guarantees that
    one of the existing extensions will be chosen
    dynamically when processing. This is very useful
    when you prioritize the quality.
    """
    LOWEST = 'lowest'
    """
    The lowest available extension, that guarantees that
    one of the existing extensions will be choosen
    dynamically when processing. This is very useful 
    when you prioritize the speed.
    """

    @staticmethod
    def real_values():
        """
        Obtain all the values that are actually extension
        values and not special and dynamic values to be
        processed in a special way.
        """
        return VideoFormatExtension.get_all() - VideoFormatExtension.special_values()
    
    @staticmethod
    def special_values():
        """
        Obtain all the values that are special an dynamic
        to be processed in a special way.
        """
        return [VideoFormatExtension.HIGHEST, VideoFormatExtension.LOWEST]
    
    @staticmethod
    def formats_ordered_by_quality():
        """
        The video formats but ordered by quality to get 
        dynamically the best quality format that is
        available.

        You can use this keys, in order, to access to
        the first available extension for our video
        formats that have been processed.
        """
        return [
            VideoFormatExtension.WEBM,
            VideoFormatExtension.MP4
        ]
    
# TODO: When I'm able to inherit one YTAEnum class
# from another, make both VideoFormatExtension and
# AudioFormatExtension inherit from a common class
# that includes the 'real_values' and
# 'special_values' methods to avoid duplicated code
# and also with VideoFormatQuality and
# AudioFormatQuality

    