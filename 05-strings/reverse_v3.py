# Programa para inverter um texto

texto = input ("Digite um texto: ")
texto2 = ""

for pos in range(len(texto)-1, -1, -1):
    texto2 += texto[pos]
    
print(texto2)