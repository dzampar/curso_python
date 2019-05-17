sal = float(input('Informe seu salario atual: '))
cores = {'limpa':'\033[m',
         'verde':'\033[32m'}
if sal >=1250.01:
    au = (sal * 10)/100
    sal = au + sal
    print('Seu aumento é de 10% = R$ {}{}{}'.format(cores['verde'],au,cores['limpa']))
    print('Seu salario passou para R$ {}{}{}'.format(cores['verde'],sal,cores['limpa']))
else:
    au = (sal * 15)/100
    sal = au + sal
    print('Seu aumento é de 15% = R$ {}{}{}'.format(cores['verde'],au,cores['limpa']))
    print('Seu salario passou para R$ {}{}{}'.format(cores['verde'],sal,cores['limpa']))
