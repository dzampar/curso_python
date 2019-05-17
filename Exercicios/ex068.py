from random import randint
c = 0
print('==-'*10)
print('VAMOS JOGAR PAR OU IMPAR')
print('==-'*10)
while True:
    jogador = str(input('Escolha Par ou Impar [P/I]: ')).strip().upper()[0]
    njogardor = int(input('Digite seu número: '))
    if jogador == 'I':
        computador = 'P'
        ncomputador = randint(0, 10)
        soma = njogardor + ncomputador
        resultado = soma %2
        if resultado == 0:
            print('GAME OVER :(')
            print(f'Você jogou {njogardor} e o computador {ncomputador} somando {soma} que é par')
            print(f'Você ganhou {c} vezes')
            break
        if resultado == 1:
            print('PARABÉNS VOCÊ GANHOU !!!')
            print(f'Você jogou {njogardor} e o computador {ncomputador} somando {soma} que é impar')
    if jogador == 'P':
        computador = 'I'
        ncomputador = randint(0, 10)
        soma = njogardor + ncomputador
        resultado = soma %2
        if resultado == 0:
            print('PARABÉNS VOCÊ GANHOU !!!')
            print(f'Você jogou {njogardor} e o computador {ncomputador} somando {soma} que é par')
        if resultado == 1:
            print('GAME OVER :(')
            print(f'Você jogou {njogardor} e o computador {ncomputador} somando {soma} que é impar')
            print(f'Você ganhou {c} vezes')
            break
    c += 1