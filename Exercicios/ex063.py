print('=-'*20)
print('VAMOS CALCULAR A SEQUENCIA DE FIBONACCI')
print('=-'*20)
n = int(input("Quantos termos quer mostrar:"))
t1 = 0
t2 = 1
c = 3
print('~'*20)
print('{} -> {}'.format(t1,t2),end='')
while c <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print('-> FIM!')
