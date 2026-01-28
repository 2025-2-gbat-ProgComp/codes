import time 

pato_x = 500
pato_w = 50
pato_y = 300
pato_h = 50

jac_x = 100
jac_w = 50
jac_y = 300
jac_h = 50

# pato = Ler a imagem do pato
# jacare = Ler a imagem do jacare

while (jac_x+jac_w) < pato_x:
    # Limpar a tela
    # Desenhar o pato
    print (f"O pato está em {pato_x, pato_y}")
    # Desenhar o jacare
    print (f"O jacare está em {jac_x, jac_y}")
    
    pato_x -= 10
    if pato_x < 0:
        pato_x = 640
        
    time.sleep(1)