from .BaseModel import BaseModel
import json

class Category(BaseModel):
    class Meta:
        table_name = "Categories"

    def __init__(self, label: str, description: str = "Item category"):
        #self.id = -1
        self.label = label
        self.description = str(f"{description} -> {self.label}")

    @property
    def label(self):
        return self.label

    @property
    def description(self):
        return self.description

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)



class Kind(Category):
    pass