vetor = []
quantnegativos = 0
somapositivos = 0


print("Digite dez números reais para armazenar:  ")
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)
    if numero < 0:
        quantnegativos += 1
    else:
        somapositivos += numero

print(vetor)
print("A quantidade de números negativos digitados foi: ", quantnegativos)
print("A soma dos números positivos digitados foi: ", somapositivos)
