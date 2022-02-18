from actor import Actor

class Gem(Actor):
    def __init__(self):
        super().__init__('*')
        self._acceleration = -1

test = Gem()

print(test.get_text())