from Obstacle import Obstacle
from PowerUp import PowerUp
from GameObject import GameObject

class Player(GameObject):
    def __init__(self, position: (int, int), block: bool, name: str, score: int, life:int):
        super().__init__(position, block)
        self.__name = name
        self.__score = score
        self.__life = life

    @property
    def name(self):
        return self.__name
    
    @property
    def score(self):
        return self.__score
    
    @property
    def life(self):
        return self.__life
    
    def handle_on_collision(self):
        return True
    
    def powerup_collision(self, other_object):
        if isinstance(other_object, PowerUp ):
            if other_object.is_life_powerup():
                self.life = other_object.get_life()
            else:
                self.score= other_object.get_score()


    def obstacle_collision(self, other_object):
        if isinstance(other_object, Obstacle):
            if other_object.is_life_obstacle():
                self.life = other_object.remove_life()
            else:
                self.score= other_object.remove_score()
        