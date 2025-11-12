# Programa para verificar número palíndromo

texto = input ("Digite um texto: ")

if texto.isdigit():
    texto2 = ""

    for pos in range(len(texto)-1, -1, -1):
        texto2 += texto[pos]
        
    if texto == texto2:
        print ("Número palíndromo.")
else:
    print ("Não é número.")