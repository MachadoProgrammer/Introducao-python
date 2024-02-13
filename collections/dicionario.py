# Não pode ser confudido com o set, no set apenas tem a chave e no dicionário tem chave e valor

gameFifa = {
    "nome": "Fifa 23",
    "desenvolvedora": "EA Sports",
    "ano": 2022,
    "price": 299.99,
    "plataformas": ["PlayStation 4", "PlayStation 5", "Xbox One", "Xbox Series X", "PC"]
} 
print(gameFifa)
print(len(gameFifa))
print(gameFifa["plataformas"][::1])

# Recover a element from a dictionary
print(gameFifa["nome"])
# get(), tenta recuperar um valor, se não existir, retorna None
print(gameFifa.get("ano", None))

# Recover the keys from a dictionary
print(gameFifa.keys())

# Recover the values from a dictionary
print(gameFifa.values())

# Recover the items from a dictionary tuple format
print(gameFifa.items())

# Add a new item to the dictionary
gameFifa["classificacao"] = "Livre"
print(gameFifa)

# update a item from the dictionary
gameFifa.update({"price": 399.99})
print(gameFifa)

# Remove a item from the dictionary
gameFifa.pop("classificacao")
print(gameFifa)

