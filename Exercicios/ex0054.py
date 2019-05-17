from datetime import date
maior = 0
menor = 0
for c in range (1,8):
    nascimento = int(input('Insira o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = date.today().year - nascimento
    if idade <18:
        menor = menor + 1
    else:
        maior = maior + 1
print('{} pessoas são de maior'.format(maior))
print('{} pessoa são de menor'.format(menor))
