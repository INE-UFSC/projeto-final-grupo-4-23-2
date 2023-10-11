from Engine.Structs.Vector3 import Vector3

class SimpleCollision2DMap:
    def __init__(self, bin_map:[[]], block_size:int, map_offset:Vector3):
        self.__bin_map = bin_map
        self.__block_size = block_size
        self.__map_offset = map_offset
    
    def get_bin_matrix(self): return self.__bin_map
    
    def will_collide(self, next_pos:Vector3):
        pos = next_pos.copy()
        str_col_map_x = (self.__map_offset.get_x())
        end_col_map_x = (self.__map_offset.get_x()+len(self.__bin_map[0])*self.__block_size)
        
        str_col_map_y = (self.__map_offset.get_y())
        end_col_map_y = (self.__map_offset.get_y()+len(self.__bin_map)*self.__block_size)
        
        
        """ if pos.get_x() <= 0 or pos.get_y() <= 0: return True
        if not (str_col_map_x < pos.get_x() < end_col_map_x): return False
        if not (str_col_map_y < pos.get_y() < end_col_map_y): return False  """
        
        xdf = (pos.get_x()-str_col_map_x)
        ydf = (pos.get_y()-str_col_map_y)
        x,y = xdf//self.__block_size+1, ydf//self.__block_size+1
        print(x, " ", y)
        
        
        if x>0 and x<len(self.__bin_map):
            if y>0 and y<len(self.__bin_map[x]):
                return self.__bin_map[x][y]==1
        
        return False