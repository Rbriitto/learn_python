
filmsSet ={"Inception","The Shawwshank redemption",
            "The Dark knight","Pulp Fiction", "Interstellar"}

print(type(filmsSet))

print(len(filmsSet)) #1 - Busca o tamanho do set

exampleSet = {"Inception",True,1,9.0} #2 - True e 1 são considerados o mesmo valor
print(exampleSet)

filmsSet.update(exampleSet) #3 - Adicionar item de outro set
print(filmsSet)

# 4 - Remove um item no set
filmsSet.remove(True)
filmsSet.remove(9.0)
print(filmsSet)