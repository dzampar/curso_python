from datetime import date
ano = int(input('Digite o ano, se for 0(zero) será o ano atual: '))
if ano ==0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(' Ano {} é Bissexto'.format(ano))
else:
    print('Ano {} não é Bissexto'.format(ano))