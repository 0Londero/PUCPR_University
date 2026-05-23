matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor para a posição ({i}, {j}): "))
        linha.append(valor)
    matriz.append(linha)

print("Matriz:")
for linha in matriz:
    print(linha)

maior_valor = matriz[0][0]
linha_maior = 0
coluna_maior = 0

for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior_valor:
            maior_valor = matriz[i][j]
            linha_maior = i
            coluna_maior = j

print(f"O maior valor é {maior_valor} e está na posição ({linha_maior}, {coluna_maior})")