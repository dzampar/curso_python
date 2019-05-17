n1 = float(input('Digite seu salario:'))
n2 = float(input('Quantos % de aumento:'))
au = (n1*n2)/100
to = n1+au
print('Seu salario de R${} teve um aumento de R${:.2f}, total R${:.2f}'.format(n1,au,to))