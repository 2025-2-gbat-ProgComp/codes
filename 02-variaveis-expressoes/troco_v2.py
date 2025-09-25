# Este programa calcula o troco de uma conta.
# Ele foi feito por Galileu Batista em set/2025.
 
valor_conta = int(input("Qual o valor da conta: "))
valor_pago  = int(input("Qual o valor de pagamento: "))
troco = valor_pago - valor_conta
print ("O valor do troco é: ", troco)

ced200 = troco // 200
print ("Devolva ", ced200, "cédulas de 200.")
troco = troco - 200*ced200

ced100 = troco // 100
print ("Devolva ", ced100, "cédulas de 100.")
