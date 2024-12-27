class Map:
    
    def __init__(self, x=1, y=1):
        self.x_ = x
        self.y_ = y
        self.map_ = self.initMap()
        

    def initMap(self):
        listX = []
        for i in range(self.getY()):
            listY = []
            for j in range(self.getX()):
                listY += [0]
            listX += [listY]
        return listX
    
    def printMap(self):
        print(self.map_)
    
    # =================
    # Getter and Setter
    # =================
    
    def getX(self):
        return(self.x_)
    
    def getY(self):
        return(self.y_)
    
    def getSize(self):
        return(self.x_, self.y_)