from actor import Actor
from point import Point

<<<<<<< HEAD
'''
    File: gem.py
    Author:
    Description:
'''


'''Basically creates a gem as a * in the code, inhertiets from the projectile class'''
class Gem(Projectile):
    def __init__(self):
        super().__init__('*') 
        
=======
class Gem(Actor):
    def __init__(self):
        super().__init__('*')
        self.set_acceleration(Point(0, -1))
>>>>>>> 330e6a1b6aab5917d5a86713f001a711d39d0f67

test = Gem()

print(test.get_text())