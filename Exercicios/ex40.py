print('§'*30)
print('Vamos verificar sua media')
print('§'*30)
n1  = float(input('insira sua nota: '))
n2 = float(input('insira outra nota: '))
media = (n1 + n2) /2
if media > 10:
    print('Acho que vc esta digitando os valores errado\n'
          'confira novamente as notas que digitou')
elif media >=7:
    print('Parabens voce passou, sua media é {}'.format(media))
elif media < 5:
    print('Vc foi reprovado, sua media foi {}'.format(media))
else:
    print('Vc ficou de recuperação, sua media foi {}'.format(media))