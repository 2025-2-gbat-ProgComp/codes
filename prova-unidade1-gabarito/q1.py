from random import choice 
 
simbolos = "XaTUKliJkl0912&%*!+" 
senha = "" 
for pos in range(16): 
    senha = senha + choice(simbolos) 
print (senha)

acertou = False 
tentativas = 0 
while (acertou == False) and (tentativas < 3): 
    senha_usuario = input ("Digite a senha: ") 
    if senha == senha_usuario: 
        acertou = True 
    tentativas += 1 

if acertou: 
    print ("Acertou em:", tentativas, "tentativas") 
else: 
    print ("Número de tentativas excedido!!!")