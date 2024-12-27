class Map:
    
    def __init__(self, x=1, y=1):
        self.x_ = x
        self.y_ = y
        self.free_param = 'o'
        self.occupy_param = 'X'
        self.block_param = '-'
        self.map_ = self.initMap()
        
    # initialize the map with everything on a free status
    def initMap(self):
        listX = []
        for i in range(self.getX()):
            listY = []
            for j in range(self.getY()):
                listY += [self.free_param]
            listX += [listY]
        return listX
    
    # dsplay the map
    def printMap(self):
        for elem in self.map_:
            print(elem)
            
    def occupy(self,x,y):
        self.setMap(x,y, self.occupy_param)
        
    def free(self,x, y):
        self.setMap(x,y,self.free_param)
    
    def check_free(self, x, y):
        return( self.getMap(x,y) == self.free_param)
    
    def block(self, x, y):
        self.setMap(x,y,self.block_param)
    
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