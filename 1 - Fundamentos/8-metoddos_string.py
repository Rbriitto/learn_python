movieName = "Toooop Guuuun"

movieDescription = """ 
    TOP GUN é um filme de aviação e aventura
    muito consagrado na industria 
"""

print(movieName.upper()) # tudo maiusculo
print(movieName.lower()) # tudo maiusculo
print(movieName.capitalize()) # primeira letra maiuscula
print(movieName.title()) # primeira letra maiuscula
print(movieName.center(10, "-")) # retorna string centrazida com caracter de preenchimento
print(movieName.find("u"))# retorna a posiçao/indice do caracter
print(movieName.count("o"))# conta quantas letras tem
print(movieName.replace("Top","Matrix"))# Altera um elemento por outro
print(movieDescription.split(','))# Altera um elemento por outro