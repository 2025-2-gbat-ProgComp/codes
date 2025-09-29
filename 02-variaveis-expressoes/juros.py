# Programa para cálculo de juros compostos

capital = float(input("Capital investido: "))
taxa  = float(input("Taxa de juros (em %): "))
tempo = float(input("Tempo de investimento: "))

montante = capital*(1 + taxa/100)**tempo

print ("O montante é: ", round(montante,2))