filmInception = {
    #propriedade : valor
    "title": "Inception",
    "yearRelease":2010,
    "imdbRating":9.9,
    "genre": ["Sci-fi", "Action", "Thriller"]

}

print(filmInception)
print(len(filmInception))
print(type(filmInception))

# 1 - Recuperar um Elemento do Dicionario
# passa a variavel e o valor que deseja dentro do colchetes
print(filmInception["genre"])
print(filmInception.get("imdbRating"))

# 2 - Buscar apenas as chaves do dicionario
print(filmInception.keys())

# 3 - Buscar apenas os valores do dicionario
print(filmInception.values())

# 4 - Buscar itens do dicionario com chave e valor
print(filmInception.items())

# 5 - Adicionar itens no dicionario
filmInception["director"] = "Christopher Nolan"
print(filmInception.items())

# 6 - Atualizar itens no dicionario
# passar a chave e 2qual item que quer atualizar

filmInception.update({"imdbRating":7.7})
print(filmInception.get("imdbRating"))

# 7 - Remover item no dicionario
filmInception.pop("director")
print(filmInception)