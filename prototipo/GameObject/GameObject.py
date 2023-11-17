from abc import ABC, abstractmethod

class GameObject(ABC):
    def __init__(self, position: (int,int), block: bool):
        self.__position = position
        self.__block = block

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, position):
        self.__position = position

    @property
    def block(self):
        return self.__block
    
    @block.setter
    def block(self, block):
        self.__block = block

    
    @abstractmethod
    def handle_on_collision(self):
        pass

    @abstractmethod
    def update(self): #para atualizar o estado do objeto
        pass
       