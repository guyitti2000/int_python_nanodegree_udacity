class MagicShoppingCart:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return sum(self.items.values())

    def __str__(self):
        return f"MagicShoppingCart({self.items})"

    def __contains__(self, item):
        return item in self.items
    # good to define the dunder magic methods first:w
