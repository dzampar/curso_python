nome = str(input('Digite seu nome completo: ')).strip().split()#split dividiu tudo em blocos
cores = {'limpa':'\033[m',
         'roxo':'\033[1;30;45m',
         'azul':'\033[1;30;44m'}
print('primeiro: {}{}{}'.format(cores['roxo'],nome[0],cores['limpa']))
print('último: {}{}{}'.format(cores['azul'],nome[len(nome)-1],cores['limpa']))#exiba o nome mais com a condição
#de contar quantos blocos tem "lean(nome)" e exibir ultimo bloco -1
#o Python sempre conta 1 a casa a mais, porque ele começa no 0
#assim o -1 é para ele exibir o ultimo nome antes do ultimo bloco que o
#Python conta que não existe para nos


