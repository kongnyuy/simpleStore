from .BaseModel import BaseModel
from peewee import *
from backend.core.persistence.db import Database
import json

#class Category(BaseModel):
class Category(Model):
    label =  CharField()
    description = TextField()
    class Meta:
        table_name = "Categories"
        database = Database.get_db_handle()

    def __init__(self, label: str, description: str = "Item category"):
        #self.id = -1
        self.label = label
        self.description = str(f"{description} -> {self.label}")

    # @property
    # def label(self):
    #     return self.label

    # @label.setter
    # def label(self, value):
    #     self._label = value


    # @property
    # def description(self):
    #     return self.description

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)



class Kind(Category):
    pass