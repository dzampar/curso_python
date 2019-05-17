print('='*20)
print('Vamos comparar os numeros')
print('='*20)
n1 = float(input('Insira um numero:'))
n2 = float(input('Insira outro: '))
if n1 > n2:
    print('o numero {:.2f} é maior que {:.2f}'.format(n1,n2))
elif n2 > n1:
    print('o numero {:.2f} é maior que {:.2f}'.format(n2,n1))
else:
    print('os numero são iguais')