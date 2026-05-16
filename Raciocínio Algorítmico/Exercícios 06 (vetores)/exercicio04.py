vetor = []
print("A seguit, você irá digitar 8 números para armazenar.")

for i in range(8):
    numero = float(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

print(f"A lista é {vetor}")
print("Quais posições você deseja somar? (Entre 0 e 7)")

pos1 = int(input("Digite a primeira posição: "))
pos2 = int(input("Digite a segunda posição: "))

soma = vetor[pos1] + vetor[pos2]
print(f"A soma dos números nas posições {pos1} e {pos2} é: {soma}")

# Não coloquei nenhuhma validação, espero que o usuário digite apenas números e posições válidas.