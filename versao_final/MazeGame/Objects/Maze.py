import pygame
from MazeGame.MazeGenerator.maze_generation import Graph

from Engine.Structs.GameObject import GameObject
from Engine.Structs.Vector3 import Vector3
from Engine.Graphics.IGraphicsApi import IGraphicsApi
from Engine.Physics.CollisionPolygon import CollisionPolygon


class Maze(GameObject):
    
    def __init__(self, initial_position:Vector3=Vector3(0,0,0), size:int=20, block_size:int=15):
        super().__init__(initial_position=initial_position)
        self.__block_size = block_size
        self.__bin_matrix = Graph.binaryMatrix(size)
        self.create_collision_polygons()
        self.__fences_img = pygame.image.load("MazeGame\\Assets\\Images\\fences.png").convert()
    
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
        pos = self.get_position()
        m = self.__bin_matrix
        s = self.__block_size
        for x in range(len(m)):
            for y in range(len(m[x])):
                if m[x][y] == 1: # and x==0 and y==0
                    pass#self.get_graphics_api().draw_2d_rect(pos.get_x() + s*x, pos.get_y() + s*y, s, s, (255,0,0))
        
    def handle_on_collision(self, collisions_descriptions): pass