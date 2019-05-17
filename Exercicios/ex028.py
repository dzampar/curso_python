import random
print('Foi gerar um numero entre 0 e 5 tente adivinhar')
usuario = int(input('Digite seu numero: '))
computador = random.randrange(5)
if usuario == computador:
    print('Parabéns você acertou!! Seu numero foi {} e o meu foi {}'.format(usuario,computador))
else:
    print('Não foi dessa vez. Seu numero foi {} e o meu {}'.format(usuario,computador))


