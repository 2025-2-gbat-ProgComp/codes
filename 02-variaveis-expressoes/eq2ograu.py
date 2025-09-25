# Este programa calcula as raizes de uma eq do 2o grau.
# Ele foi feito por Galileu Batista em set/2025.

print ("Programa para calcular  raizes de uma eq. 2o. grau")

a = int(input("Digite o coeficiente a: "))
b = int(input("Digite o coeficiente b: "))
c = int(input("Digite o coeficiente c: "))

delta = b**2 - 4*a*c
x1 = (-b + delta**(1/2)) / (2*a)
x2 = (-b - delta**(1/2)) / (2*a)

print ("As raizes sao", x1, x2)