import os
import warnings
from typing import Literal
from configparser import ConfigParser, RawConfigParser

class Config:
    def __init__(self, filename, parser:Literal['config','rawconfig']='config', warning = False):
        self.filename = filename
        self.parser = parser
        self.warning = warning
        if parser == 'config':
            self.config = ConfigParser()
        elif parser == 'rawconfig':
            self.config = RawConfigParser()
    
    def _read_process(self, filepath):
        if os.path.isfile(filepath):
            self.config.read(filepath)
            return self.config
        else:
            if self.warning:
                curr_path = os.getcwd()
                rela_path = os.path.relpath(filepath, curr_path)
                warnings.warn( f":::No file in './{rela_path}/':::")
            return None    

    def read_projdir(self, folder):
        """+ folder : project/<folder>/"""
        filepath = os.path.join(os.getcwd(), folder, self.filename)
        return self._read_process(filepath)

    def read_filedir(self, file):
        """+ file : __file__"""
        filepath = os.path.join(os.path.dirname(file), self.filename)
        return self._read_process(filepath)

        # if os.path.isfile(filepath):
        #     self.config.read(filepath)
        #     return self.config
        # else:
        #     return None        
        
    def read_libdir(self, filename='default.ini'):
        """+ filename : default fallback file"""
        filepath = os.path.join(os.path.dirname(__file__), filename)
        return self._read_process(filepath)
        # if os.path.isfile(filepath):
        #     self.config.read(filepath)
        #     return self.config
        # else:
        #     return None 
           
    def is_section(self, section):
        if section not in self.config.sections():
            return None
        else :
            return section