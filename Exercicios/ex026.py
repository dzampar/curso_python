nome = str(input('Digite seu nome: ')).upper().strip()
print('Possui {} vezes a letra A'.format(nome.count('A')))
print('Ela aparece pela primeira vez na posição {}'.format(nome.find('A')+1))
print('Ela aparece pela última vez na posição {}'.format(nome.rfind('A')+1))