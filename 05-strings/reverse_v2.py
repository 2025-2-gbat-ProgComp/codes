# Programa para inverter um texto

texto = input ("Digite um texto: ")
texto2 = ""

pos = len(texto) - 1
while pos >= 0:
    texto2 += texto[pos]
    pos = pos - 1
    
print(texto2)