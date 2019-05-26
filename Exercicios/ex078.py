num = []
pmaior = []
pmenor = []
for c in range(0, 5):
    val = int(input("Digite um valor ="))
    num.append(val)
for p, v in enumerate(num):
    if v == max(num):
        pmaior.append(p)
    if v == min(num):
        pmenor.append(p)
print('{:=^40}'.format('Seus Valores'))
print(f'Voce digitou os valores {num}')
print(f'O maior valor digitado foi {max(num)} na posição {pmaior}')
print(f'O menor valor digitado foi {min(num)} na posição {pmenor}')