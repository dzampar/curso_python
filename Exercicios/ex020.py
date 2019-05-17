import random
cores = {'limpa':'\033[m',
         'inverte':'\033[7m'}
a = str(input('escreva o primeiro nome:'))
b = str(input('escreva outro nome:'))
c = str(input('escreva outro:'))
d = str(input('e o utimo nome:'))
lista = [a,b,c,d]
random.shuffle(lista)
print('A ordem dos escolhidos é:')
print(cores['inverte'],lista,cores['limpa'])