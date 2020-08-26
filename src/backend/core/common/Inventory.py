from .Types import *
from .Utils import *
from ..models.Category import Category

class Inventory:
    all_articles = dict()
    aggregate = dict()


    def get_category(self, cat: ITEM_TYPES):
        if not is_dict_empty(self.all_articles):
            bowl = self.all_articles[cat]
            return bowl
        return []

    def injest_inventory_from_file(file_path: str):
        with open(file_path, 'r')  as supplied_items:
            for line in supplied_items.readlines():
                #db injest
                pass

    def populate_categories_from_file(file_path:str):
        with open(file_path, 'r') as supplied_items:
            for idx, line in enumerate(supplied_items.readlines(), start=1):
                #db injest
                if idx == 1: continue
                c = str(line).split(',')
                cat = Category(label = c[0], description= c[1])
                cat.save() #save category to db
