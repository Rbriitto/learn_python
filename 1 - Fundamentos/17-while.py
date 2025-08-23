# Lista de filmes
moviesList = ["Titanic","The Godfather","Inception","Jurassic Park" ]

# 1 - iterando alores de uma lista de filme usando while
# index = 0
# print(len(moviesList))

# while index < len(moviesList):
#     print(moviesList[index])
#     index += 1

# 2 - Quando a condiçao for atendida o loop será encerrado
# index = 0
# while index < len(moviesList):
#     if (moviesList[index]=="Inception"):
#         break
#     print(moviesList[index])
#     index += 1

# 3 - Quando a condição for atendida, o loop vai para a proxima iteração
# index = 0
# while index < len(moviesList):
#     if (moviesList[index]=="Inception"):
#         index +=1
#         continue
#     print(moviesList[index])
#     index += 1

# 4 - Avaliaçao do filme com while
movieName = input("Digite o nome do filme: ")
movieRating = int(input("Digite quantas avaliações deseja fazer: "))
total = 0
count = 0

while count < movieRating:
    note = float(input("Informe a nota do filme: "))
    total += note
    count +=1

if movieRating > 0 :
    average = total / movieRating
else:
    average = 0

print(f"Média de avaliação do filme {movieName} é: {average:.2f}")
