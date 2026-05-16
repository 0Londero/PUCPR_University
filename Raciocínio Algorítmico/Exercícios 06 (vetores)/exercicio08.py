nota = []
print("Digite as 15 notas dos alunos:  ")
for i in range(15):
    n = float(input(f"Digite a {i+1}ª nota: "))
    nota.append(n)

print("A média geral das notas é de: ", sum(nota) / len(nota))