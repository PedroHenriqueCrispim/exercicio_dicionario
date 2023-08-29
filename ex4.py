def contar_vogais(texto):
    vogais = "aeiou"
    contador = {}

    for char in texto:
        if char.lower() in vogais:
            if char.lower() in contador:
                contador[char.lower()] += 1
            else:
                contador[char.lower()] = 1
    
    return contador

texto = input("Digite o texto: ")
resultado = contar_vogais(texto)
print(resultado)