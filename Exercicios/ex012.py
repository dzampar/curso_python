n1 = float(input('Digite o valor da compra:'))
n2 = float(input('Quanto de desconto?:'))
de = (n1*n2)/100
to = n1-de
print('Sua compra de R${} teve um desconto de R${:.2f}, total R${:.2f}'.format(n1,de,to))