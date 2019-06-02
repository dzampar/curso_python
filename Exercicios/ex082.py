lista = []
par = []
impar = []
u = ' '
while u not in 'N':
    n = int(input("Digite um numero"))
    lista.append(n)
    u = str(input("Deseja Continuar [S/N]?")).strip().upper()
    while u not in 'SN':
        u = str(input("Deseja Continuar [S/N]?")).strip().upper()
print(f"Sua lista completa é {sorted(lista)}")
for n in lista:
    if n %2 == 0:
        par.append(n)
    if n %2 == 1:
        impar.append(n)
print(f"Sua lista com numeros pares é {sorted(par)}")
print(f"Sua lista com numeros impares é {sorted(impar)}")