from point import Point
from keyboard_service import KeyboardService
from video_service import VideoService
from actor import Actor

''' 
    File: player.py
    Author:
    Description:
'''

# Inherit projectile class?
class Player(Actor):
    '''
        Keep track of the player's movement's and points
    '''
    def __init__(self):
        super().__init__()
        self._score = 0

    def score(self):
        pass

    def get_position(self):
        pass

    def set_position(self):
        pass