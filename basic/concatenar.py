name = input("What is your name? ")
yearLaunch = int(input("What year did you launch your company? "))
gamePrice = float(input("How much does your game cost? "))


# formatação de string com f-string para concatenar variáveis.

print(f"Nome: {name} - {type(name)} Ano de lançamento: {yearLaunch} - {type(yearLaunch)} Preço do jogo: {gamePrice} - {type(gamePrice)}")