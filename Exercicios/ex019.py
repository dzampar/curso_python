import random
import emoji
a = str(input('escreva o primeiro nome:'))
b = str(input('escreva outro nome:'))
c = str(input('escreva outro:'))
d = str(input('e o utimo nome:'))
lista = [a,b,c,d]
x = random.choice(lista)
print('O escolhido foi: {} !!!Parabéns'.format(x),emoji.emojize(":smile:",use_aliases=True))