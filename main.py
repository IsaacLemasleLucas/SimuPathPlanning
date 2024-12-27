import Map
import Robot
    
if __name__ == "__main__":
    my_map = Map.Map(15,20)
    snoopy = Robot.Robot(my_map, 3, 4)
    snoopy.initPos()
    my_map.printMap()
    