name = 'fifffa 23'

# print(name.capitalize().replace('f', '$').lower())

name = input("Digite o nome do jogo: ")
char = input("Digite o caractere que deseja substituir: ")
newChar = input("Digite o novo caractere: ")
print(name.replace(char, newChar))

print("=" * 25)

name = input("Digite o nome do jogo: ")
char = name[0].lower()
new_game = name.replace(char, '$')
new_game = char + new_game[1:]
print(new_game)






