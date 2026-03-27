# Se a temperatura for maior que 25, esta quente. Se estiver entre 18 e 24, esta amena. Abaixo de 18, esta frio.
temperatura = float(input("Digite a temperatura: "))

if temperatura > 25:
    print("Está quente.")
elif 18 <= temperatura <= 24:
    print("Está amena.")
else:    print("Está frio.")

