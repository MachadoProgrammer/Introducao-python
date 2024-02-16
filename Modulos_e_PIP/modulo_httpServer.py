# Simula um servidor HTTP 

# Método GET -> para obter informações
# Método POST -> para enviar informações
# Método PUT -> para atualizar informações
# Método DELETE -> para deletar informações

# MODULO WEBBROWSER
# O módulo webbrowser permite que seu programa abra páginas da web em um navegador da web.
# Este módulo funciona tanto para sistemas Windows quanto para sistemas Unix.

import webbrowser

done = False
while not done:
  print("O que você deseja fazer?")
  print("1. Aprender python")
  print("2. Aprender Java")
  print("3. Aprender JavaScript")
  print("4. Sair")
  
  escolha = input("Digite o número da opção desejada: ")
  
  if escolha == "1":
    webbrowser.open("https://www.python.org/")
  elif escolha == "2":
    webbrowser.open("https://www.java.com/")
  elif escolha == "3":
    webbrowser.open("https://www.javascript.com/")
  elif escolha == "4":
    done = True
  else:
    print("Opção inválida")
    
  
