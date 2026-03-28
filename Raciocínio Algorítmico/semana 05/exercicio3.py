numero = float(input("Digite um número: "))
counter = 0
total = 0

while numero != -1:
    total += numero
    counter += 1
    numero = float(input("Digite um número: "))

print("A média dos números digitados é ->", total / counter)