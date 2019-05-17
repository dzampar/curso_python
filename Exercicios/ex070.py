print('Sistema de calculo de compras')
pnome = str(input('Insira o nome do produto: ')).strip().upper()
pvalor = float(input('Insira o valor do produto: '))
vpbarato = pvalor
npbarato = pnome
tgasto = tp1000 = 0
while True:
    tgasto += pvalor
    if pvalor < vpbarato:
        vpbarato = pvalor
        npbarato = pnome
    if pvalor >= 1000.00:
        tp1000 += 1
    continua = str(input('Deseja Continuar? [S/N]')).strip().upper()
    if continua == 'N':
        print('{:-^40}'.format('FIM DO PROGRAMA'))
        print(f'O total de seus gastos foram R${tgasto}\n'
              f'O produto mais barato foi {npbarato} e custou R${vpbarato}\n'
              f'{tp1000} produto(s) custaram mais de R$1000')
        break
    pnome = str(input('Insira o nome do produto: ')).strip().upper()
    pvalor = float(input('Insira o valor do produto: '))
