class House:

    layout = 'square'

    def __init__(self, size, color='white'):
        self.size = size
        self.color = color
        self.appliances = []

    def paint(self, color):
        self.color = color

    def build_expansion(self, addition):
        self.size += addition

    def install(self, appliance):
        self.appliances.append(appliance)


home_one = House(1000)
vacation_home = House(5000)

home_one.install('oven')
home_one.install('microwave')

# print(House.appliances)  # ['oven', 'microwave']
# print(id(House.appliances))  # 45...1632
# print(id(vacation_home.appliances))  # 45...1632
# print(id(home.appliances))  # => 45...1632
# all same ID, misuse of shared info
# appliances should be made inside of dunder init method to ensure that each time it is called, it will be unique
