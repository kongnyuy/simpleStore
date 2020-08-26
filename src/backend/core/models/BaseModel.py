from peewee import *
from backend.core.persistence.db import Database
#db = SqliteDatabase(':memory:')


class BaseModel(Model):
    class Meta:
        database = Database.get_db_handle()