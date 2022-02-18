from projectile import Projectile

class Gem(Projectile):
    def __init__(self, text):
        super().__init__(text)

test = Gem('*')

print(test.get_text())