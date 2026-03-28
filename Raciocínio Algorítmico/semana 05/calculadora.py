while True:
    print(r"""________ CALCULADORA ________
            1. Adição
            2. Subtração
            3. Multiplicação
            4. Divisão
            0. Sair                             """)
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 0:
        print("Encerrando a calculadora!")
        break
    elif opcao == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"O resultado da adição é: {resultado}")
    elif opcao == 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print(f"O resultado da subtração é: {resultado}")
    elif opcao == 3:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print(f"O resultado da multiplicação é: {resultado}")
    elif opcao == 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado da divisão é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")