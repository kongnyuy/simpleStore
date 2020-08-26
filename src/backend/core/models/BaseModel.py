from peewee import *
db = SqliteDatabase(':memory:')


class BaseModel(Model):
    class Meta:
        database = db