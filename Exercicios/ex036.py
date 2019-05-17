cores = {'clear':'\033[m',
         'red':'\033[30;41m',
         'green':'\033[30;42m',
         'purple':'\033[1;30;45m'}
print('='*35)
print('{}Calculo para emprestimo imobiliario{}'.format(cores['purple'],cores['clear']))
print('='*35)
a = float(input('Insira o valor do imovel: '))
b = float(input('Qual a sua renda?: '))#salario
c = int(input('Quantos anos deseja pagar?:'))
d = int(input('e meses?: '))
prestacao = a / ((c * 12) + d)
limite = (b * 30)/100
if prestacao <= limite:
    print('{}Seu emprestimo foi aprovado{}'.format(cores['green'],cores['clear']))
    print('Sua prestação é de R$ {:.2f}'.format(prestacao))
else:
    print('{}Seu emprestimo foi negado{}\n'
    'Sua prestação de R$ {:.2f} excedeu o limite de R${}\n'
    'que representa 30% do salario de R$ {}'.format(cores['red'],cores['clear'],prestacao,limite,b))