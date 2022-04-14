from data.MTA_data import *
import ast


class StrUtils:

    @staticmethod
    def MTA_data_to_name(mta: MTAData) -> str:
        if mta.name == mta.name_chn:
            return mta.name
        else:
            return f'{mta.name}({mta.name_chn})'

    @staticmethod
    def str_to_MTA_data(line: str) -> MTAData:
        args = line.split(chr(30))
        args[2] = MTAType(int(args[2]))
        args[3] = list(map(lambda i: MTATag(i), ast.literal_eval(args[3])))
        args[4] = MTAArea(int(args[4]))
        args[6] = MTAQuality(int(args[6]))
        args[8] = int(args[8])
        return MTAData(*args)
