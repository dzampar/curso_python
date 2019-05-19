lista = ('Caderno', 2.50,'Lapis', 0.50,'Borracha',0.25,'Livros',11.50)
print('{:=^40}'.format('LISTA DE MATERIAIS'))
for memoria in range(0, len(lista),2):#guarde na memoria os itens da lista pulando de 2 e 2, repetindo de 0 ao tamanho da lista (len)
    print('{:.<30}R$ {:.2f}'.format(lista[memoria],lista[memoria+1]))#mostre os os itens da lista salva na memoria