from GameObject import*

class Player(GameObject):
    def __init__(self, position: (int, int), block: bool, name: str, score: int):
        super().__init__(position, block)
        self.__name = name
        self.__score = score

    @property
    def name(self):
        return self.__name
    
    @property
    def score(self):
        return self.__score
    
    def handle_on_collision(self):
        return super().handle_on_collision()
        