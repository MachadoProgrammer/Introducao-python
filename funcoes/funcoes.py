
# Função para somar
def sum(a, b):
    return a + b
print(sum(2, 2))

# Função para cadastrar um usuário
def cadastrar_usuario():
    name = input('Digite seu nome: ')
    age = int(input('Digite sua idade: '))
    print(f'{name} tem {age} anos')
cadastrar_usuario()

# Função com argumentos 
def user_info(name, age):
    print(f'{name} tem {age} anos')

user_info('João', 25)

# Função com argumentos por default
def address(country='Brazil'):
    print(f'I am from {country}')
address()

# Se o segundo argumento for nomeado o que vem depois também deve ser
# TUDO NOMEADO OU NÃO NOMEADO

#  Cadastro de jogo
def rating_game(qtdRating):
    game_name = input('Digite o nome do jogo: ')
    sum = 0
    for i in range(qtdRating):
        rating = float(input(f'Digite a nota {i+1}: '))
        sum += rating
    print(f'A média do jogo {game_name} é {sum/qtdRating}')
ratingNote = int(input('Digite a quantidade de notas: '))
rating_game(ratingNote)
