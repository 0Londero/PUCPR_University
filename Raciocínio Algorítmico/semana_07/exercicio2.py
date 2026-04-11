while True:
    inteiro = int(input("Digite um número inteiro positivo: "))
    if inteiro < 0:
        print("POSITIIVO!!!!!!!!!!!!!!")
    else:           
        break

soma = 0
for i in range (1, inteiro + 1):
    soma += i


print(f"A soma dos números inteiros de 1 a {inteiro} é: {soma}")
print(f"A expressão aritmética é -> {' + '.join(str(i) for i in range(1, inteiro + 1))} = {soma}")