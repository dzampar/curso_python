tupla = ('ZERO','UM','DOIS','TRES','QUATRO','CINCO',
         'SEIS','SETE','OITO','NOVE','DEZ','ONZE','DOZE',
         'TREZE','QUATORZE','QUINZE','DEZESSEIS','DEZESSETE',
         'DEZOITO','DEZENOVE','VINTE')
while True:
    n = int(input('Digite um numero entre 0 e 20=>'))
    if 0<= n <=20:
        break
    print('Digite o numero correto!!',end='...')
print(f"Você digitou o numero {tupla[n]}")
