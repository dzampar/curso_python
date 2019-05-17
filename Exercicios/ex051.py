primeiro = int(input('PRIMEIRO TERMO:'))
razao = int(input('RAZÃO:'))
decimo = primeiro + (10 -1) * razao #decimo numero será o razao vezes 10, nesse caso 9 pq o Pyton conta o zero, mais o primeiro termo
for c in range (primeiro, decimo + razao, razao):#contagem a partir do primeiro termo terminando no decimo numero e pulando através da razão definida.
    #o decimo é somado a razão novamente para que o ultimo numero da contagem seja exibido, pois o Python não mosta o ultimo numero da contagem
    print(c,end='-> ')
print('ACABOU')

# uma outra maneira de fazer esse exercicio seria multiplicando por 10
#a razao, e na contagem informar somente o decimo, como sendo a contagem final

'''primeiro = int(input('PRIMEIRO TERMO:'))
razao = int(input('RAZÃO:'))
decimo = primeiro + 10 * razao  
for c in range (primeiro, decimo, razao):
    print(c,end='-> ')
print('ACABOU')'''