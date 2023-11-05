from GameObject import GameObject


class Obstacle(GameObject):
    def __init__(self, position: (int, int), block: bool):
        super().__init__(position, block)

    def handle_on_collision(self):
        return super().handle_on_collision()
    
    def remove_score(self):
        pass

    def remove_live(self):
        pass

    def is_life_obstacle(self):
        pass 
