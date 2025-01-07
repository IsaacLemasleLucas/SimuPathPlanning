import pygame
import json

class Map:
    
    def __init__(self, x=1, y=1, scale=25):
        pygame.init()
        self.x_ = x
        self.y_ = y
        self.scale_ = scale
        self.windows_x_ = self.x_ * self.scale_
        self.windows_y_ = self.y_ * self.scale_
        
        # Initialisation of the param saved in the file json
        with open("param_map.json","r") as file:
            file_dict = json.load(file)
        self.free_param = file_dict["map"]["free_param"]
        self.occupy_param = file_dict["map"]["occupy_param"]
        self.block_param = file_dict["map"]["block_param"]
        self.color_osbtacle = tuple(file_dict["colors"]["obstacle"])
        self.color_robot = tuple(file_dict["colors"]["robot"])
        color_background = tuple(file_dict["colors"]["background"])
        
        self.map_ = self.initMap()
        self.fenetre_ = pygame.display.set_mode((self.windows_x_, self.windows_y_))
        self.fenetre_.fill(color_background)
        
    # initialize the map with everything on a free status
    def initMap(self):
        listY = []
        for i in range(self.getY()):
            listX = []
            for j in range(self.getX()):
                listX += [self.free_param]
            listY += [listX]
        return listY
    
    # display the map
    def printMap(self):
        for elem in self.map_:
            print(elem)
        for xi in range(len(self.map_)):
            for yi in range(len(self.map_[xi])):
                if not self.check_free(xi,yi):
                    color = self.getColor(xi,yi)
                    pygame.draw.rect(self.fenetre_, color, (yi*self.scale_,
                                                            xi*self.scale_,
                                                            self.scale_,
                                                            self.scale_))
                    
    # ==================================
    # Modicaters and definers of the map
    # ==================================
            
    # Modify the map
    def occupy(self,x,y):
        self.setMap(x,y, self.occupy_param)
        
    def free(self,x, y):
        self.setMap(x,y,self.free_param)
    
    def check_free(self, x, y):
        return( self.getMap(x,y) == self.free_param)
    
    # Ajout d'obstacles
    def block(self, x, y):
        self.setMap(x,y,self.block_param)
    
    def obstacle(self, x1, x2, y1, y2):
        for i in range(len(self.map_)):
            if x1 <= i and i <= x2:
                for j in range(len(self.map_[i])):
                    if y1<=j and j<=y2:
                        self.block(i,j)
    
    # =================
    # Getter and Setter
    # =================
    
    def getX(self):
        return(self.x_)
    
    def getY(self):
        return(self.y_)
    
    def getSize(self):
        return(self.x_, self.y_)

    def setMap(self,x, y, value):
        self.map_[y-1][x-1] = value
    
    def getMap(self,x, y):
        return(self.map_[x-1][y-1])
    
    def getColor(self, x, y):
        status = self.getMap(x, y)
        switch = {
            self.occupy_param : self.color_robot,
            self.block_param : self.color_osbtacle
        }
        return switch.get(status,(255,255,255))