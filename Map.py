class Map:
    
    def __init__(self, x=1, y=1):
        self.x_ = x
        self.y_ = y
        self.map_ = self.initMap()
        

    def initMap(self):
        listY = []
        for i in range(self.getY()):
            listX = []
            for j in range(self.getX()):
                listX += [0]
            listY += [listX]
        return listY
    
    def printMap(self):
        for elem in self.map_:
            print(elem)
    
    # =================
    # Getter and Setter
    # =================
    
    def getX(self):
        return(self.x_)
    
    def getY(self):
        return(self.y_)
    
    def getSize(self):
        return(self.x_, self.y_)