# List, dict, funções, laço de repetição etc...


def count_upper_lowerString(string):
  # global letras_maiusculas
  # global letras_minusculas
  letras_maiusculas = 0
  letras_minusculas = 0
  for letra in string:
    if letra.isupper():
      letras_maiusculas += 1
    elif letra.islower():
      letras_minusculas += 1
  print(f'Quantidade de letras maiúsculas: {letras_maiusculas}')
  print(f'Quantidade de letras minúsculas: {letras_minusculas}')
count_upper_lowerString('Giovanna Silva de Oliveira Machado')