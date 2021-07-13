class House:
    def __init__(self, size, num_bedrooms, num_bathrooms):
        self.size = size
        self.beds = num_bedrooms
        self.baths = num_bathrooms

    @classmethod
    def create(cls, description):
        """The description is 'SIZE BEDS BATH'"""
        size, beds, baths = description.split(' ')
        # make a House using these values.
        return cls(float(size), int*(beds), int(baths))

    @staticmethod
    def build_door(width, height):
        return (width, height)


home = House.create("1000 2 2")
print(home.size)
print(home.beds)
