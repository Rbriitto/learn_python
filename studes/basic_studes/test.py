inteiros = [5,7,2]

print(inteiros)
print(inteiros[:1])


total = sum(inteiros)
print(total)


prod1 = input("Informe o produto: ")
valor1 = float(input("Informe o valor: "))
prod2 = input("Informe o produto: ")
valor2 = float(input("Informe o valor: "))
prod3 = input("Informe o produto: ")
valor3 = float(input("Informe o valor: "))

# Agora cada produto tem como valor diretamente o preço (float)
mercadoria = {
    prod1: valor1,
    prod2: valor2,
    prod3: valor3
}

print(mercadoria)

mais_caro = max(mercadoria, key=mercadoria.get)
print(mais_caro)

media = sum(mercadoria.values()) / len(mercadoria)
print(f"{media:.2f}")
