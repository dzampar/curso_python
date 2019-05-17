count = 0
numero = int(input('Digite um numero: '))
for c in range (1,numero +1):
    if numero % c == 0:
       count = count + 1
       print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print(c,end=' ')
if count == 2:
    print('\n\033[m Seu numero {} é PRIMO\n'
          'Pois ele foi dividido por {} vezes'.format(numero,count))
else:
    print('\n\033[m Seu numero {} NÃO é primo\n'
          'Pois ele foi divido por {} veze(s)'.format(numero,count))



