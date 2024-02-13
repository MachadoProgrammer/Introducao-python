# tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# Tuples are written with round brackets.
# if there is only one it will be considered a string, so it is necessary to put a comma at the end of the value.
#  nao precisa colocar os parentess para criar uma tupla

gamesTuple = ('FIFA', 'PES', 'GTA', 'Minecraft', 'Fortnite')
name = ('Leonardo')
print(type(name))
print(gamesTuple)
print(type(gamesTuple))

# Cannot add value to a tuple append()
# Cannot remove value from a tuple remove()
# Cannor order value from a tuple sort()

# Recover the first two items from the tuple
print(gamesTuple[:2])

# Recover the last two items from the tuple
print(gamesTuple[-2:])

# Recover games till a specific position 
print(gamesTuple[:3])
print(gamesTuple[2::])

# Recover a item by index
print(gamesTuple.index('Minecraft'))

listaJogos = "fifa", "pes", "gta", "minecraft", "fortnite"
print(listaJogos[-1]) 