#!usr/bin/env python3

import Map
import Robot
import pygame
import sys
import time
    
if __name__ == "__main__":
    
    # Initialisation of pygame
    #pygame.init()
    
    # Creation of a windows
    #fenetre = pygame.display.set_mode((640,480))

    
    # Creation of the map
    my_map = Map.Map(15,20)
    my_map.obstacle(5,12,3,6)
    my_map.obstacle(10,13,5,20)

    # Creation of the robot
    snoopy = Robot.Robot(my_map, 3, 4)
    spot = Robot.Robot(my_map,3,2)
    nao = Robot.Robot(my_map,3,3)
    my_map.printMap()
    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        
    