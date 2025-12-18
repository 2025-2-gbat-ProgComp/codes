arquivo = open("try_on-2017-11-13.txt", "r")

n_linhas = 0
n_palavras = 0
n_caract  = 0

tudo = arquivo.readlines()

n_linhas = len(tudo)
for linha in tudo:
    n_caract += len(linha)

    palavras = linha.split()
    for palavra in palavras:
        n_palavras += 1
    
print (n_linhas, n_palavras, n_caract)
arquivo.close()
