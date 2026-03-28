counter = 0
impar = 0
par = 0

numero = float(input("Digite um número: "))

while counter < 10:
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
    counter += 1
    numero = float(input("Digite um número: "))

print("Quantidade de números pares ->", par)
print("Quantidade de números ímpares ->", impar)
