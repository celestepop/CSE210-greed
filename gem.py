from projectile import Projectile

'''
    File: gem.py
    Author:
    Description:
'''


'''Basically creates a gem as a * in the code, inhertiets from the projectile class'''
class Gem(Projectile):
    def __init__(self):
        super().__init__('*') 
        

test = Gem()

print(test.get_text())