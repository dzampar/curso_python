import math
a = float(input('Insira um angulo para calculo: '))
cos = math.cos(a)
sin = math.sin(a)
tan = math.tan(a)
print('O cosseno do angulo {} é igual a {:.2f}'.format(a, cos))
print('O seno do angulo {} é igual a {:.2f}'.format(a, sin))
print('A tangente do angulo {} é igual a {:.2f}'.format(a, tan))