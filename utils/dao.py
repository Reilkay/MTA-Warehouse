import os
from data.MTA_data import MTAArea, MTAData, MTAQuality, MTATag, MTAType
from utils.str_utils import StrUtils


# 单例模式，单次初始化
class Dao:
    _instance = None
    __first_init = False

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        if not self.__first_init:
            self.__first_init = True
            self.__path_name = './.MTA/repo'
            path, _ = os.path.split(self.__path_name)
            if not os.path.exists(path):
                os.makedirs(path)

    def get_MTA_list(self) -> list[MTAData]:
        mlist = []
        with open(self.__path_name, "r", encoding='utf-8') as f:
            for line in f:
                mlist.append(StrUtils.str_to_MTA_data(line))
        return mlist

    def update(self) -> None:
        pass

    def add_MTA_item(self, item: MTAData):
        with open(self.__path_name, "a", encoding='utf-8') as f:
            f.write(item.to_str() + '\n')
