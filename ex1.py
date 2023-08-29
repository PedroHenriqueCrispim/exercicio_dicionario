dicionarios_pessoas={}

for i in range(5):
    cpf = input("Digite o CPF da pessoa: ")
    nome = input("Digite o nome da pessoa: ")
    dicionarios_pessoas[cpf] = nome

print(dicionarios_pessoas)