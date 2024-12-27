class Map:
    
    def __init__(self, x=1, y=1):
        self.x_ = x
        self.y_ = y
        self.free_param = 'o'
        self.occupy_param = 'X'
        self.block_param = 'B'
        self.map_ = self.initMap()
        
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
        return(self.map_[y-1][x-1])