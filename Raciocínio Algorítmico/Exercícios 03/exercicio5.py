coordenadax = int(input("Digite a coordenada x: "))
coordenaday = int(input("Digite a coordenada y: "))

if coordenadax < 0 and coordenadax > 10 or coordenaday > 0 and coordenaday > 10:
    print("Fora do plano")
elif coordenadax == 0 or coordenadax == 10 or coordenadax == 0 or coordenaday == 10:
    print("Na borda do plano")
else:
    print("Dentro do plano")
