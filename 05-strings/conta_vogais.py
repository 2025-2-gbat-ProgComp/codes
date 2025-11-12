texto = input("Digite um texto: ")

letras_a = 0
letras_e = 0
letras_i = 0
letras_o = 0
letras_u = 0

for letra in texto:
    if letra == 'a':
        letras_a += 1
    if letra == 'e':
        letras_e += 1
    if letra == 'i':
        letras_i += 1
    if letra == 'o':
        letras_o += 1
    if letra == 'u':
        letras_u += 1
        
print ("Letras a: ", letras_a)
print ("Letras e: ", letras_e)
print ("Letras i: ", letras_i)
print ("Letras o: ", letras_o)
print ("Letras u: ", letras_u)