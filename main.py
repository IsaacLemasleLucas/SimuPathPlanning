#!usr/bin/env python3

import Map
import Robot
import matplotlib
import tkinter
    
if __name__ == "__main__":
    
    # Creation of the map
    my_map = Map.Map(15,20)
    my_map.obstacle(5,12,3,6)
    my_map.obstacle(10,13,5,20)
    # Creation of the robot
    snoopy = Robot.Robot(my_map, 3, 4)
    spot = Robot.Robot(my_map,3,2)
    
    # Actions
    my_map.printMap()
    print("\n\n")
    my_map.printMap()
    snoopy.go_right(my_map)
    snoopy.go_right(my_map)
    snoopy.go_right(my_map)
    print("\n\n")
    my_map.printMap()
    
    
    