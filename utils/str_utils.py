from typing import Tuple
from data.MTA_data import *
import ast
import time
import os
import re
import functools


class StrUtils:

    # 将MTA列表转换为展示列表
    @staticmethod
    def MTA_list_to_show_list(mta_list: list[MTAData]) -> list[str]:
        return [mta.to_show() for mta in mta_list]

    # 将MTA对象翻译为中文Info
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
        other_msg_show = mta.other_msg if mta.other_msg != 'NoMessage' else '无'
        return f'片名: {mta.name}\n\
中文片名: {mta.name_chn}\n\
类型: {type_show}\n\
标签: {tag_show}\n\
地区: {area_show}\n\
年份: {mta.year}\n\
清晰度: {quality_show}\n\
路径: {mta.path}\n\
保存时间: {save_time_show}\n\
其他信息: {other_msg_show}'

    # 将文本标签转为索引
    @staticmethod
    def str_tag_to_index(tag: str) -> int:
        tag_dict = {
            'tag_drama': 1,
            'tag_comedy': 2,
            'tag_action': 3,
            'tag_love': 4,
            'tag_science': 5,
            'tag_homo': 6,
            'tag_music': 7,
            'tag_chorus': 8,
            'tag_biography': 9,
            'tag_history': 10,
            'tag_war': 11,
            'tag_swordsmen': 12,
            'tag_disaster': 13,
            'tag_adventrue': 14,
            'tag_fancy': 15,
            'tag_west': 16,
            'tag_suspence': 17,
            'tag_horror': 18,
            'tag_crime': 19,
            'tag_cartoon': 20,
            'tag_thriller': 21,
            'tag_sex': 22,
            'tag_other': 23
        }
        return tag_dict.get(tag)

    # 从单行文本中提取MTA元素
    @staticmethod
    def str_to_MTA_data(line: str) -> MTAData:
        args = line.split(chr(30))
        args[2] = MTAType(int(args[2]))
        args[3] = list(map(lambda i: MTATag(i), ast.literal_eval(args[3])))
        args[4] = MTAArea(int(args[4]))
        args[6] = MTAQuality(int(args[6]))
        args[8] = int(args[8])
        return MTAData(*args)

    # 从用户输入中提取MTA元素
    @staticmethod
    def info_to_MTA_data(name: str, name_chn: str, type: int,
                         tag_input: list[Tuple[str, bool]], area: int,
                         year: str, quality: int, path: str, save_time: int,
                         other_msg: str) -> MTAData:
        type = MTAType(type)
        tag_index = [
            StrUtils.str_tag_to_index(t[0]) for t in tag_input if t[1]
        ]
        tag_index.sort()
        tag = list(map(lambda i: MTATag(i), tag_index))
        area = MTAArea(area)
        quality = MTAQuality(quality)
        if other_msg == '':
            other_msg = 'NoMessage'
        return MTAData(name, name_chn, type, tag, area, year, quality, path,
                       save_time, other_msg)

    # 获取当前时间戳
    @staticmethod
    def get_current_timestamp() -> int:
        return int(time.time())

    # 格式化时间转时间戳
    @staticmethod
    def timef_to_timestamp(str_time) -> int:
        timeArray = time.strptime(str_time, "%Y")
        return int(time.mktime(timeArray))

    # 将时间戳转换为当地时间
    @staticmethod
    def timestamp_to_localtime(stamp: int) -> str:
        time_local = time.localtime(stamp)
        #转换成新的时间格式(2016-05-05 20:28:54)
        return time.strftime("%Y-%m-%d %H:%M:%S", time_local)

    # 文件名排序对比函数
    @staticmethod
    def file_name_cmp(file1: str, file2: str):
        # 去除文件路径和文件后缀
        _, file1 = os.path.split(file1)
        _, file2 = os.path.split(file2)
        file1, _ = os.path.splitext(file1)
        file2, _ = os.path.splitext(file2)

        if file1 == file2:
            return 0
        # 试图寻找file1中的分集信息
        file1_nums = re.findall(r'Ep([0-9]+)', file1, re.IGNORECASE)
        if not file1_nums:
            file1_nums = re.findall(r'E([0-9]+)', file1, re.IGNORECASE)
            if not file1_nums:
                file1_nums = re.findall(r'([0-9]+)', file1)
        # 试图寻找file2中的分集信息
        file2_nums = re.findall(r'Ep([0-9]+)', file2, re.IGNORECASE)
        if not file2_nums:
            file2_nums = re.findall(r'E([0-9]+)', file2, re.IGNORECASE)
            if not file2_nums:
                file2_nums = re.findall(r'([0-9]+)', file2)
        # 若文件名中有数字（可能为分集信息的值）
        if file1_nums and file2_nums:
            if file1_nums[-1] < file2_nums[-1]:
                return -1
            elif file1_nums[-1] > file2_nums[-1]:
                return 1
            else:
                return 0
        # 否则按文件名排序
        else:
            if file1 < file2:
                return -1
            else:
                return 1

    # 文件排序函数
    @staticmethod
    def file_name_sorted(file_list: list[str]) -> list[str]:
        return sorted(file_list,
                      key=functools.cmp_to_key(StrUtils.file_name_cmp))

    # 文件名合法校验
    @staticmethod
    def is_file_name_legal(name: str) -> bool:
        name_format = re.compile(r'[\/:*?"<>|]')
        if name_format.findall(name):
            return False
        else:
            return True
