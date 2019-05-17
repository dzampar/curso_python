print('Vamos ver seu IMC')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura ** 2)
print('Seu IMC é: \033[1;30;44m{:.1f}\033[m'.format(imc))
if imc < 18.5:
    print('Vc está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('vc esta no peso ideal')
elif imc >= 25.1 and imc < 30:
    print('Vc está com sobrepeso')
elif imc >= 30.1 and imc < 40:
    print('Vc esta obeso')
else:
    print('Obsidade morbida')
