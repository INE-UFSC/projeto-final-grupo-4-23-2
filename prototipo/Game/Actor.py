from GameObject import GameObject

class Actor(GameObject):
    def __init__(self, position: (int, int), block: bool, points: int, duration: int, points_life: None):
        super().__init__(position, block)

        self.__points = points
        self.__duration = duration
        self.__points_life = points_life

    @property
    def points(self):
        return self.__points
    @property
    def duration(self): #### tempo que o powerup vai ficar disponível para que o player consiga pegar
        return self.__duration
    
    @property
    def points_life(self):
        return self.__points_life
    
    def update(self, delta_time):#checar se chegou o momento de remover/excluir o obstaculo/powerup ##delta_time =tempo do ultimo update
        self.duration -= delta_time
        if self.duration < 0:
            pass #remover da tela
            
    
    
    def handle_on_collision(self):
        pass
        