# minha resolução sem lista
expressao = str(input("Digite uma expressão matematica"))
a = expressao.count(')')
b = expressao.count('(')
while not a >= 1 and not b >= 1:
    print("Você não está colocando parenteses na sua expressão")
    expressao = str(input("Digite uma expressão matematica"))
    a = expressao.count(')')
    b = expressao.count('(')
if expressao.find(')') < expressao.find('(') or not a == b:
    print("Expressão não é valida, verifique sua expressão")
else:
    print("Expressão valida!!!")

# resolução do professor usando lista
'''expressao = str(input("Digite uma expressão matematica"))
pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print("Expressão valida!!!")
else:
    print("Expressão não é valida, verifique sua expressão")'''