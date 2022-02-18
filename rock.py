from projectile import Projectile

class Rock(Projectile):
    def __init__(self, text):
        super().__init__(text)
        

test = Rock("O")

print(test.get_text())