movieName = "Top Gun"

#string[inicio:fim]
# indice começa no 0 (zero)  vai ate o indice final 

# 1- Buscar toda string a partir da primira posição

print(movieName[0:])

# 2 - Buscar toda string até a ultima posição
print(movieName[:7])

# 3 - Buscar toda string da terceira até a ultima posição
print (movieName[2:])

"""
string [inicio:fim:passo]
índic começa na posição 0 | índice final - 1
passo - determina o incremento. por padrão ess número é o 1
"""

# 4 - Buscar toda a string e 2 em 2 caracteres
print (movieName[::2])

# 5 - Buscar todas a string nos índices impares
print(movieName[1::2])

# 6 - Inverter uma string de trás para frente
print(movieName[::-1])