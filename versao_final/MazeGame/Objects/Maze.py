import pygame
import random
from MazeGame.MazeGenerator.maze_generation import Graph
from Utils import*

from Engine.Structs.GameObject import GameObject
from Engine.Structs.Vector3 import Vector3
from Engine.Graphics.IGraphicsApi import IGraphicsApi
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.ResourceManager import ResourceManager


class Maze(GameObject):
    
    def __init__(self, initial_position:Vector3=Vector3(0,0,0), size:int=20, block_size:int=15):
        super().__init__(initial_position=initial_position)
        self.__fence_dict = {}
        self.__block_size = block_size
        self.__maze_size = size
        self.__bin_matrix = Graph.binaryMatrix(size)
        self.__fence = ResourceManager().get_image(FENCES)
        
        self.create_collision_polygons()
        self.create_fences_matrix()
    
    def create_fences_matrix(self):
        #[top-right-bottom-left]
        #[0000]: (x_id, y_id)
        
        self.__fence_dict = {
            "0010": (0,0),
            "0110": (1,0),
            "0111": (2,0),
            "0011": (3,0),
            
            "1010": (0,1),
            "1110": (1,1),
            "1111": (2,1),
            "1011": (3,1),
            
            "1000": (0,2),
            "1100": (1,2),
            "1101": (2,2),
            "1001": (3,2),
            
            "0000": (0,3),
            "0100": (1,3),
            "0101": (2,3),
            "0001": (3,3),            
        }
    
    def render_fence(self,x,y):
        pos = self.get_position()
        s = self.__block_size
        m = self.__bin_matrix
        
        if m[x][y] == 0: return
        
        top = m[x][y-1] if y > 0 else 0
        right = m[x+1][y] if x < len(m)-1 else 0
        bottom = m[x][y+1] if y < len(m[0])-1 else 0
        left = m[x-1][y] if x > 0 else 0
        
        size = 16
        x_id,y_id = self.__fence_dict[f"{top}{right}{bottom}{left}"]
        self.get_graphics_api().draw_2d_indexed_sprite(self.__fence, pos.get_x() + x*s, pos.get_y() + y*s, x_id, y_id, size, size)
        
    # def get_end_flag_vec3(self):
    #     pos = self.get_position()
    #     s = self.__block_size
    #     return Vector3(pos.get_x() + s*len(self.__bin_matrix) + 50, pos.get_y() + s*len(self.__bin_matrix), 0);
    
    def get_connections(self, x, y, visited):
        top = (x,y-1)
        right = (x+1,y)
        bottom = (x,y+1)
        left = (x,y-1)
        cons = [top, right, bottom, left]
        cons = [i for i in cons if i[0]>=0 and i[0]<len(self.__bin_matrix) and i[1]>=0 and i[1]<len(self.__bin_matrix[0]) and i not in visited]
        cons = [i for i in cons if self.__bin_matrix[i[0]][i[1]] == 1]
        return cons
    
    def find_largest_path(self, x, y, visited=[], path=[], level=0):
        path.append((x,y))
        cons = [x for x in self.get_connections(x, y, visited) if x not in path]
        if len(cons)==0: 
            return path
        
        _max = None
        _max_len = 0
        for c in cons:
            _path = self.find_largest_path(c[0], c[1],visited, path, level+1)
            _len = len(_path)
            if _len > _max_len or _max == None:
                _max = c
                _max_len = _len
                
        return path
        
    def find_smallest_connections_nodes(self, visited):
        smallest = None
        smallest_len = 0
        
        for x in range(len(self.__bin_matrix)):
            for y in range(len(self.__bin_matrix[x])):
                if (x,y) not in visited:
                    cons = self.get_connections(x,y,visited)
                    if len(cons)<smallest_len or smallest==None:
                        smallest = (x,y)
                        smallest_len = len(cons)

        return smallest
    
    def get_random_free_position(self, margin:Vector3=Vector3(0,0,0),exclude=[]):
        total_width = (self.__block_size*2+1) * self.__maze_size

        aux = True
        while aux:
            x = random.randint(1, self.__maze_size) * self.__block_size*2 + margin.get_x() - self.__block_size
            y = random.randint(1, self.__maze_size) * self.__block_size*2 + margin.get_y() - self.__block_size
        # y = total_width - random.randint(1, total_width//(self.__block_size*2)) * (self.__block_size*2) + margin.get_y()
            if (x, y) not in exclude:
                aux = False
        
        return Vector3(x, y, 0)
    
    def create_collision_polygons(self):
        polys = []
        
        x_len = len(self.__bin_matrix)
        y_len = len(self.__bin_matrix[0])
        
        #horizontal polys
        init_pos = None
        last_pos = None
        for y in range(y_len):
            for x in range(x_len):
                if self.__bin_matrix[x][y] == 1:
                    if init_pos == None:
                        init_pos = (x,y)
                    last_pos = (x,y)
                else:
                    if init_pos!=last_pos:
                        polys.append([init_pos, last_pos])
                    init_pos = None
                    last_pos = None
            if init_pos!=last_pos:
                polys.append([init_pos, last_pos])
            init_pos = None
            last_pos = None
        
        #vertical polys
        init_pos = None
        last_pos = None
        for x in range(x_len):
            for y in range(y_len):
                if self.__bin_matrix[x][y] == 1:
                    if init_pos == None:
                        init_pos = (x,y)
                    last_pos = (x,y)
                else:
                    if init_pos!=last_pos:
                        polys.append([init_pos, last_pos])
                    init_pos = None
                    last_pos = None
            if init_pos!=last_pos:
                polys.append([init_pos, last_pos])
            init_pos = None
            last_pos = None
        
        bs = self.__block_size
        self.set_collision_polygons([CollisionPolygon(vector_list=[Vector3(i[0][0]*bs , i[0][1]*bs, 0), Vector3(i[1][0]*bs, i[1][1]*bs , 0)]) for i in polys])
        return polys
    
    def loop(self): pass
    def start(self): pass
    
    def render_graphics(self, graphics_api:IGraphicsApi):
        super().render_graphics(graphics_api)
        m = self.__bin_matrix
        #TX Tileset Grass.png
        self.get_graphics_api().draw_2d_img(ResourceManager().get_image("TX Tileset Grass2.png"), 0, 0)
        
        for x in range(len(m)):
            for y in range(len(m[x])):
                self.render_fence(x,y)
                
        
    def handle_on_collision(self, collisions_descriptions): pass