class Category:
    def __init__(self, label: str, description: str = "Item category"):
        self.id = -1
        self.label = label
        self.description = str(f"{description} -> {self.label}")

    @property
    def label(self):
        return self.label

    @property
    def description(self):
        return self.description

