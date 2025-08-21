# 1 - Listar valores de 0 a 10 que sejam menores do que 4
# imprima o i onde o i está no range 
listNumbers = [i for i in range (10) if i < 4]
print(listNumbers)



filmes = [
    "O Poderoso Chefão",
    "Clube da Luta",
    "Interestelar",
    "Forrest Gump",
    "A Origem",
    "Matrix",
    "Gladiador",
    "Os Vingadores",
    "O Senhor dos Anéis: A Sociedade do Anel",
    "Vingadores: Ultimato",
    "Coringa",
    "Titanic",
    "Star Wars: Uma Nova Esperança",
    "Jurassic Park",
    "De Volta para o Futuro"
]
# 2 - Filmes que possuem a letra 'e' no título 
# moviesWithE = [movie for movie in filmes if 'e' in movie.lower()]
# print(moviesWithE)

moviesList = ["Titanic","The Godfather","Inception","Jurassic Park" ]
# 3 - Filmes que eu assisti
moviesWatched = [movie for movie in moviesList if movie != "Jurassic Park" ]
print(moviesWatched)

# 4 - Encontrando um filme pelo nome
while True:
    searchName = input("Informe o nome do filme para buscar na lista (ou sair para encerrar): ")
    if searchName.lower() == "sair":
        print("Tchau")
        break

    foundMovies = [movie for movie in moviesList if searchName.lower() in movie.lower()]
    if foundMovies:
        print(f"Filme(s) encontrado(s) com o nome: {searchName}: ")
        for foundMovie in foundMovies:
            print (foundMovie)
    else:
        print(f"Nenhum filme foi encontrado com o nome {searchName}. Tente novamente")
