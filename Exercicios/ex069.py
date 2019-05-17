#Variaveis de armazenamento
maiores = thomens = tmulheresmenor20 = 0
while True:
    print('CADASTRO DE DADOS')
    print('=' * 20)
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [F/M]: ')).upper().strip()[0]
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        thomens += 1
    if sexo == 'F' and idade < 20:
        tmulheresmenor20 += 1
    continua = str(input('Continuar cadastrando [S/N] ?')).upper().strip()
    if continua == 'N':
      print('='*20)
      print('FIM DO CADASTRO')
      print('=' * 20)
      print(f'Existem {maiores} pessoa(s) maiore(s) de idade cadastrada(s) no sistema\n'
           f'Total de homens cadastrados = {thomens}\n'
           f'Total de mulheres menor de 20 anos = {tmulheresmenor20}')
      break
