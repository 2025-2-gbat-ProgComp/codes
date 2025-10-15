num = int(input("Digite um número: "))
num_orig = num
invertido = 0
while num > 0:
    ult_digito = num % 10
    invertido = invertido*10 + ult_digito
    num //= 10

if invertido == num_orig:
    print (num_orig, "é palíndromo")
else:
    print (num_orig, "não é palíndromo")
