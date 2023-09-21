import math


class Vector3:
    def __init__(self, x:float=0, y:float=0, z:float=0):
        self.__x = x
        self.__y = y
        self.__z = z
        
    def get_x(self): return self.__x
    def get_y(self): return self.__y
    def get_z(self): return self.__z
    
    def set_x(self, val:float): self.__x = val
    def set_y(self, val:float): self.__y = val
    def set_z(self, val:float): self.__z = val
        
    def copy(self): return Vector3(self.__x,self.__y,self.__z)
    
    def add(self, vector):
        self.__x += vector.get_x()
        self.__y += vector.get_y()
        self.__z += vector.get_z()
        return self
    
    def transform_2d(self, value:float, rotation_axis):
        self.__x += value * math.sin(rotation_axis.get_x())
        self.__y += value * math.cos(rotation_axis.get_x())
        self.__z += value * math.sin(rotation_axis.get_x())
        return self
    
    def rotate(self, axis_values):
        
        pass
    
    def get_2d_point_intersection(pair_1:[], pair_2:[]):
        v1 = ((pair_1[0].get_x(),pair_1[0].get_y()),(pair_1[1].get_x(),pair_1[1].get_y()))
        v2 = ((pair_2[0].get_x(),pair_2[0].get_y()),(pair_2[1].get_x(),pair_2[1].get_y()))
        vlst = [v1, v2]
        
        xdiff = (v1[0][0] - v1[1][0], v2[0][0] - v2[1][0])
        ydiff = (v1[0][1] - v1[1][1], v2[0][1] - v2[1][1])

        def det(a, b): return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0: return None  # Linhas não se cruzam

        d = (det(*v1), det(*v2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        
        for i in range(2):
            if x > max(vlst[i][0][0], vlst[i][1][0]) or x < min(vlst[i][0][0], vlst[i][1][0]): return None
            if y > max(vlst[i][0][1], vlst[i][1][1]) or y < min(vlst[i][0][1], vlst[i][1][1]): return None
        
        return Vector3(x, y, 0)  # Retorna as coordenadas do cruzamento