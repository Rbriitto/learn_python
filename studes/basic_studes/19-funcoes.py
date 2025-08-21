# cria com uma palavra reservada chamada def

# 1 - Função para imprimir uma mensagem 
def welcome():
    print("Bem vindo ao sistema de filmes!")

# for i in range (10):
#     welcome()

# 2 - Função para calcular a média de notas
# def calculate_average():
#     num_ratings = int(input("Informe quantas avaliações deseja fazer: "))
#     total = 0
#     for i in range (num_ratings):
#         note = float(input("Digite a nota para o filme: "))
#         total += note
    

#     if num_ratings > 0 :
#         average = total / num_ratings
#     else:
#         average = 0

#     return average

# print(f"A média de avaliações é: {calculate_average():.2f}")
                    

# 3 - Cadastrar um filme
def create_movie():
    name = input("Nome do filme: ")
    yearLaunch = int(input("Ano de lançamento: "))
    moviePrice = float(input("Informe o preço do filme: "))
    rating = float(input("Digite a nota do filme: "))
    print(f"{name}({yearLaunch}) - R${moviePrice:.2f}")

create_movie()
create_movie()

