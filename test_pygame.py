import pygame
import sys
import json


pygame.init()

fenetre = pygame.display.set_mode((150,200))

pygame.draw.rect(fenetre, (255,0,0),(10,30,10,30))

with open("param_map.json","r") as file:
    file_dict = json.load(file)
free_param = file_dict["map"]["free_param"]
occupy_param = file_dict["map"]["occupy_param"]
block_param = file_dict["map"]["block_param"]

# Wait for 5000 milliseconds (5 seconds)
#pygame.time.wait(5000)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
        