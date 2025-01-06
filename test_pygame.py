import pygame
import sys

pygame.init()

fenetre = pygame.display.set_mode((150,200))

pygame.draw.rect(fenetre, (255,0,0),(10,10,20,20))



# Wait for 5000 milliseconds (5 seconds)
#pygame.time.wait(5000)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
        