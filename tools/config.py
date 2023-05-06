import os
from configparser import ConfigParser, RawConfigParser

class Config:
    """
    >>> # pip install -e Qlogger
    # project
    #├── project.
    #└── config 
    #   └── log.ini* 
    [section]
    level   = DEBUG
    fmt     = <string format>
    datefmt = <date format>
    """
    # ------------------------------------------------------------------------ #
    config_default = 'config.ini'
    config_project = 'log.ini'
    # ------------------------------------------------------------------------ #
    @classmethod
    def set_config_project(cls, ini_path):
        # print(os.path.dirname(__file__))
        # print(os.getcwd())
        # print(__name__)
        """
        in project __init__.py file        """
        cls.config_project = ini_path

    @classmethod
    def get_config_default(cls):
        ini_dir = os.path.dirname(__file__)
        ini_path = os.path.join(ini_dir, cls.config_default)
        return ini_path

    @classmethod
    def get_config_path (cls):
        path_config_project = os.path.join(os.getcwd(),"config",cls.config_project)

        if os.path.isfile(path_config_project):
            path_config = path_config_project
        else:
            path_config = cls.get_config_default()

        return path_config

    @classmethod
    def get_config_parser(cls, parser="default"):
        ini_path = cls.get_config_path()
        if parser =="default":
            ini_conf = ConfigParser()
        elif parser == "raw":
            ini_conf = RawConfigParser()
        ini_conf.read(ini_path)
        return ini_conf
