cont = 0
soma = 0
for c in range (1, 501,2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('Existem {} numeros impares multiplos de 3'.format(cont))
print('Estes somandos resultam no numero {}'.format(soma))