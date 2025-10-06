# Este programa calcula as raizes de uma eq do 2o grau.
# Ele foi feito por Galileu Batista em out/2025.

print ("Programa para calcular  raizes de uma eq. 2o. grau")

a = int(input("Digite o coeficiente a: "))
b = int(input("Digite o coeficiente b: "))
c = int(input("Digite o coeficiente c: "))

if a != 0:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + delta**(1/2)) / (2*a)
        x2 = (-b - delta**(1/2)) / (2*a)

        print ("As raizes sao", x1, x2)
    else:
        if delta == 0:
            x1 = -b / (2*a)
            print ("A unica raiz eh", x1)
        else:
            print ("Não há raizes reais.")
else:
    print ("Não é eq. do segundo grau. a == 0.")
