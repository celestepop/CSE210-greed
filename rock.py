from actor import Actor

class Rock(Actor):
    def __init__(self):
        super().__init__("O")
        self._acceleration = -1
        
