from actor import Actor

class Gem(Actor):
    def __init__(self):
        super().__init__('*')

test = Gem()

print(test.get_text())