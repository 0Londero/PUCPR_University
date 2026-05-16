vetor = []

print("Digite dez números para armazenar:  ")
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

print(vetor)
print("O maior número digitado foi: ", max(vetor))
print("A posição do maior número é: ", vetor.index(max(vetor)))
