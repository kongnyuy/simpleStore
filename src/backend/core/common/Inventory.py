from .Types import *
from .Utils import *

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


    
