usuario = input("Digite o nome do usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "123":
    print("Acesso concedido.")
else:    
    print("Acesso restrito.")