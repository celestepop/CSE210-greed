from actor import Actor
from point import Point

class Gem(Actor):
    def __init__(self):
        super().__init__('*')
        self.set_acceleration(Point(0, -1))

test = Gem()

print(test.get_text())