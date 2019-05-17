import math
y = int(input('insira o cateto oposto:' ))#cateto oposto
x = int(input('insira o cateto adjacente:'))#cateto adjacente
h = math.hypot(x,y) #hipoteneusa
print('O cateto da hipotenusa é: {:.2f}'.format(h))