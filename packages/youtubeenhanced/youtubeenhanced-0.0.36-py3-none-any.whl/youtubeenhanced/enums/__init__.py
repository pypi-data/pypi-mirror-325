from yta_general_utils.programming.enum import YTAEnum as Enum


class Subtitles(Enum):
    """
    Subtitle types.
    """

    TYPE_JSON3 = 'json3'
    TYPE_SRV1 = 'srv1'
    TYPE_SRV2 = 'srv2'
    TYPE_SRV3 = 'srv3'
    TYPE_TTML = 'ttml'
    TYPE_VTT = 'vtt'

class Language(Enum):

    # TODO: Set all existing languages
    ARABIC = 'ar'
    SPANISH = 'es'
    CHINESE_TRADITIONAL = 'zh-Hant'
    ENGLISH = 'en'
    FRENCH = 'fr'
    GERMAN = 'de'
    HINDI = 'hi'
    JAPANESE = 'ja'
    KOREAN = 'ko'
    PORTUGUESE = 'pt'
    RUSSIAN = 'ru'
    INDONESIAN = 'in'
    TURKISH = 'tr'
    VIETNAMESE = 'vi'
    DEFAULT = 'default'
    """
    This option will use the first option that
    is available on the video.
    """

class Quality(Enum):

    ULTRA_HD = 2160
    QUAD_HD = 1440
    FULL_HD = 1080
    HD = 720
    SD = 480
    LOW = 360
    MINIMUM = 240
    DEFAULT = 1
    """
    This option will use the first option that
    is available on the video (the highest one).
    """