a = float(input("Digite o comprimento do lado A: "))
b = float(input("Digite o comprimento do lado B: "))
c = float(input("Digite o comprimento do lado C: "))


def valida_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return "É um triângulo"
    else:
        return "Não é um triângulo"
    
def tipo_triangulo(a, b, c):
    if a == b == c:
        return "Triângulo Equilátero"
    elif a == b or b == c or a == c:
        return "Triângulo Isósceles"
    else:
        return "Triângulo Escaleno"

def triangulo_retangulo(a, b, c):
    lados = sorted([a, b, c])
    if lados[0]**2 + lados[1]**2 == lados[2]**2:
        return "É um triângulo retângulo"
    else:
        return "Não é um triângulo retângulo"
    

    
if valida_triangulo(a, b, c) == "É um triângulo":
    print(tipo_triangulo(a, b, c))
    print(triangulo_retangulo(a, b, c))
else:
    print("Não é um triângulo")
