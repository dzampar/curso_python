import pyconverter
cores = {'clear':'\033[m',
         'yellow':'\033[1;30;43m',
         'puple':'\033[1;30;45m',
         'blue':'\033[1;30;44m',
         'green':'\033[1;30;42m'}
print('*'*30)
print('{}Vamos converter um numero inteiro{}'.format(cores['green'],cores['clear']))
print('*'*30)
n = int(input('Digite um numero inteiro: '))
print('{}1-Binário {}  {}2-Octal   {}   {}3-Hexadecimal{}'.format(cores['puple'],cores['clear'],cores['yellow'],cores['clear'],cores['blue'],cores['clear']))
user = int(input('Selecione uma das opções acima, digite o numero: '))
if user == 1:
    b = pyconverter.inttobin(n)
    print('Seu numero em binario é ***{}***'.format(b))
elif user == 2:
    b = pyconverter.inttobin(n)
    o = pyconverter.bintooct(b)
    print('Seu numero em octal é ***{}***'.format(o))
else:
    h = pyconverter.inttohex(n)
    print('Seu numero em hexadecimal é ***{}***'.format(h))


