#from math import factorial
n = int(input("Insira um numero para calcular seu fatorial: "))
counter = n
f = 1 # na multiplicação ou divisão o valor neutro é 1 pois o numero multiplicado por 1 sera ele mesmo
print('Calculando fatorial de {}!='.format(n), end='')
while counter > 0:
    print("{}".format(counter), end='')
    print(" x " if counter > 1 else ' =', end='')
    f *= counter
    counter -= 1
print('{}'.format(f))
