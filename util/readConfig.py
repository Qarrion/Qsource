import os
from typing import Literal
from configparser import ConfigParser, RawConfigParser

def read_config(
        filename, 
        parser:Literal['config','rawconfig']='config',
        location:Literal['file','project']='project'):
    """
    filename : <filename.ini>
    location : project -> project/config/
    """
    

    if location =='file':
        basedir = os.path.dirname(__file__)
    elif location =='project':
        basedir = os.path.join(os.getcwd(),'config')

    filepath = os.path.join(basedir, filename)

    if not os.path.isfile(filepath):
        msg = f"No file ({filepath}))"
        cred = '\033[91m'
        cend = '\033[0m'
        print(cred+msg+cend)
        return()
    
    if parser == 'config':
        conf = ConfigParser()
    elif parser == 'rawconfig':
        conf = RawConfigParser()

    conf.read(filepath)
    return conf

if __name__ == "__main__":
    config = read_config('myconfig.ini')
    print(config['test']['var1'])
    print(config.get('test','var1'))