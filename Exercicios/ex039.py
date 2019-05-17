from datetime import date
print('-'*50)
print('Vamos verificar seu alistamento')
print('-'*50)
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
if idade == 18:
    print('Está na hora de se alistar malandro!!!')
elif idade < 18:
    falta = 18 - idade
    print('Ainda não está na hora de se alistar')
    print('Faltam {} anos para se alistar'.format(falta))
else:
    passou = idade - 18
    print('Passou da hora de se alistar')
    print('Vc já passou {} anos do seu alistamento'.format(passou))