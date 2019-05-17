print('Vamos ver se pode ser feito um triangulo')
print('Insira as medidas')
a = float(input('Medida a:'))
b = float(input('Medida b:'))
c = float(input('Medida c:'))
if b - c < a and a < b + c:
    print('\33[30;45mCom suas medidas \33[1;30;42mPODE\33[m\33[30;45m ser feito um triangulo\33[m')
else:
    print('\33[30;45mCom suas medidas \33[1;30;41mNÃO\33[m\33[30;45m pode ser feito um triangulo\33[m')
