vetor = []

print("Digite dez números para armazenar:  ")
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

print("O maior número digitado foi: ", max(vetor))
print("O menor número digitado foi: ", min(vetor))