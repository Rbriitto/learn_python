"""

"""

#1 - Fatorial de um numero 
def factorial(num):
    if num == 1:
        return 1 
    else:
        return (num * factorial (num - 1 ))

number = int(input("Informe o numero: "))
print(f"o Fatorial de {number} é {factorial(number)}")

# 2 - Soma total de um numero
def total_sum(num):
    if num == 1:
        return 1 
    else:
       return (num + total_sum (num - 1 ))
    
#number = int(input("Informe o numero: para soma "))
print(f"{number} é {total_sum(number)}")

