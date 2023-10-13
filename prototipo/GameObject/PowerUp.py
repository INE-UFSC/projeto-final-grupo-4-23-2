from GameObject import GameObject
from Player import Player

class PowerUp(GameObject):
    def __init__(self, position: (int, int), block: None,  duration: int, points_life: None, points: None):
         super().__init__(position, block)
         self.__duration = duration
         self.__points_life = points_life #pontos de vida que ele vai ganhar com o power up
         self.__points = points #pontos (score) que ele vai ganhar com o power up
       

    @property
    def duration(self): #### tempo que o powerup vai ficar disponível para que o player consiga pegar
        return self.__duration
    
    @property
    def points_life(self):
        return self.__points_life
    
    @property
    def points(self):
        return self.__points
    
    def handle_on_collision(self):
        return super().handle_on_collision()
    

    def is_life_powerup(self):
        return self.points_life is not None #se o atributo points_life não for vazio, então afeta a vida do jogador e retorna True

    def get_score(self, player):
        if isinstance(player, Player) and player.handle_on_collision():
            if self.duration > 0:
                self.points += self.points
                self.duration -=1
        

    def get_life(self, player):
        if isinstance(player, Player) and player.handle_on_collision():
            if self.duration > 0 :
                self.points_life += self.points_life
                self.duration -=1