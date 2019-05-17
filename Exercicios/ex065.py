n = int(input("Digite um numero: "))
c = 1
maior = menor = soma = n
continua = str(input("Continua? [S/N]")).upper().strip()[0]
while continua == "S":
    n = int(input("Digite um numero: "))
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    c += 1
    continua = str(input("Continua? [S/N]")).upper().strip()[0]
    soma += n
media = soma / c
print("Voce digitou",c,"numeros e a media foi ",media,
      "\nO maior valor foi ",maior,"e o menor ",menor)