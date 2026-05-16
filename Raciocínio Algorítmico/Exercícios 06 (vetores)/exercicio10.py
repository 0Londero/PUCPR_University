vetor = []
print('Digite cinco valores para armazenar:  ')



for i in range(5):
    valor = int(input(f"Digite o {i+1}º valor: "))
    vetor.append(valor)

print("Os valores digitados foram: ", vetor)
print("o maior valor é : ", max(vetor))
print("O menor valor é: ", min(vetor))
print("A média dos valores digitados é: ", sum(vetor) / len(vetor))