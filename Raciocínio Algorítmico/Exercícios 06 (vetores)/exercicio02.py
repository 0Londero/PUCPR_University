valores = []

print("Digite seis valores inteiros para armazenar:  ")

for i in range(6):
    valor = int(input(f" Digite o {i+1}º valor -->     "))
    valores.append(valor)

print(f" Os valores armazenado são:  {valores}")