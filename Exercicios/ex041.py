from datetime import date
print('-'*50)
print('Vamos verificar sua categoria paro o time de natação')
print('-'*50)
ano = int(input('Insira o seu ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('Voce está no mirim')
elif idade in (10,11,12,13,14):
    print('Voce está no infantil')
elif idade in (15,16,17,18,19):
    print('Voce esta no juniores')
elif idade == 20:
    print('Vc esta no senior')
else:
    print('Voce está no master')
