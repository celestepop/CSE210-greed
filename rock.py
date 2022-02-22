from projectile import Projectile

'''
    File: rock.py
    Author:
    Description:
'''


'''Basically creates a rock as a O in the code, inhertiets from the projectile class'''
class Rock(Projectile):
    def __init__(self):
        super().__init__("O")
        
