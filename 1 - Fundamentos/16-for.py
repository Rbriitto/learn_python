moviesList = ["Titanic","The Godfather","Inception","Jurassic Park" ]

# 1 - Iterando valores de uma lista
# para cada filme na lista de filmes 
print("\n1.")
for movie in moviesList:
    print(movie) 

# 2 - Quando a codição for atendida o loop será encerrado
print("\n2.")
for movie in moviesList:
    if  movie == "Inception" :
        break
    print(movie)


# 3 - Quando a condiçao for atendida, o loop vai para a proxima iteração
print("\n3.")
for movie in moviesList:
    if movie == "Inception":
        continue
    print(movie)

# 4 - Avaliação do filme:
print("\n4.")
movieName = input("Digite o nome do filme: ")
movieRating = int(input("Digite quantas avaliações deseja fazer: "))

total = 0

for i in range (movieRating):
    note = float(input("Digite a nota para o filme: \n"))
    total += note

if movieRating > 0 :
    average = total / movieRating
else:
    average = 0

print(f"Média de avaliação do filme {movieName} é: {average:.2f}")