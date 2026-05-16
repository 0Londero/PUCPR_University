vetor = []
par = 0
impar = 0

print("A seguir, você irá digitar 10 números para armazenar.")

for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1




