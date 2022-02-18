from projectile import Projectile

class Gem(Projectile):
    def __init__(self):
        super().__init__('*')

test = Gem()

print(test.get_text())