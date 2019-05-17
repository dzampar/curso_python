primeiro = int(input("Insira o termo:"))
razao = int(input("Insira a razão:"))
print('{}-> '.format(primeiro),end='')
c = 2
while c <= 10:
    pa = primeiro + razao
    print('{}-> '.format(pa),end='')
    c += 1
    primeiro = pa
print('ACABOU')