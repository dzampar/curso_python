lista = []
u = ' '
while u not in 'N':
    n = int(input("Digite um numero"))
    lista.append(n)
    u = str(input("Deseja Continuar [S/N]?")).strip().upper()
    while u not in 'SN':
        u = str(input("Deseja Continuar [S/N]?")).strip().upper()
print('=-'*30)
print("Você digitou {} Valores".format(len(lista)))
lista.sort(reverse=True)
print(f"Sua lista na ordem decrescente ficou assim {lista}")
if 5 in lista:
    print("O valor 5 está na sua lista")
else:
    print("O valor 5 não está na sua lista")