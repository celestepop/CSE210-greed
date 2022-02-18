from point import Point
from color import Color

'''
    File: projectile.py
    Author:
    Description:
'''

class Projectile():

    def __init__(self, text):
        self.position = Point(0,0)
        self.velocity = Point(0,0)
        self.color = Color(255,255,255) 
        self.font_size = 20
        self.text = text

    def get_text(self):
        return self.text

    def get_position(self):
        return self.position

    def get_velocity(self):
        return self.velocity
    
    def get_color(self):
        return self.color

    def get_font_size(self):
        return self.font_size