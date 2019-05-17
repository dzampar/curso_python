n = 0
soma = 0
cont = 0
while n != 999:
    n = int(input("Insira um numero: "))
    if n != 999:
        cont += 1
        soma += n
print('o total dos {} numeros digitados é {}'.format(cont,soma))