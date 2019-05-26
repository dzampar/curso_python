lista= []
while True:
    n = int(input("Digite um valor: "))
    if n not in lista:
        lista.append(n)
        print("Numero adicionado com sucesso...")
    else:
        print("Valor duplicado não vou adicionar...")
    user = str(input("Adicionar outro numero[S/N]?")).strip().upper()
    if user == 'N':
        break
print('=-'*30)
lista.sort()
print(f"Voce digitou os valores {lista}")

