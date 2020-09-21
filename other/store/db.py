import sys
import os
import re
import json
import shutil
import datetime
import time
import pickle

from models.Article import Article

DB_OPEN_FLAG = False
DATA_DIR = os.path.join(os.curdir, "data")
DB_FILE = 'store.db'
file_path = fp = os.path.join(os.curdir, 'data', DB_FILE)
tmp_file = ""
tmp_file_created = False
ROLLBACK_FLAG = False


def createDatabaseFile(name: str = file_path):
    if not os.path.exists(fp):
        with open(fp, 'w') as file:
            pass
        # os.mknod(fp)


def initialize_database():
    pass


def parseLine(line: str = ""):
    if line == "":
        raise Exception()
    if re.match('^(\\d)+|(.)*|(\\w)*$', line):
        p = line.strip().split('|')
        return p


def getData():
    """ read data from the file """
    data = {"cat": []}
    if os.path.exists(file_path):
        if(os.stat(file_path).st_size == 0):
            # raise Exception("Empty file")
            print("Database file is empty")
            return {}
        l = {}
        with open(file_path, 'r') as file:
            DB_OPEN_FLAG = True
            try:
                l = parseLine(file.readlines())  # [count, article, category]
            except Exception as ex:
                print("File data structure miss matched", file=sys.stderr)
                return
            data[str.lower(l[3])].append(
                Article.get_instance(json.loads(l[1])))
    return data


def update_data(data: dict = {}):
    if len(data.keys == 0):
        return
    with open(file_path, 'w') as fp:
        fp.write(json.dumps(data))  # json structure


def read_data():
    if(os.stat(file_path).st_size > 0):
        with open(file_path, 'rb') as fp:
            #d = json.loads(fp.read())            
            #return d
            print("<>>>>>>> am always here")
            obj = pickle.load(fp)
            print(obj)
            return obj
    createDatabaseFile()
    return {}

def on_start():
    createDatabaseFile()
    create_temp_db()
    # return getData()
    d =  read_data()
    print("...................")
    print(type(d))
    print(d)
    return d


def on_end(data:dict = {}):
    # gracefully shutdown
    global ROLLBACK_FLAG
    #ROLLBACK_FLAG = True
    if os.path.exists(tmp_file):
        if ROLLBACK_FLAG:
            os.remove(file_path)
            shutil.copy2(tmp_file, file_path)
            os.remove(tmp_file)
        else:
            os.remove(tmp_file)
    persistData(data)


def writeStructure(art: Article):
    pass

def persistData(data:dict = {}):
    #ser = json.dumps(data)
    #ser = pickle.dumps(data)
    #data crush/replace
    with open(file_path, 'wb') as fp:
        #fp.write(ser)
        pickle.dump(data, fp, pickle.HIGHEST_PROTOCOL)

        

    


def create_temp_db():
    """replicate db file """
    tmp_file = os.path.join(
        DATA_DIR, f".store.db.bak.{time.strftime('%Y%m%d%H%M%S')}")
    shutil.copy2(file_path, tmp_file)
    global tmp_file_created
    tmp_file_created = True
