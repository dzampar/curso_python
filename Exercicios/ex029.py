velocidade = int(input('Qual foi a velocidade:'))
multa = (velocidade - 80) * 7.0
if velocidade >= 81:
    print('Você ultrapassou o limite de 80Km/h e foi multado em R${}'.format(multa))
else:
    print('Parabéns por dirigir no limite estabelecido')