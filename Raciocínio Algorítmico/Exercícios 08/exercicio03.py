matriz = []
for i in range(5):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição ({i}, {j}): "))
        linha.append(valor)
    nota_final = linha[1] + linha[2]
    linha.append(nota_final)
    matriz.append(linha)

maior_nota = -1
matricula_maior = -1
for linha in matriz:
    if linha[3] > maior_nota:
        maior_nota = linha[3]
        matricula_maior = linha[0]

print(f"Matrícula do aluno com maior nota final: {matricula_maior}")
