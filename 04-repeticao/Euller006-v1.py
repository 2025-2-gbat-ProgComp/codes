'''
Este programa resolve o problema 06 do Projeto Euller.
https://projecteuler.net/problem=6
Por Galileu Batista - Out 2025
IFRN/CNAT
'''

soma = 0
x = 1

while x < 1000:
    soma =  soma + x
    x = x + 1
quadrado_soma = soma * soma

soma_quadrados = 0
x = 1
while x < 1000:
    soma_quadrados =  soma_quadrados + x*x
    x = x + 1

print ("A diferenca entre o quadrado da soma e a soma dos quadrados ",
       "dos numeros menores do que 1000 é:", 
       quadrado_soma - soma_quadrados)