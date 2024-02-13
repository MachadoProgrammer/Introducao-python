# Lambda é uma função anônima que pode ter qualquer número de argumentos, mas apenas uma expressão.


# Função de Potência de número
power = lambda num: num ** 2

# Função de Par
pair = lambda num: num % 2 ==  0 # Par

# Função de Divisão
div1 = lambda num1, num2: num1 / num2

# Função que inverte uma string
invert = lambda string: string[::-1]

print(power(5))
print(pair(5))
print(div1(10, 2))
print(invert('Python'))
