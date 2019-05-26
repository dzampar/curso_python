# minha solução
'''lista = []
v = int(input("Digite um Valor"))
lista.append(v)
print("Adicionado ao final da lista")
for n in range(1, 5):
    v = int(input("Digite um Valor"))
    if v > max(lista):
        v = lista.append(v)
        print("Adicionado ao final da lista")
    elif v < min(lista):
        v = lista.insert(0, v)
        print("Adicionado ao inicio da lista")
    elif v <= lista[1]:
        v = lista.insert(1, v)
        print("Adicionado a posição 1 da lista")
    elif v >= lista[1] and v <= lista[2]:
        v = lista.insert(2, v)
        print("Adicionado a posição 2 da lista")
    elif v >= lista[1] and v <= lista[3]:
        v = lista.insert(3, v)
        print("Adicionado a posição 3 da lista")
print(lista)'''
#Solução Otimizada
lista = []
# o primeiro numero será adicionado pelo append, pois o valor de c é igual a 0.
for c in range(5):
    n = int(input('Número: '))
    if c == 0 or n > lista[-1]: #lista[-1] representa ultimo numero da lista
        lista.append(n)
        print('O número foi adicionado no final da lista.')
    else:
        for i in range(5): # i irá iniciar em zero que será a posição na lista
            if n <= lista[i]: # se o numero digitado for menor que o numero da posição i
                lista.insert(i,n) # faça o insert na posição i do valor digitado
                print(f'O número foi adicionado na posição {i}.')#printa a posição
                break#se o laço não quebrar volta para o for e o valor de i passa a ser 1
                     #e assim até chegar no 5 e econtrar um numero para quebrar o laço
print(lista)