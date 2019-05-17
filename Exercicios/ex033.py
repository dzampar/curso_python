n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
n3 = int(input('Digite e outro:'))
# calcular o menor
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
#calcular o maior
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('Maior valor é {}'.format(maior))
print('Menor valor é {}'.format(menor))
