from random import sample #sample cria uma lista de numero definidos em um range(),'n' numero de repetições
tupla = tuple(sample(range(60), 6))
print('Os valores sorteados são: ',end='')
for n in tupla:
    print(f'{n} ',end='')
print(f'\nO maior numero é o {max(tupla)}\n'
      f'O menor numero é o {min(tupla)}')
