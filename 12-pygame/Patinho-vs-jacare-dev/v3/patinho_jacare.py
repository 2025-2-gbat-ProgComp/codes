import time 
import pygame

def tem_colisao():
    if ((jac_x+jac_w < pato_x) or
        (pato_x+pato_w < jac_x)):
        return False
    if ((jac_y+jac_h < pato_y) or
        (pato_y+pato_h < jac_y)):
        return False
    return True

CHAO  = 300
 
pato_x = 500
pato_w = 50

pato_h = 50
pato_y = CHAO-pato_h

jac_x = 100
jac_w = 50

jac_h = 50
jac_y = CHAO-jac_h

pygame.init()
tela = pygame.display.set_mode((640, 480))

pygame.display.set_caption('Pato vs Jacare')

pato   = pygame.image.load("../imagens/pato.jpg")
pato   = pygame.transform.scale(pato, (pato_w, pato_h))

jacare = pygame.image.load("../imagens/jacare.jpg")
jacare = pygame.transform.scale(jacare, (jac_w, jac_h))

n_vidas = 3

while True:
    if tem_colisao(): 
        n_vidas -= 1
        pato_x = 500
        pato_y = CHAO-pato_h
        if n_vidas == 0:
            break
        
    event = pygame.event.poll()
    # caso o evento QUIT (clicar no x da janela) seja disparado
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
        pato_y -= 10    
    
    tela.fill(color=(255,255,255))
    for vida in range(n_vidas):
        tela.blit(pato, (450 + vida*60, 10))

    tela.blit(pato, (pato_x, pato_y))
    tela.blit(jacare, (jac_x, jac_y))
    pygame.display.flip()
        
    pato_x -= 10
    if pato_x < 0:
        pato_x = 640
    
    if pato_y+pato_h < CHAO:
        pato_y += 1
    
    time.sleep(0.1)