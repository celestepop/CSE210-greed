from actor import Actor
from point import Point

'''
    File: gem.py
    Author:
    Description:
'''


'''Basically creates a gem as a * in the code, inhertiets from the projectile class'''

class Gem(Actor):
    def __init__(self):
        super().__init__('*')
        self.set_acceleration(Point(0, -1))
