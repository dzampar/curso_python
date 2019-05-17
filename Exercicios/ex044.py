cores = {'clear':'\033[m',
         'green':'\033[1;30;42m'}
print('='*30)
print('Calculo de Pagamento')
print('='*30)
compra = float(input('Digite o valor da compra:'))
print('1 - dinheiro (10% de desconto)\n'
      '2 - cartão debito(5% de desconto)\n'
      '3 - cartão de credito em 2x(sem desconto)\n'
      '4 - cartão de credito em 3x ou mais(20% de juros)')
opcao = int(input('Selecione o metodo de pagamento:' ))
if opcao ==1:
    desconto = (compra * 10)/100
    total = compra - desconto
    print('Voce teve um desconto de R${}\n'
          'Sua compra ficou em {}R${}{}'.format(desconto,cores['green'],total,cores['clear']))
elif opcao ==2:
    desconto = (compra * 5) / 100
    total = compra - desconto
    print('Voce teve um desconto de R${}\n'
          'Sua compra ficou em {}R${}{}'.format(desconto, cores['green'], total, cores['clear']))
elif opcao ==4:
    acrescimo = (compra * 20) / 100
    total = compra + acrescimo
    print('Voce teve um acrescimo de R${}\n'
          'Sua compra ficou em {}R${}{}'.format(acrescimo, cores['green'], total, cores['clear']))
else:
    total = compra
    print('O valor de sua compra não teve desconto\n'
          'Sua compra ficou em {}R${}{}'.format(cores['green'],total, cores['clear']))