filmsList = ["Inception","The Shawwshank redemption",
            "The Dark knight","Pulp Fiction", "Interstellar"]

#1 - tamanho da lista

print(len(filmsList))

#2 - Recuperar um item da lista pelo nome
print(filmsList.index("Interstellar"))

# 3 - Adicionar item ao final da lista
filmsList.append("The Lord of The Rings")
print(filmsList)

#4 - Ordernar a Lista
filmsList.sort()
print(filmsList)

#5 - Copiar os itens de uma lista para outra
filmsCopy = filmsList.copy()
filmsCopy.remove("Pulp Fiction")
print(filmsCopy)

#6 - Remove todos os filmes
filmsList.clear()
print(filmsList)