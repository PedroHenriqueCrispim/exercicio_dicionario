dicionarios_produto={}

for i in range(5):
    nome_produto = input("Digite o nome do produto: ")
    preço = float(input("Digite o preco do produto: "))
    if preço<50:
        print('O preço deve ser superior a 50 reais')
    else:
        dicionarios_produto[nome_produto] = preço

print(dicionarios_produto)