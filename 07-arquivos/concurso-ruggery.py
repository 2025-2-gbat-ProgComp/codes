fd = open('dadosResultadoConcurso.txt', 'r')

linhas = fd.readlines()

maior_subj = -1.0
candidato_subj = ''
maior_obj = -1.0
candidato_obj = ''
lista_aprovados = []

maior_nota = -1
lista_10 = []

for linha in linhas:
	colunas = linha.split(';')
	
	inscricao = colunas[0]
	nome = colunas[1]
	n1 = float(colunas[2].replace(',', '.'))
	n2 = float(colunas[3].replace(',', '.'))
	n3 = float(colunas[4].replace(',', '.'))
	subj = float(colunas[5].replace(',', '.'))
	
	media_obj = (n1 + n2 + n3) / 3
	total = media_obj + subj
	aprovado = media_obj >= 6.0 and subj >= 20.0

	if subj > maior_subj:
		maior_subj = subj
		candidato_subj = nome
	
	if media_obj > maior_obj:
		maior_obj = media_obj
		candidato_obj = nome

	if aprovado:
		lista_aprovados.append((nome, total))
		lista_10.append((nome, total))
	

print()
print(' - Resultados finais do concurso - \n')
	
print(f'Maior nota subjetiva: {maior_subj} - {candidato_subj}')
print(f'Maior nota objetiva: {maior_obj} - {candidato_obj}\n')


print('Os aprovados são:')
for nome, total in lista_aprovados:
    print(f'- {nome} - {total}')

print()

lista_10 = sorted(lista_10, key=lambda x: -x[1])[:10]

print(f'Os dez primeiros colocados são:')
for nome, total in lista_10:
	print(f'- {nome} - {total}')