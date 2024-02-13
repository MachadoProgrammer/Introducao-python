# descrição de varias linhas 
gameDescripiton = '''It's a race game when the first in place wins!!!'''


# Python é case sensitive 
# A forma que o texto é colocado, aparece no terminal.
print(gameDescripiton)

# Substrings a partir de uma string 
# slice de string, string[start:end:step] - index starts at 0, final index -1 
# step determine increment, by default is 1


# Como utilizar uma string e fatiamento e interpolação de strings
gameName = 'F1 2023'

#  Busque toda a string a partir do index 0
print(gameName[0:])

# Busque toda a string até a ultima posição
print(gameName[:])

# Busque toda a string a partir do index 0 até o index 1
print(gameName[0:2])

# busque a string de 2 em 2 
print(gameName[::2])

# Busque a string de trás para frente
print(gameName[::-1])




# Interpolação de strings
# s = 'string'  
# f = 'float'
# d e i = 'int'
# x e X = 'Hexadecimal'

# %s - string
# %f - float
# %d - int
# %x - hexadecimal

# be careful with the type of the variable
name = 'Machado'
preco = 199.987761
variable = '%s, o preço do produto é R$ %.2f ' % (name, preco)
print(variable)
print('O Hexadecimal de %d é %04x' % (15, 15))
print(f'{name!a}')

