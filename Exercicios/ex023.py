num = int(input('insira um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('unidade {}'.format(u))
print('dezena {}'.format(d))
print('centana {}'.format(c))
print('milhar {}'.format(m))