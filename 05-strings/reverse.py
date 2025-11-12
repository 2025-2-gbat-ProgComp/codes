# Programa para inverter um texto

texto = input ("Digite um texto: ")

pos = len(texto) - 1
while pos >= 0:
    print (texto[pos], end="")
    pos = pos - 1
    
print()