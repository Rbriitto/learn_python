# 1 - Funcão para imprimir um nome completo

# def full_name(first_name, last_name):
#     print(f"Nome é: {first_name} {last_name}")

# full_name("Rodrigo","Britto")

# 2 - Função para somar 2 numeros
# def soma(a, b):
#     return a + b

# print(f"{soma(10,50)}")   

# 3 - Função com parametro default
# def address(country="Brazil"):
#     print(f"Eu moro em {country}")

# address()

# 4 - Funçao para avaliar um filme
def rate_movie(num_ratings, movie_name):
    total = 0
    for i in range(num_ratings):
        note = float(input("Digite a nota para o filme: "))
        total += note

    if num_ratings > 0 :
        average = total / num_ratings
    else:
        average = 0

    print(f"Média e avaliação o filme: {movie_name} é : {average:.1f}")

rate_movie(2,"Sonic") 

