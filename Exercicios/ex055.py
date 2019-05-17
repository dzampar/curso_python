maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Insira o peso da {}ª pessoa:'.format(c)))
    if c == 1:# esse irá ler só o primeiro peso, pois é == 1, depois cai no else pois não será mais == 1 e sim 2
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))