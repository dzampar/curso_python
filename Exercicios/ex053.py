frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junta = ''.join(palavras)
#inverso = ''
inverso = junta[::-1]
#for letra in range(len(junta) -1, -1, -1):
    #inverso = inverso + junta[letra]
if inverso == junta:
    print('A palavra "{}" é a mesma lida de traz pra frente, "{}"\n'
          'Temos uma PALINDROMO'.format(junta,inverso))
else:
    print('A palavra "{}" não é a mesma lida de traz pra frente, "{}"\n'
          'Assim NÂO temos uma PALINDROMO'.format(junta,inverso))