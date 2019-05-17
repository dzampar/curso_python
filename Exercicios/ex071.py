cedulas = 0
c50 = 50
c20 = 20
c10 = 10
c1 = 1
print('$'*30)
print('CAIXA 24 HORAS')
print('$$'*15)
print('CEDULAS DE [1 , 10 , 20 , 50] DISPONIVEIS')
saque = int(input('DIGITE O VALOR DO SAQUE:'))
while saque >= c50:
    saque -= c50
    cedulas +=1
print(f'TOTAL DE {cedulas} CEDULAS DE R$50')
cedulas = 0
while saque >= c20:
    saque -= c20
    cedulas +=1
print(f'TOTAL DE {cedulas} CEDULAS DE R$20')
cedulas = 0
while saque >= c10:
    saque -= c10
    cedulas +=1
print(f'TOTAL DE {cedulas} CEDULAS DE R$10')
cedulas = 0
while saque >= c1:
    saque -= c1
    cedulas +=1
print(f'TOTAL DE {cedulas} CEDULAS DE R$1')
print('='*30)
print('VOLTE SEMPRE')

