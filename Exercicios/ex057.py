sexo = str(input("Digite seu sexo[F/M]: ")).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input("Dados Invalidos, voce esta digitando correto? [F/M]: ")).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))