"""
*args - Utilizamos ele quando não temos certeza de quantos argumentos queremos ter numa função
    - argumentos passados como uma tupla

**kwargs - Alem dos valores podemos pássar tamem as respectivas chaves para cada argumento.
- Os argumentos são passados como um dicionario 


"""

# 1 - Soma de numeros 

def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma é: {sum_total}")

sum(7,9,122,11,1)

# 2 - Apresentação de cursos 
def presentation (**data):
    for key, value in data.items():
        print(f"{key} - {value}")

print("Lista e cursos: ")
presentation(name="Python", category="Backend", level="Iniciante\n")
presentation(name="Visao computacional com Python", category="IA", level="Avançado\n")
presentation(name="Dashboard com dash", category="Data Science", level="Intermediário")


