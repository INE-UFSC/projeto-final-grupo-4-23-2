from abc import ABC, abstractmethod


class GameState(ABC):
    def __init__(self, setstatus,view) -> None:
        self.__view = view
        self.__setstatus = setstatus

    @property
    def setstatus(self):
        return self.__setstatus

    @property
    def view(self):
        return self.__view
    
    @view.setter
    def view(self, view):
        self.__view = view


    @abstractmethod
    def render(self): #desenha a tela
        pass

    @abstractmethod
    def update(self,event): #atualiza os objetos em cada estado
        pass



