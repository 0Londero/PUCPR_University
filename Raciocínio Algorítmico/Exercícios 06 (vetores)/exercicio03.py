# ESSA É A VERSÃO MELHORADA DO EXERCÍCIO 03, POIS SÓ NO FINAL NOTEI QUE OS CONJUNTOS DEVEM TER UM LIMITE DE 10 ELEMENTOS.


i = float(input("Digite quantos números você deseja armazenar:  "))
numeros = []
nsquare = []


while i >= 0:
    i -= 1
    n = float(input("Digite um número: "))
    numeros.append(n)
    nsquare.append(n**2)


