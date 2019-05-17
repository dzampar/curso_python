print('Vamos ver se pode ser feito um triangulo')
print('Insira as medidas')
r1 = int(input('Medida a:'))
r2 = int(input('Medida b:'))
r3 = int(input('Medida c:'))
if r2 - r3 < r1 and r1 < r2 + r3:
   print('Com suas medidas PODE ser feito um triangulo ', end='')
   if r1 == r2 == r3:
         print('EQUILATERO!!')
   elif r1 != r2 != r3 != r1:
         print('ESCALENO!!')
   else:
         print('ISOSCELES!!')
else:
    print('Com suas medidas NÃO pode ser feito um triangulo')
