# Funcão anonima

# Função e potencia de um numero , recebe sempre uma variavel

power = lambda num: num ** 2
print(power(5))



# Função que verifica se um numero é par 

eh_par = lambda x: x % 2 == 0 
print(eh_par(27))
print(eh_par(30))

# Função que divide um numero por outro 
div_num = lambda x, y: x / y
print(div_num(10,2))
print(div_num(66,2))

# Função que inverte um string

reverse_string = lambda s : s[::-1]
print(reverse_string("Python"))
print(reverse_string("JavaScript"))


# Funcionalidaes relacionaas aos filmes:

movies_list = ["Titanic", "The GodFather","Inception","Jurassic Park","Matrix"]
ratings = {
    "Titanic":[7.0,9.0,5.5],
    "The GodFather":[5.0,7.0,9.5],
    "Inception":[9.0,9.5,5.9],
    "Jurassic Park":[7.0,7.0,7.5],
    "Matrix":[9.3,9.7,5.2],
}

      
# Função para calcular a média e avaliações e um filme

avaliacao = lambda movie_name: sum(ratings[movie_name])/ len(ratings[movie_name])

print(f"Média de avaliação o filme Matrix: {avaliacao("Matrix"):.2f}")

# Função que verifica se um filme esta na lista 

check_movie = lambda movie_name: movie_name in movies_list
print(f"Inception está na lista ? {check_movie("Inception")}")

# Função para recomendar o filme com base na avaliação média
recomendar = lambda movie_name: f"Recomendo assistir {movie_name} com média de {avaliacao(movie_name):.2f}"
print(f"{recomendar("Titanic")}")