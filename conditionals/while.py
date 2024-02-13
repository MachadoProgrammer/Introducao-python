gameName = input('Enter the name of the game: ')
qtdRating = 0
totalRating = 0
rating = 0
average = 0

while(rating != -1):
    rating = float(input('Enter the rating of the game: '))
    # condição para sair do loop
    if rating == -1:
        # break para sair do loop 
        break
    qtdRating += 1
    totalRating += rating
    average = totalRating / qtdRating
print(f'The average note of the game {gameName} is {average:.2f}')

# Qual letra aparece mais vezes na frase?
frase = 'O python é uma linguagem multiparadigma'
i = 0
apareceu_mais_vezes = 0
letra_mais_apareceu = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qts_vezes_letra = frase.count(letra_atual)

    if apareceu_mais_vezes < qts_vezes_letra:
        apareceu_mais_vezes = qts_vezes_letra
        letra_mais_apareceu = letra_atual

    i += 1

print(f'A letra que mais apareceu foi {letra_mais_apareceu} com {apareceu_mais_vezes} vezes')