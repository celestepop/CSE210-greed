from actor import Actor
from point import Point

<<<<<<< HEAD
'''
    File: rock.py
    Author:
    Description:
'''


'''Basically creates a rock as a O in the code, inhertiets from the projectile class'''
class Rock(Projectile):
=======
class Rock(Actor):
>>>>>>> 330e6a1b6aab5917d5a86713f001a711d39d0f67
    def __init__(self):
        super().__init__("O")
        self.set_acceleration(Point(0, -1))
        
