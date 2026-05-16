vetor = []

print ("Digite cinco valores para armazenar:  ")
for i in range(5):
    valor = int(input(f"Digite o {i+1}º valor: "))
    vetor.append(valor)

print (" O menor valor está em posição: ", vetor.index(min(vetor)))
print (" O maior valor está em posição: ", vetor.index(max(vetor)))