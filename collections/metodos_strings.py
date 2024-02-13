
gameName = 'Fifa 23'
gameDescripiton = '''It's a race game when the first in place wins!!!'''

print(gameName.upper()) # Transforma a string em maiuscula
print(gameName.lower()) # Transforma a string em minuscula
print(gameName.capitalize()) # Transforma a primeira letra da string em maiuscula
print(gameName.title()) # Transforma a primeira letra de cada palavra em maiuscula
print(gameName.center(10, '-')) # Centraliza a string em um espaço de 10 caracteres, preenchendo com '-'
print(gameName.find('23')) # Procura a string '23' e retorna o index da primeira letra
print(gameDescripiton.count('f')) # Conta quantas vezes a letra 'f' aparece na string
print(gameName.replace('Fifa', 'Pes')) # Substitui a palavra 'Fifa' por 'Pes' na string
print(gameName.lstrip()) # Remove espaços em branco no inicio da string
print(gameName.rstrip()) # Remove espaços em branco no fim da string


# split, join e strip

lista_palavras = gameDescripiton.split(' ')
print(lista_palavras)

new_list = [x for x in gameDescripiton if 'a' in x]
print(new_list)


# strip() remove espaços em branco no inicio e no fim da string
# melhor pratica é criar uma lista e depois usar o strip()
lista_frase = []
for i, frase in enumerate(lista_palavras):
    lista_frase.append(lista_palavras[i].strip())

# join 
frase = ''.join(lista_frase)
print(frase)

