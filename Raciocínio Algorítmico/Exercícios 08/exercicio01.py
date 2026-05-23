matriz = []
print(matriz)



for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input(f"Digite o valor para a posição ({i}, {j}): "))
        linha.append(valor)
    matriz.append(linha)


# Preenche com 0
for i in range(5):
    for j in range(5):
        matriz[i][j] = 0


# Diagonal principal com 1
for i in range(5):
    matriz[i][i] = 1

print(matriz)