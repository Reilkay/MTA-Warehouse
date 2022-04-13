from enum import Enum


class MTAType(Enum):
    ANIME: 1  # 动漫
    MOVIE: 2  # 电影
    DRAMA: 3  # 电视剧
    RECORD: 4  # 纪录片
    OTHER: 5  # 其他


class MTATag(Enum):
    DRAMA: 1  # 剧情
    COMEDY: 2  # 喜剧
    ACTION: 3  # 动作
    LOVE: 4  # 爱情
    SCIENCE: 5  # 科幻
    HOMO: 6  # 同性
    MUSIC: 7  # 音乐
    CHORUS: 8  # 歌舞
    BIOGRAPHY: 9  # 传记
    HISTORY: 10  # 历史
    WAR: 11  # 战争
    SWORDSMEN: 12  # 武侠
    DISASTER: 13  # 灾难
    ADVENTRUE: 14  # 冒险
    FANCY: 15  # 奇幻
    WEST: 16  # 西部
    SUSPENCE: 17  # 悬疑
    HORROR: 18  # 恐怖
    CRIME: 19  # 犯罪
    CARTOON: 20  # 动画
    THRILLER: 21  # 惊悚
    SEX: 22  # 情色
    OTHER: 23  # 其他


class MTAArea(Enum):
    China: 1  # 中国大陆
    America: 2  # 美国
    Hongkong: 3  # 香港
    Taiwan: 4  # 台湾
    Japan: 5  # 日本
    Korea: 6  # 韩国
    Britain: 7  # 英国
    France: 8  # 法国
    Spain: 9  # 西班牙
    Italy: 10  # 意大利
    Thailand: 11  # 泰国
    Russia: 12  # 俄罗斯
    Germany: 13  # 德国
    India: 14  # 印度
    Other: 15  # 其他


class MTAQuality(Enum):
    UHD8K: 1  # 8K
    UHD: 2  # 4K
    QHD: 3  # 2K
    FHD: 4  # 1080P
    HD: 5  # 720P
    LOWER: 6  # 更低


class MTAData:

    def __init__(self, name: str, name_chn: str, type: MTAType,
                 tag: list[MTATag], area: MTAArea, year: str,
                 quality: MTAQuality):
        self.__name = name
        self.__name_chn = name_chn
        self.__type = type
        self.__tag = tag
        self.__area = area
        self.__year = year
        self.__quality = quality

    def __str__(self):
        return f'[{self.__name}{self.__name_chn}{self.__type}{self.__tag}{self.__area}{self.__year}{self.__quality}]'
