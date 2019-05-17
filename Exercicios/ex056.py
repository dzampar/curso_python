nomehmaior = ''
somaidade = 0
nmulher20 = 0
hmaior = 0
for c in range(1, 6):
    print('----{}ª PESSOA----'.format(c))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip().upper()
    somaidade += idade
    if c == 1 and sexo == 'M':
         hmaior = idade
         nomehmaior = nome
    if idade > hmaior and sexo == 'M':
             hmaior = idade
             nomehmaior = nome
    if sexo == 'F' and idade < 20:
             nmulher20 += 1
mediaidade = somaidade /4
print('A media de idade do grupo é {}'.format(mediaidade))
print("O homem mais velho tem {} anos é se chama {}".format(hmaior,nomehmaior))
print('Existem {} mulheres no grupo com menos de 20 anos'.format(nmulher20))


