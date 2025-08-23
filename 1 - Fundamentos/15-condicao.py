# # Informações sobre o filme

# name = input("Digite o nome do filme:\n")
# yearRelease = int(input("Informe o ano de lançamento:\n"))
# rating = float(input("Digite a nota de avaliação do filme:\n"))

# # Verifica se o filme é recomendado
# if rating > 8.0 and yearRelease > 2015 :
#     print(f"O filme {name} é muito bom. Recomendo assisti-lo.")
# else:
#     print(f"O filme {name} ainda nao atingiu uma boa nota.")

num1 = float(input("valor 1:"))
num2 = float(input("valor 2:"))

operation = input("digite a operação:(+ - x / ): ")

if(operation == "+" ):
    result = num1 + num2
elif operation == "-":
      result = num1 - num2
elif operation == "x":
      result = num1 * num2 
elif operation == "/":
      if num2 !=0:
        result = num1 * num2      
      else:
           print("Erro: não divisivel por 0 (zero)") 
           result = 0
                                                 
else:
      print("Operaçao Inválida")
      result = 0

print(f"o resultado de {num1} {operation} {num2} é: {result:.2f}")       
