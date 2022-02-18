from projectile import Projectile

'''
    File: gem.py
    Author:
    Description:
'''

class Gem(Projectile):
    def __init__(self):
        super().__init__('*')

test = Gem()

print(test.get_text())