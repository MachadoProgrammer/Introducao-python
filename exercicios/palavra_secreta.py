palavra_secreta = 'banana'
letras_acertadas = ''
numero_tentativas = 0

# Limpar o terminal automatico
import os 

while True:
 letra_digitada = input('Digite uma letra: ')
 numero_tentativas += 1

 if len(letra_digitada) > 1:
    print('Digite apenas uma letra')
    continue

 if letra_digitada in palavra_secreta:
   letras_acertadas += letra_digitada  
 else:
  print('Tente novamente')

  # Para exibir a palavra de uma vez
  palavra_formada = ''
  for letra_secreta in palavra_secreta:
    if letra_secreta in letras_acertadas:
      palavra_formada += letra_secreta
    else:
      palavra_formada += '*'
  print('Palavra formada: ', palavra_formada)

  if palavra_formada == palavra_secreta:
    os.system('clear')
    print('Voê acertou')
    print('A palavra era: ', palavra_secreta)
    print('Número de tentativas: ', numero_tentativas)
    letras_acertadas = ''
    numero_tentativas = 0

