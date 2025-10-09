# Programa que lê um número inteiro positivo de até 4 dígitos e calcula a soma dos valores de cada dígito.
# Programa codado por Lucas Mateus em out/2025

try:
    number = int(input("Digite um número inteiro: "))
    if number > 0:
        if number > 999 and number < 10000:
            
            unidade = number % 10
            dezena = (number // 10) % 10
            centena = (number // 100) % 10
            milhar = (number // 1000) % 10
            somaValor = unidade + dezena + centena + milhar
            
            
            print("Unidade: ", unidade)
            print("Dezena: ", dezena)
            print("Centena: ", centena)
            print("Milhar: ", milhar)
            print("A soma dos valores é: ", somaValor)
            print("O número digitado é: ", number)
        elif number <= 999:
            print("O número digitado é: ", number)
            print("O número digitado não alcança os 4 dígitos.")
        elif number >= 10000:
            print("O número digitado é: ", number)
            print("O número digitado excede o limite de 4 dígitos.")
    else:
        print("O número digitado não é positivo.")
except ValueError:
    print("O valor digitado não é um número inteiro.")
except Exception as e:
    print("Ocorreu um erro inesperado:", e)