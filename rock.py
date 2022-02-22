from actor import Actor
from point import Point

'''
    File: rock.py
    Author:
    Description:
'''


'''Basically creates a rock as a O in the code, inhertiets from the projectile class'''
class Rock(Projectile):
    def __init__(self):
        super().__init__('O')

class Rock(Actor):

    def __init__(self):
        super().__init__("O")
        self.set_acceleration(Point(0, -1))
        
