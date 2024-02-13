# List comprehension is a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.

# List values from o to 10 that be lower than 4
# for i in range(10):
#     if i < 4:
#         print(i)  # 0, 1, 2, 3

# List comprehension
# [expression for item in iterable if condition == True]
listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)  # returns in a list: [0, 1, 2, 3]

gameList = ["Star Wars", "The Matrix", "F1 2023", "God Of War"]
# only the games that have more than 10 characters
new_list = [game for game in gameList if len(game) > 7]
print(new_list)  # returns in a list: ['Star Wars', 'The Matrix']

new_list2 = [x for x in gameList if "a" in x]
print(new_list2)  # returns in a list: ['Star Wars', 'The Matrix', 'F1 2023']


# TODOS OS PRODUTOS ACIMA DE 1000, IMPOSTO DE 50% SOBRE O VALOR TOTAL
lista_precos = [500, 1500, 2000, 100, 25]

produtos_com_imposto = [(preco * 0.5) + preco for preco in lista_precos if preco > 1000]
print(produtos_com_imposto)  # returns in a list: [750.0, 1000.0]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# first_col = [row[0] for row in matrix]
# print(first_col)  # returns in a list: [1, 4, 7]


for i, row in enumerate(matrix):
    print(f'{row[i]} ', end='')
