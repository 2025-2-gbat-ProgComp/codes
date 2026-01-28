def leia_palavras (file_name):
    fd = open (file_name, "r")
    palavras = fd.read().replace('"', '')
    fd.close()
    return palavras.split(',')

def valora_palavra (palavra):
    valor = 0;
    for letra in palavra:
        valor += ord(letra) - 64
    return valor

def esta_na_sequencia(valor):
    # Resolve a expressão 1/2*n*(n+1) == x 
    # e verifica se é inteiro positivo
    posicao = (-1 + (1+8*valor)**0.5)/2
    return posicao == int(posicao)
    
def eh_triagular(palavra):
    valor_palavra = valora_palavra(palavra)
    if esta_na_sequencia(valor_palavra):
        return True
    else:
        return False

def main():
    palavras = leia_palavras("words.txt")

    num_palavras = 0
    for palavra in palavras:
        if eh_triagular(palavra):
            num_palavras += 1            
    print (f"O número de palavras triangulares é {num_palavras}.")
    
main()
