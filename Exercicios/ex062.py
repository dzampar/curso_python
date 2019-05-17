primeiro = int(input("Insira um numero:"))
razao = int(input("Insira a razao:"))
termo = primeiro
mais = 10
total = 0
contador = 1
while mais != 0:
    if mais > 0:
        total += mais
    while contador <= total:
        print(termo, end= '..')
        termo += razao
        contador +=1
    print('PAUSA')
    mais = int(input("Quantos mais:"))
print('FIM')
print("total de {} PA".format(total))

'''primeiro = int(input("Insira um numero:"))
razao = int(input("Insira a razao:"))
limite = 10
contador = 10
indice = 0
while indice < limite:
    print(primeiro, end='..')
    primeiro += razao
    indice += 1
    if indice == limite:
        print('PAUSA')
        limite = int(input("Quantos a mais: "))
        indice = 0
        if limite > 0:
            contador += limite
print('FIM')
print('Rodou {} vezes'.format(contador))'''