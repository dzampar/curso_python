import temp2temp
n = float(input('Digite o valor da temperatura em ºC: '))
f = temp2temp.Celsius.to_fahrenheit(n)
print('Sua temperatura em Fahrenheit é =={}ºF=='.format(f))
