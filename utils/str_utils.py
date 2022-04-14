from data.MTA_data import *
import ast
import time


class StrUtils:

    @staticmethod
    def MTA_list_to_show_list(mta_list: list[MTAData]) -> list[str]:
        return [mta.to_show() for mta in mta_list]

    @staticmethod
    def get_MTA_info(mta: MTAData) -> str:
        type_dict = {
            MTAType.ANIME: '动漫',
            MTAType.MOVIE: '电影',
            MTAType.DRAMA: '电视剧',
            MTAType.RECORD: '纪录片',
            MTAType.OTHER: '其他'
        }
        tag_dict = {
            MTATag.DRAMA: '剧情',
            MTATag.COMEDY: '喜剧',
            MTATag.ACTION: '动作',
            MTATag.LOVE: '爱情',
            MTATag.SCIENCE: '科幻',
            MTATag.HOMO: '同性',
            MTATag.MUSIC: '音乐',
            MTATag.CHORUS: '歌舞',
            MTATag.BIOGRAPHY: '传记',
            MTATag.HISTORY: '历史',
            MTATag.WAR: '战争',
            MTATag.SWORDSMEN: '武侠',
            MTATag.DISASTER: '灾难',
            MTATag.ADVENTRUE: '冒险',
            MTATag.FANCY: '奇幻',
            MTATag.WEST: '西部',
            MTATag.SUSPENCE: '悬疑',
            MTATag.HORROR: '恐怖',
            MTATag.CRIME: '犯罪',
            MTATag.CARTOON: '动画',
            MTATag.THRILLER: '惊悚',
            MTATag.SEX: '情色',
            MTATag.OTHER: '其他'
        }
        area_dict = {
            MTAArea.China: '中国大陆',
            MTAArea.America: '美国',
            MTAArea.Hongkong: '香港',
            MTAArea.Taiwan: '台湾',
            MTAArea.Japan: '日本',
            MTAArea.Korea: '韩国',
            MTAArea.Britain: '英国',
            MTAArea.France: '法国',
            MTAArea.Spain: '西班牙',
            MTAArea.Italy: '意大利',
            MTAArea.Thailand: '泰国',
            MTAArea.Russia: '俄罗斯',
            MTAArea.Germany: '德国',
            MTAArea.India: '印度',
            MTAArea.Other: '其他'
        }
        quality_dict = {
            MTAQuality.UHD8K: '8K',
            MTAQuality.UHD: '4K',
            MTAQuality.QHD: '2K',
            MTAQuality.FHD: '1080P',
            MTAQuality.HD: '720P',
            MTAQuality.LOWER: '更低'
        }
        type_show = type_dict.get(mta.type)
        tags = list(map(lambda t: tag_dict.get(t), mta.tag))
        tag_show = '/'.join(tags)
        area_show = area_dict.get(mta.area)
        quality_show = quality_dict.get(mta.quality)
        save_time_show = StrUtils.timestamp_to_localtime(mta.save_time)
        return f'片名: {mta.name}\n\
中文片名: {mta.name_chn}\n\
类型: {type_show}\n\
标签: {tag_show}\n\
地区: {area_show}\n\
年份: {mta.year}\n\
清晰度: {quality_show}\n\
路径: {mta.path}\n\
保存时间: {save_time_show}'

    @staticmethod
    def str_to_MTA_data(line: str) -> MTAData:
        args = line.split(chr(30))
        args[2] = MTAType(int(args[2]))
        args[3] = list(map(lambda i: MTATag(i), ast.literal_eval(args[3])))
        args[4] = MTAArea(int(args[4]))
        args[6] = MTAQuality(int(args[6]))
        args[8] = int(args[8])
        return MTAData(*args)

    @staticmethod
    def timestamp_to_localtime(stamp: int) -> str:
        time_local = time.localtime(stamp)
        #转换成新的时间格式(2016-05-05 20:28:54)
        return time.strftime("%Y-%m-%d %H:%M:%S", time_local)
