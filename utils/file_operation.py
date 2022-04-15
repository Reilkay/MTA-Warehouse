import os


class FileOperation:

    @staticmethod
    def get_files_from_path(path: str) -> list[str]:
        files_list = []
        for root, _, files in os.walk(path):
            # root 表示当前正在访问的文件夹路径
            # dirs 表示该文件夹下的子目录名list
            # files 表示该文件夹下的文件list
            # 遍历文件
            for f in files:
                files_list.append(os.path.join(root, f))
        return files_list
