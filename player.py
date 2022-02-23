from point import Point
from keyboard_service import KeyboardService
from video_service import VideoService
from actor import Actor

''' 
    File: player.py
    Author:
    Description:
'''

class Player(Actor):
    '''
        Keep track of the player's movement's and points
    '''
    def __init__(self):
        super().__init__()
        self._score = 0

    def get_score(self):
        return self._score
