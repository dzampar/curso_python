print('Passagens até 200Km será cobrado R$0,50 o Km')
print('Do contrario R$0,45 por Km')
n = float(input('Insira a distancia:'))
if n <=200.0:
    p1 = 0.50 * n
    print('O preço da sua passagem é R${}'.format(p1))
else:
    p2 = 0.45 * n
    print('o preço da sua passagem é R${}'.format(p2))
