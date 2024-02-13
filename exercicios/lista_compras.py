import os

lista = []

while True:
  print('Selecione uma opção: ')
  opcao = input('[A]dicionar item\n[R]emover item\n[L]istar itens\n[S]air\n')
  if opcao == 'A':
    os.system('clear')
    valor = input('Digite o valor: ')
    lista.append(valor)
  elif opcao == 'R':
    indice_str = input('Digite o índice do item que deseja remover: ')

    try:
      indice = int(indice_str)
      del lista[indice]
    except:
      print('Digite um número válido')
    
  elif opcao == 'L':
    # os.system('clear')

    if len(lista) == 0:
      print('Lista vazia')
    for i, v in enumerate(lista):
      print(i, v)

  elif opcao == 'S':
    break
  else:
    print('Opção inválida')
    continue
  os.system('clear')