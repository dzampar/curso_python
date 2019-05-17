print("Insira dois valores abaixo")
valor1 = float(input("Primeiro Valor:"))
valor2 = float(input("Segundo Valor:"))
opcao = 0
while opcao != 5:
    print('  [ 1 ]Somar\n'
          '  [ 2 ]Multiplicar\n'
          '  [ 3 ]Maior\n'
          '  [ 4 ]Novos numeros\n'
          '  [ 5 ]Sair')
    opcao = int(input(">>>>>Qual a sua opção?"))
    #if menu == 5:
     #  sair = 5
    if opcao == 1:
        soma = valor1 + valor2
        print("A soma entre {} + {} é {}\n"
              "===========================".format(valor1,valor2,soma))
    elif opcao == 2:
        multiplicar = valor1 * valor2
        print("A multiplicação entre {} x {} é {}\n"
              "===========================".format(valor1,valor2,multiplicar))
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
            print("O maior valor entre {} e {} é {}\n"
              "===========================".format(valor1,valor2,maior))
        if valor1 < valor2:
            maior = valor2
            print("O maior valor entre {} e {} é {}\n"
              "===========================".format(valor1,valor2,maior))
        if valor1 == valor2:
            print("Os valores {} e {} são iguais\n"
                  "=======================".format(valor1,valor2))
    elif opcao == 4:
        print("Insira os valores novamente")
        valor1 = float(input("Primeiro Valor:"))
        valor2 = float(input("Segundo Valor:"))
print("=-"*10)
print('Fim do programa, obrigado!!!')
print("=-"*10)
