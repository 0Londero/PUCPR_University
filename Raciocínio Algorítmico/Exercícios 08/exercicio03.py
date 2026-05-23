matriz = []
print("Digite os dados de 5 alunos conforme o enunciado abaixo:")
print("1ª coluna: número de matrícula")
print("2ª coluna: média das provas")
print("3ª coluna: média dos trabalhos")
print("4ª coluna: nota final (calculada como a soma das médias)")
for i in range(5):
    matricula = int(input(f"Aluno {i+1} - matrícula: "))
    media_provas = int(input(f"Aluno {i+1} - média das provas: "))
    media_trabalhos = int(input(f"Aluno {i+1} - média dos trabalhos: "))
    nota_final = media_provas + media_trabalhos
    linha = [matricula, media_provas, media_trabalhos, nota_final]
    matriz.append(linha)

maior_nota = -1
matricula_maior = -1
for linha in matriz:
    if linha[3] > maior_nota:
        maior_nota = linha[3]
        matricula_maior = linha[0]

print(f"Matrícula do aluno com maior nota final: {matricula_maior}")
