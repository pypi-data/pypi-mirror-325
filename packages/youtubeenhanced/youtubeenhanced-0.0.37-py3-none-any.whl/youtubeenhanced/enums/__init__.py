from yta_general_utils.programming.enum import YTAEnum as Enum


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