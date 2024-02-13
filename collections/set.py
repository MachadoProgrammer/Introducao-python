# CONJUTNOS - SETS


# Armazena valores únicos e não ordenados
# Não aceita valores duplicados, criado para suportar operações matemáticas -> {}
# É possivel adcionar mas não é possivel alterar os valores

nomes = {'João', 'Maria', 'José', 'Ana', 'Maria'}
print(type(nomes)) 

# Converter uma lista em um conjunto
numbers = [1, 2, 3, 4, 5, 5, 5, 5, 5]
print(set(numbers))

#  Removw X discard 

#  Remove -> se não encontrar o valor, retorna um erro
# Isto é uma gambiarra
try:
  nomes.remove('Machado')
  print(nomes)
except:
  pass

#  Discard -> se não encontrar o valor, não retorna erro
nomes.discard('Machado')
print(nomes)

# SUBCONJUNTO

a = {1, 2, 3,}
b = {1, 2, 7}
print(a | b) # união -> union() -> 

print(a & b) # interseção -> intersection() -> valores que estão em ambos os conjuntos

print(a - b) # diferença -> difference() -> valores que estão em a mas não estão em b

print(a ^ b) # diferença simétrica -> symmetric_difference() -> valores que estão em a ou b mas não em ambos

# CASO PRECISE CRIAR UM CONJUNTO IMUTÁVEL, UTILIZE FROZENSET()