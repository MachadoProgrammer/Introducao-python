# Description: Dicionário aninhado
import pprint
gamesDict = {
    "Super Mario": {
        "release": 1985,
        "platforms": ["Nintendo Switch", "Wii", "Nintendo 64"]
        },
    "Star Wars": {
        "release": 2023,
        "platforms": ["PlayStation 5", "Xbox Series X", "PC"]
        },
    "Fifa 23": {
        "release": 2022,
        "platforms": ["PlayStation 4", "PlayStation 5", "Xbox One", "Xbox Series X", "PC"]
    }
}
# para imprimir um dicionário aninhado, é necessário utilizar a biblioteca pprint
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

# Acessar um valor de um dicionário aninhado
print(gamesDict["Super Mario"]["platforms"])

# Adicionar um valor a um dicionário aninhado
gamesDict["Super Mario"]["platforms"].append("Wii U")
print(gamesDict["Super Mario"]["platforms"])

# Remover um valor de um dicionário aninhado
del gamesDict["Super Mario"]
pp.pprint(gamesDict)


# E-mails de gerentes de loja

email_gerentes = {
  "Iguatemi": "iguatemi.@gmail.com",
  "Plaza": "plaza.@gmail.com",
  "Barra": "barra.@gmail.com",
}


# Qual o email do gerente do shopping Iguatemi ?
email = email_gerentes["Iguatemi"]
print(email)

# Adicionar um novo shopping e seu respectivo email
email_gerentes["Norte Shopping"] = "norte.@gmail.com"
print(email_gerentes) 

# Descobrir todos os shoppings
# Forma 1: fazer um for loop
for shopping in email_gerentes:
    print(shopping)

# Forma 2: dict.keys()
print(list(email_gerentes.keys()))

# Descobrir todos os emails
# Forma 1: fazer um for loop
for email in email_gerentes:
    print(email_gerentes[email])

# Forma 2: dict.values()
print(list(email_gerentes.values()))

# Descobrir todos os shoppings e emails
# Forma 1: fazer um for loop
for shopping, email in email_gerentes.items():
    print(f'{shopping}: {email}')


