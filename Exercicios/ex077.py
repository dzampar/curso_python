a = ('batata','cenoura','tomate','brocoles','nabo','alface','repolho','abobrinha','pepino')
for memoria in a:
    print(f'\nAs vogais da palavra {memoria} são:',end=' ')
    for letra in memoria:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')