import json
class Article:
    def __init__(self, name:str, maker:str, model:str, cost:int, quantity:int, category:str):
        self.name = name
        self.maker = maker
        self.model = model
        self.cost = cost
        self.quantity = quantity        
        self.category = category
    
    def serialize(self):
        return json.dumps(self.__dict__)

    @classmethod
    def get_instance(cls, d:dict):
        return cls(**d)
