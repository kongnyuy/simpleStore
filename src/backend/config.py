import configparser
cfgFile = 'config.ini'
_config = configparser.ConfigParser()

_config.read(cfgFile)
print(_config['APPLICATION']['name'])



def getAppConfig():
    return _config

def get_data_rep():
    return _config['DATABASE']['data_repository']

def db_name():
    return _config['DATABASE']['database_file']



if __name__ == "__main__":
    print(get_data_rep())