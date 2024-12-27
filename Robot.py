import Map

class Robot:
    
    #TODO : lors du placement du robot, vérifier qu'il n'y ait rien de présent
    #Ou accepter deux robots à la même place 
    def __init__(self, map:Map, x0=0, y0=0):
        self.x0_ = x0
        self.y0_ = y0
        self.x_ = x0
        self.y_ = y0
        map.occupy(x0,y0)
    
    # Initialize the position of the robot
    def initPos(self):
        print(f"I am at ({self.getX0()},{self.getY0()})")
    
    #Movements of the robot
    def go_up(self, map):
        if map.check_free(self.x_, self.y_-1):
            map.free(self.x_, self.y_)
            self.y_ = self.y_-1
            map.occupy(self.x_, self.y_)
    
    def go_down(self, map):
        if map.check_free(self.x_, self.y_+1):
            map.free(self.x_, self.y_)
            self.y_ = self.y_+1
            map.occupy(self.x_, self.y_)
    
    def go_right(self, map):
        if map.check_free(self.x_+1, self.y_):
            map.free(self.x_, self.y_)
            self.x_ = self.x_+1
            map.occupy(self.x_, self.y_)
    
    def go_left(self, map):
        if map.check_free(self.x_-1, self.y_):
            map.free(self.x_, self.y_)
            self.x_ = self.x_-1
            map.occupy(self.x_, self.y_)
    
    
            
    
    # Getter and setter
    def getX0(self):
        return(self.x0_)
    def getY0(self):
        return(self.y0_)
        