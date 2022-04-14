from enum import Enum


class MTAType(Enum):
    ANIME = 1  # 动漫
    MOVIE = 2  # 电影
    DRAMA = 3  # 电视剧
    RECORD = 4  # 纪录片
    OTHER = 5  # 其他


class MTATag(Enum):
    DRAMA = 1  # 剧情
    COMEDY = 2  # 喜剧
    ACTION = 3  # 动作
    LOVE = 4  # 爱情
    SCIENCE = 5  # 科幻
    HOMO = 6  # 同性
    MUSIC = 7  # 音乐
    CHORUS = 8  # 歌舞
    BIOGRAPHY = 9  # 传记
    HISTORY = 10  # 历史
    WAR = 11  # 战争
    SWORDSMEN = 12  # 武侠
    DISASTER = 13  # 灾难
    ADVENTRUE = 14  # 冒险
    FANCY = 15  # 奇幻
    WEST = 16  # 西部
    SUSPENCE = 17  # 悬疑
    HORROR = 18  # 恐怖
    CRIME = 19  # 犯罪
    CARTOON = 20  # 动画
    THRILLER = 21  # 惊悚
    SEX = 22  # 情色
    OTHER = 23  # 其他


class MTAArea(Enum):
    China = 1  # 中国大陆
    America = 2  # 美国
    Hongkong = 3  # 香港
    Taiwan = 4  # 台湾
    Japan = 5  # 日本
    Korea = 6  # 韩国
    Britain = 7  # 英国
    France = 8  # 法国
    Spain = 9  # 西班牙
    Italy = 10  # 意大利
    Thailand = 11  # 泰国
    Russia = 12  # 俄罗斯
    Germany = 13  # 德国
    India = 14  # 印度
    Other = 15  # 其他


class MTAQuality(Enum):
    UHD8K = 1  # 8K
    UHD = 2  # 4K
    QHD = 3  # 2K
    FHD = 4  # 1080P
    HD = 5  # 720P
    LOWER = 6  # 更低


class MTAData:

    def __init__(self, name: str, name_chn: str, type: MTAType,
                 tag: list[MTATag], area: MTAArea, year: str,
                 quality: MTAQuality, path: str, save_time: int):
        self.name = name
        self.name_chn = name_chn
        self.type = type
        self.tag = tag
        self.area = area
        self.year = year
        self.quality = quality
        self.path = path
        self.save_time = save_time

    def to_str(self):
        tag_value = list(map(lambda e: e.value, self.tag))
        args = [
            self.name, self.name_chn, self.type.value, tag_value,
            self.area.value, self.year, self.quality.value, self.path,
            self.save_time
        ]
        split = chr(30)
        return split.join(map(str, args))

    def __str__(self) -> str:
        return f'name: {self.name}, name_chn: {self.name_chn}, type: {self.type}, tag: {self.tag}, area: {self.area}, year: {self.year}, quality: {self.quality}, path: {self.path}, save_time: {self.save_time}'

    def to_show(self) -> str:
        if self.name == self.name_chn:
            return f'{self.name} ({self.year})'
        else:
            return f'{self.name} {self.name_chn} ({self.year})'