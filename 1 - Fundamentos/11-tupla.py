# Nas tuplas nao tm algumas operações que tem na lista

filmsTuple =("Inception","The Shawwshank redemption",
            "The Dark knight","Pulp Fiction", "Interstellar")

print(type(filmsTuple))

# 1 - Buscar os dois primeiros itns da tupla

print(filmsTuple[:2])

# 2 - Buscar o ultimo item da tupla
print(filmsTuple[-1])

# 3 - Buscar filmes ate uma determinada posição
print(filmsTuple[:3])

# 4 - Buscar filmes de uma posição em diante
print(filmsTuple[2:])

# 5 - Recuperar um item a tupla pelo nomee
print(filmsTuple.index("Pulp Fiction"))