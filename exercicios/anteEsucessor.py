num = input("Digite um número: ")
num = int(num)
print(f"O antecessor de {num} é {num - 1} e o sucessor é {num + 1}")

# The input() function is used to get input from the user.
# The input() function will return a string.
# The int() function is used to convert a number or string into an integer.
# The f-string is used to format the output.

# Media de 4 notas

num1 = int(input('Primeria nota: '))
num2 = int(input('Secunda nota: '))
num3 = int(input('Terceira nota: '))
num4 = int(input('Quarta nota: '))

sumMedia = num1 + num2 + num3 + num4
print(f'A média das notas é {sumMedia/ 4}')