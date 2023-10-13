from GameObject import*

class Wall(GameObject):
    def __init__(self, position: (int, int), block: bool):
        super().__init__(position, block)

    
    def handle_on_collision(self):
        return super().handle_on_collision()
    
    def wall(self):
        pass