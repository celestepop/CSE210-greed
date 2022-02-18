from actor import Actor
from point import Point

class Rock(Actor):
    def __init__(self):
        super().__init__("O")
        self.set_acceleration(Point(0, -1))
        
