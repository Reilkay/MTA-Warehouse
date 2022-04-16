import toml
import os


class Config:
    _instance = None
    __first_init = False

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        if not self.__first_init:
            self.__first_init = True
            self.__path_name = './.MTA/config.toml'
            path, _ = os.path.split(self.__path_name)
            if not os.path.exists(path):
                os.makedirs(path)
            if not os.path.isfile(self.__path_name):
                self.init_config_file()
            self.__config = self.get_from_file()

    def get_from_file(self) -> dict:
        config = toml.load(self.__path_name)
        return config

    def update(self, config: dict) -> None:
        with open(self.__path_name, 'w') as f:
            toml.dump(config, f)
        self.__config = self.get_from_file()

    def get(self) -> dict:
        return self.__config

    def get_warehouse(self) -> dict:
        return self.__config['warehouse']

    def init_config_file(self):
        init_data = """
        """
        with open(self.__path, 'w') as f:
            f.write(init_data)