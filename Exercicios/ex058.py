from random import randint
computador = randint(0, 10)
print('Sou seu computador, acabei de pensar um numero entre 0 e 10')
print('Será que voce consegue acertar qual foi:')
acertou = False
contador = 0
while not acertou:
    jogador = int(input('Qual o seu numero:'))
    contador += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.... Tente outra vez')
        elif jogador > computador:
            print('Menos.... Tente outra vez')
print('Acertou com {} tentativas'.format(contador))