import Map

class Robot:
    
    def __init__(self, map:Map, x0=0, y0=0):
        self.x0_ = x0
        self.y0_ = y0
        map.occupy(x0,y0)
    
    # Initialize the position of the robot
    def initPos(self):
        print(f"I am at ({self.getX0()},{self.getY0()})")
        
    # Getter and setter
    def getX0(self):
        return(self.x0_)
    def getY0(self):
        return(self.y0_)
        