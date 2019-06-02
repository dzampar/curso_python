numeros = [[],[]]
for c in range (1, 7):
    valores = int(input('Digite o {}º valor'.format(c)))
    if valores %2 ==0:
        numeros[0].append(valores)
    else:
        numeros[1].append(valores)
print('=-'*30)
print('Os valores pares digitados foram:{}'.format(sorted(numeros[0])))
print('Os valores impares digitados foram:{}'.format(sorted(numeros[1])))
