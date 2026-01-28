import time 
import pygame

pato_x = 500
pato_w = 50
pato_y = 300
pato_h = 50

jac_x = 100
jac_w = 50
jac_y = 300
jac_h = 50

pygame.init()
tela = pygame.display.set_mode((640, 480))

pygame.display.set_caption('Pato vs Jacare')

pato   = pygame.image.load("../imagens/pato.jpg")
pato   = pygame.transform.scale(pato, (pato_w, pato_h))

jacare = pygame.image.load("../imagens/jacare.jpg")
jacare = pygame.transform.scale(jacare, (jac_w, jac_h))

while jac_x+jac_w < pato_x:
    
    tela.fill(color=(255,255,255))
    tela.blit(pato, (pato_x, pato_y))
    tela.blit(jacare, (jac_x, jac_y))
    pygame.display.flip()
        
    pato_x -= 10
    if pato_x < 0:
        pato_x = 640
        
    time.sleep(0.1)