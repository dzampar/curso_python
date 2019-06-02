pessoas = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    segue = str(input('Continua[S/N]?')).strip().upper()
    if segue in 'N':
        break
print("=-"*30)
print("No total foram cadastradas {} pessoas".format(len(pessoas)))
print("O maior peso foi de {}Kg.".format(maior),end=' ')
for p in pessoas:
    if p[1] ==maior:
        print(f'Peso de {p[0]}')
print('O menor peso foi de {}Kg'.format(menor),end=' ')
for p in pessoas:
    if p[1] ==menor:
        print(f'Peso de {p[0]}')



