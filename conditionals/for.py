gameList = ['CSGO', 'PUBG', 'FORTNITE', 'The Finals', 'LOL', 'GOD OF WAR']
# Interating through the list 
for game in gameList:
    print(game)
    print('---')
print('Done!')

# When the condition is met, the loop will stop
for game in gameList:
    if game == 'The Finals':
        break
    print(game) 

# When the condition is met, the loop will skip the current iteration
for game in gameList:
    # Skip the game 'The Finals'
    if game == 'The Finals':
        continue
    print(game)


# Using the range function
for x in range(0, 10):
    print(x)

# Using the range function with a step  
for x in range(0, 10, 2):
    print(x)
    


users = {'Hans': 23, 'Maria': 25, 'João': 30, 'Ana': 31}

for user, age in users.copy().items():
    if age < 29:
        del users[user]
print(users)

active_users = {}
for user, age in users.items():
    if age > 30:
        active_users[user] = age
print(active_users)

# ENUMERATE 
# Usamos quando queremos pegar o índice e o valor de uma lista ao mesmo tempo

#   Index, value = enumerate(list)
for i, game in enumerate(gameList):
    print(i, game)

# Para caso tenha duas listas e queremos iterar sobre elas ao mesmo tempo

vendendores = ['João', 'Maria', 'José']
vendas = [1000, 2000, 3000]

for vendendor, venda in zip(vendendores, vendas):
    print(vendendor, venda)

