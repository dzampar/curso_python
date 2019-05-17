import random
from time import sleep
cores = {'clear':'\033[m',
         'purple':'\033[30;45m',
         'yellow':'\033[30;43m',
         'green':'\033[30;42m',
         'red':'\033[30;41m'}
print('*'*34)
print('{}Vamos jogar PEDRA, PAPEL e TESOURA{}'.format(cores['purple'],cores['clear']))
print('*'*34)
print('[ 1 ]PEDRA\n'
      '[ 2 ]PAPEL\n'
      '[ 3 ]TESOURA')
choice = int(input('Escolha sua opção: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
result = random.randrange(1,4)
if result == 1:
    print('***PEDRA***')
    if choice == 1:
        print('{}Empate, Vamos jogar novamente!!{}'.format(cores['yellow'],cores['clear']))
    elif choice == 2:
        print('{}Voce ganhou!!, papel cobre pedra{}'.format(cores['green'],cores['clear']))
    else:
        print('{}Voce perdeu, pedra quebra tesoura{}'.format(cores['red'],cores['clear']))
elif result == 2:
    print('***PAPEL***')
    if choice == 1:
        print('{}Você perdeu, papel cobre pedra{}'.format(cores['red'],cores['clear']))
    elif choice == 2:
        print('{}Empate, Vamos jogar novamente{}'.format(cores['yellow'],cores['clear']))
    else:
        print('{}Você ganhou!! Tesoura corta papel{}'.format(cores['green'],cores['clear']))
else:
    print('***TESOURA***')
    if choice == 1:
        print('{}Você ganhou!! Pedra quebra tesoura{}'.format(cores['green'],cores['clear']))
    elif choice == 2:
        print('{}Você perdeu, tesoura corta papel{}'.format(cores['red'],cores['clear']))
    else:
        print('{}Empate, Vamos jogar novamente{}'.format(cores['yellow'],cores['clear']))