# Programa para verificar palíndromo

texto = input ("Digite um texto: ")
texto = texto.replace(" ", "").upper()

texto2 = ""

for pos in range(len(texto)-1, -1, -1):
    texto2 += texto[pos]
    
if texto == texto2:
    print ("Palíndromo.")