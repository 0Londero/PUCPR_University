import datetime
mes_atual = datetime.datetime.now().month

idade = int(input("Digite a idade: "))
mes_nascimento = int(input("Digite o mês de nascimento (1-12): "))

idade_mes = idade * 12 + (mes_atual - mes_nascimento)
print(f"A idade em meses é: {idade_mes} meses")