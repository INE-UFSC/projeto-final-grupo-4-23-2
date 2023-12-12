import math
import time

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
    
    def get_abs_distance_2d(self, vector):
        return math.sqrt((self.get_x()-vector.get_x())**2 + (self.get_y()-vector.get_y())**2);
    
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
    
    def get_float_array(self):
        return [self.get_x(), self.get_y(), self.get_z()]
    
    def get_float_tuple_2d(self):
        return (self.get_x(), self.get_y())
    
    def det(a:[float], b:[float]):
        return a[0] * b[1] - a[1] * b[0]
    
    def is_inside(self_vec3:[float], edges:[[float]]):
        count = 0
        sx = self_vec3[0]
        sy = self_vec3[1]
        
        for e in edges:
            (x1, y1) = (e[0][0], e[0][1])
            (x2, y2) = (e[1][0], e[1][1])
            sy_sub_y1 = (sy-y1)
            x2_sub_x1 = (x2-x1)
            y2_sub_y1 = (y2-y1)
            
            if (sy < y1) != (sy < y2) and sx < x1 + (sy_sub_y1/y2_sub_y1*x2_sub_x1):
                count += 1
        
        return count%2==1
    
    def get_2d_point_intersection(vec3_pair_1:[[float]], vec3_pair_2:[[float]]):
        vlst = [
            [[vec3_pair_1[0][0],vec3_pair_1[0][1]],[vec3_pair_1[1][0],vec3_pair_1[1][1]]],
            [[vec3_pair_2[0][0],vec3_pair_2[0][1]],[vec3_pair_2[1][0],vec3_pair_2[1][1]]]
        ]
        if vlst[0][0][0]==vlst[0][1][0]: vlst[0][0][0] += 0.0001
        if vlst[0][0][1]==vlst[0][1][1]: vlst[0][0][1] += 0.0001
        if vlst[1][0][0]==vlst[1][1][0]: vlst[1][0][0] += 0.0001
        if vlst[1][0][1]==vlst[1][1][1]: vlst[1][0][1] += 0.0001
        
        xdiff = [vlst[0][0][0] - vlst[0][1][0], vlst[1][0][0] - vlst[1][1][0]]
        ydiff = [vlst[0][0][1] - vlst[0][1][1], vlst[1][0][1] - vlst[1][1][1]]
        
        div = Vector3.det(xdiff, ydiff)
        if div == 0: return None  # Linhas não se cruzam

        t = Vector3.det(*vlst[0])
        d = (Vector3.det(*vlst[0]), Vector3.det(*vlst[1]))
        x = Vector3.det(d, xdiff) / div
        y = Vector3.det(d, ydiff) / div
        
        for i in range(2):
            if x > max(vlst[i][0][0], vlst[i][1][0]) or x < min(vlst[i][0][0], vlst[i][1][0]): return None
            if y > max(vlst[i][0][1], vlst[i][1][1]) or y < min(vlst[i][0][1], vlst[i][1][1]): return None
        
        return Vector3(x, y, 0)  # Retorna as coordenadas do cruzamento
    
    def get_projection_vec3_arrays(transform_len:float, rotation_axis:[float], vec_pair:[[float]]):
        pv1 = vec_pair[0]
        pv1[0] += transform_len * math.sin(rotation_axis[0])
        pv1[1] += transform_len * math.cos(rotation_axis[0])
        
        pv2 = vec_pair[1]
        pv2[0] += transform_len * math.sin(rotation_axis[0])
        pv2[1] += transform_len * math.cos(rotation_axis[0])
        
        return [pv1, pv2]
    
    def will_collide_2d(pv:[[float]], vec_pair_1:[[float]], vec_pair_2:[[float]]):
        if Vector3.get_2d_point_intersection(vec_pair_1, vec_pair_2)!=None: return  True
        if Vector3.get_2d_point_intersection([vec_pair_1[0], pv[0]], vec_pair_2)!=None: return  True
        if Vector3.get_2d_point_intersection([vec_pair_1[1], pv[1]], vec_pair_2)!=None: return  True
        if Vector3.get_2d_point_intersection([pv[0], pv[1]], vec_pair_2)!=None: return  True
        
        poly = [vec_pair_1, [vec_pair_1[0], pv[0]], [vec_pair_1[1], pv[1]], [pv[0], pv[1]]]
        inside = Vector3.is_inside(vec_pair_2[0], poly) or Vector3.is_inside(vec_pair_2[1], poly)
        
        return inside