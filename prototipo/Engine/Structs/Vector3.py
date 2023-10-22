import math
import time


tn = [0,0,0]
tc = tn.copy()

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
    
    def sub(self, vector):
        self.__x -= vector.get_x()
        self.__y -= vector.get_y()
        self.__z -= vector.get_z()
        return self
    
    def transform_2d(self, value:float, rotation_axis):
        self.__x += value * math.sin(rotation_axis.get_x())
        self.__y += value * math.cos(rotation_axis.get_x())
        return self
    
    def rotate_2d(self, rotation_axis):
        hip = math.sqrt(self.get_x()**2 + self.get_y()**2)
        self.__x += hip*math.cos(rotation_axis.get_x())
        self.__y += math.sin(rotation_axis.get_x())
        return self
    
    def translate_2d(self, ref_pos, rotation_axis):
        hip = math.sqrt(self.get_x()**2 + self.get_y()**2)
        self.__x += hip*math.cos(rotation_axis.get_x())
        self.__y += math.sin(rotation_axis.get_x())
        return self
    
    def det(a, b): 
        return a[0] * b[1] - a[1] * b[0]
    
    def det_kernel():
        return """
            __kernel void det(__global const float *a_g, __global const float *b_g, __global float *res_g)
            {
                int gid = get_global_id(0);
                res_g = a_g[0] * b_g[1] - a_g[1] * b_g[0];
            }
        """
    
    def is_inside(self, edges):
        count = 0
        for e in edges:
            (x1, y1) = (e[0].get_x(), e[0].get_y())
            (x2, y2) = (e[1].get_x(), e[1].get_y())
            if (self.__y < y1) != (self.__y < y2) and self.__x < x1 + ((self.__y-y1)/(y2-y1))*(x2-x1):
                count += 1
        
        return count%2==1
    
    def get_2d_point_intersection(pair_1:[], pair_2:[]):
        vlst = (
            ((pair_1[0].get_x(),pair_1[0].get_y()),(pair_1[1].get_x(),pair_1[1].get_y())),
            ((pair_2[0].get_x(),pair_2[0].get_y()),(pair_2[1].get_x(),pair_2[1].get_y()))
        )
        
        xdiff = (vlst[0][0][0] - vlst[0][1][0], vlst[1][0][0] - vlst[1][1][0])
        ydiff = (vlst[0][0][1] - vlst[0][1][1], vlst[1][0][1] - vlst[1][1][1])

        div = Vector3.det(xdiff, ydiff)
        if div == 0: return None  # Linhas não se cruzam

        d = (Vector3.det(*vlst[0]), Vector3.det(*vlst[1]))
        x = Vector3.det(d, xdiff) / div
        y = Vector3.det(d, ydiff) / div
        
        for i in range(2):
            if x > max(vlst[i][0][0], vlst[i][1][0]) or x < min(vlst[i][0][0], vlst[i][1][0]): return None
            if y > max(vlst[i][0][1], vlst[i][1][1]) or y < min(vlst[i][0][1], vlst[i][1][1]): return None
        
        return Vector3(x, y, 0)  # Retorna as coordenadas do cruzamento
    
    def will_collide_2d(transform_len, rotation_axis, pair_1:[], pair_2:[]):
        pv1 = pair_1[0].copy().transform_2d(transform_len, rotation_axis)
        pv2 = pair_1[1].copy().transform_2d(transform_len, rotation_axis)
        
        if Vector3.get_2d_point_intersection([pair_1[0], pv1], pair_2): return  True
        if Vector3.get_2d_point_intersection([pair_1[1], pv2], pair_2): return  True
        if Vector3.get_2d_point_intersection([pv1, pv2], pair_2): return  True
        
        poly = [pair_1, [pair_1[0], pv1], [pair_1[1], pv2], [pv1, pv2]]
        inside = pair_2[0].is_inside(poly) or pair_2[1].is_inside(poly)
        
        return inside