from data.MTA_data import *
import ast


class StrUtils:

    @staticmethod
    def MTA_list_to_show_list(mta_list: list[MTAData]) -> list[str]:
        return [mta.to_show() for mta in mta_list]

    @staticmethod
    def str_to_MTA_data(line: str) -> MTAData:
        args = line.split(chr(30))
        args[2] = MTAType(int(args[2]))
        args[3] = list(map(lambda i: MTATag(i), ast.literal_eval(args[3])))
        args[4] = MTAArea(int(args[4]))
        args[6] = MTAQuality(int(args[6]))
        args[8] = int(args[8])
        return MTAData(*args)
