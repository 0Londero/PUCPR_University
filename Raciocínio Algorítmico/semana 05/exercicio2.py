soma = 0

print("______ SOMA DE NÚMEROS INTEIROS ______")
new_number = int(input("Digite um número inteiro: "))


while new_number <= 0:
    print("Número inválido! Digite um número inteiro maior que zero (0).")
    new_number = int(input("Digite um novo número inteiro: "))

soma += new_number

while True:
    new_number = int(input("Digite um outro número inteiro: "))
    
    if new_number > 0:
        soma += new_number
        print("A soma atual é ->", soma)
    else:
        print("Número inválido! Ignorado.")

    if input("Deseja continuar? (s/n): ").lower() != 's':
        break

print("A soma de TODAS as iterações é:", soma)