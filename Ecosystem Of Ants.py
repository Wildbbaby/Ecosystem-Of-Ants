import pygame, sys

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Ecosystem Of Ants')

screen = pygame.display.set_mode((800,600))
fauna = pygame.Surface((800,40))
terra = pygame.Surface((800,600))
terra.fill((38,27,7))
fauna.fill((31,54,16))

formica = pygame.image.load('Skin/FormicaN.png')

while True: 
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    
     screen.fill((49,214,206))   
     screen.blit(terra,(0,100))
     screen.blit(fauna,(0,100))
     screen.blit(formica,(100,200))
     pygame.display.flip()
     clock.tick(60)
