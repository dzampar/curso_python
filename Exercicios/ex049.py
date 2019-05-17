print('¬º'*15)
print('Vamos calcular a tabuada!!!')
print('¬º'*15)
n = int(input('Digite um numero: '))
print('Tabuada do numero {}'.format(n))
for c in range (1, 11):
   print('{} x {:2} = {}'.format(n,c,n*c))