# list are used to store multiple items in a single variable.
# list are created using square brackets.
# list are ordered, changeable and allow duplicate values.
# usable knowledge: index and slicing
# useful methods: append(), remove(), pop(), insert(), clear(), copy(), count(), extend(), index(), reverse(), sort()
# convert some list to a list: list()
# its better to take out the last item of a list using pop() method
#  CRUD - Create, Read, Update, Delete
#         Criar, Ler, Atualizar, Deletar = lista[i] (CRUD)

# Create a list
thisList = ["F1 2023", 2023, "Star Wars", 2022,  "The Matrix", 2005, [ "The Matrix", "Star Wars"]]
print(thisList)

# Access items
print(thisList[:2])
# Access the last item
print(thisList[-1][1])
# Acess the second onwwards item
print(thisList[1:4])


# copy() para nao alterar a lista original

lista = ['Maria', 'João', 'Ana', 'José']
for i in lista:
  print(lista.index(i), i)


# enumerate() para pegar o index e o valor
lista_enumerada = (enumerate(lista))

for i, v in lista_enumerada:
  print(i, v)


# \t para dar um tab
# \n para dar uma quebra de linha
# \r para dar um retorno de carro
# \b para dar um backspace
# \f para dar um form feed
  
# lista dentro de uma lista 
  for movie in thisList:
    print(f'O filme é {movie}')
    if type(movie) == list:
      for i in movie:
        print(f'O filme é {i}')