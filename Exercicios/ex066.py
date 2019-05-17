c = soma = 0
while True:
    n = int(input('Digite um numero:'))
    if n == 999:
        break
    c += 1
    soma += n
print(f'Voce digitou {c} e a soma deles é {soma}')