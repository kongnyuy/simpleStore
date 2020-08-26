from peewee import *

from backend.core.models.Category import Category, Kind
from backend.config import db_name
from .BaseModel import BaseModel

db = SqliteDatabase(db_name)


class IArticle:
    def __init__(self, name:str, cost: int, model: str, maker: str,quatity: int = 0):
        self.id = -1
        self.name = name
        self.model = model
        self.maker = maker
        self.cost = cost
        self.quantity = quatity



class Article(IArticle, BaseModel):
    id = AutoField()
    name = CharField()
    cost = BigIntegerField
    model = CharField()
    maker = CharField()
    quantity = IntegerField()
    category = ForeignKeyField(Category, backref="articles")
    kind = ForeignKeyField(Kind, backref="kinds")


    class Meta:
        database = db
        table_name = "Articles"

    def __init__(self,
                 name: str,
                 cost: int,
                 model: str,
                 maker: str,
                 quatity: int = 0,
                 category: Category = None,
                 kind: Kind = None,
                 image: str = "article.png"):
        super().__init__(name, cost, model, maker, quatity)
        self.category = category
        self.kind = kind
        self.image = image
