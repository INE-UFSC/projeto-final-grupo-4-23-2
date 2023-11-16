from GameObject import GameObject
from abc import ABC, abstractmethod

class ActionDecorator(GameObject, ABC):
    def __init__(self, game_object):
        super().__init__(game_object.position, game_object.block)
        self.__game_object = game_object
        self.__interaction =  None


    @property
    def game_object(self):
        return self.__game_object
    
    @property
    def interaction(self):
        return self.__interaction

    @abstractmethod
    def handle_on_collision(self):
        pass

    def trigger_action(self, interation):
        self.interaction = interation
