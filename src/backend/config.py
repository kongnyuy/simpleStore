import configparser
import os
cfgFile = 'config.ini'
_config = configparser.ConfigParser()

_config.read(cfgFile)
print(_config['APPLICATION']['name'])



def getAppConfig():
    return _config

def get_data_rep():
    return _config['DATABASE']['data_repository']

def db_name():
    db_file = _config['DATABASE']['database_file']
    return os.path.join(get_data_rep(), db_file)

def schema_path():
    sfile = _config['DATABASE']['schema_file']
    return os.path.join(get_data_rep(), sfile)


if __name__ == "__main__":
    print(db_name())