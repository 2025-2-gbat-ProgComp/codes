capital = float(input("Capital inicial: "))
aporte  = float(input("Aporte mensal: "))
taxa    = float(input("Taxa de juros: "))
tempo   = float(input("Tempo de investimento (em meses): "))

fator_juros = (1 + taxa/100)
fator_juros_n = fator_juros**tempo

montante = capital*fator_juros_n + aporte*(fator_juros_n - fator_juros)/(taxa/100)

print ("Montante: ", montante)