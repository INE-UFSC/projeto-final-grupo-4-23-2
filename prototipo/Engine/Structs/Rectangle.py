class Rectangle:
    def __init__(self, top:float, right:float, bottom:float, left:float):
        self.__top = top
        self.__right = right
        self.__bottom = bottom
        self.__left = left

    def get_top(self): return self.__top
    def get_right(self): return self.__right
    def get_bottom(self): return self.__bottom
    def get_left(self): return self.__left
    
    def set_top(self, value:float): self.top = value
    def set_right(self, value:float): self.right = value
    def set_bottom(self, value:float): self.bottom = value
    def set_left(self, value:float): self.left = value