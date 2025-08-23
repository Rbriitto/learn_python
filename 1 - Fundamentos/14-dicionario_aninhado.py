import pprint




filmsDict = {
    "inception":{
    "yearRelease":2010,
    "imdbRating":9.9,
    "genre": ["Sci-fi", "Action", "Thriller"]
    },
    "matrix":{
    "yearRelease":2000,
    "imdbRating":9.1,
    "genre": ["Sci-fi", "Action","lalala"]

    },
    "Os Incriveis":{
    "yearRelease":2007,
    "imdbRating":5.1,
    "genre": ["Animation" "Action"]

    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)

# 1 - Uscar uma informaçao dentro de um dicionario aninhado
print(filmsDict["matrix"]["genre"])

# 2 - Adicionar uma nova variavel 
filmsDict["inception"]["director"]= "nolan" 

print(filmsDict["inception"])

# 3 - Exclusão 
del filmsDict ["matrix"]
pp.pprint(filmsDict)