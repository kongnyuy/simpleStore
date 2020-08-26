from backend.core.models.Category import Category
from peewee import *

class IArticle:
    def __init__(self, name:str, cost: int, model: str, maker: str,quatity: int = 0):
        self.id = -1
        self.name = name
        self.model = model
        self.maker = maker
        self.cost = cost
        self.quantity = quatity



class Article(IArticle, Model):
    #name = CharField()

    def __init__(self,
                 name: str,
                 cost: int,
                 model: str,
                 maker: str,
                 quatity: int = 0,
                 category: Category = None,
                 sub_category: Category = None,
                 image: str = "article.png"):
        super().__init__(name, cost, model, maker, quatity)
        self.category = category
        self.sub_category = sub_category
        self.image = image
