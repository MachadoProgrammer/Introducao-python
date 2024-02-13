import os

teams = {}
done = False


# Função para listar os times 
def listar_times():
  print("Times cadastrados:\n")
  for i, team in enumerate(teams.values()):
    print(f"{i+1}. {team['name']} ({len(team['players'])}) jogadores")


# Função para listar jogadores de um time
def listar_team_players(team):
  print(f'Jogadores do {team['name']}')
  for i, player in enumerate(team['players']):
    print(f'{i+1}. {player}')

# teams{
#      "team_name": {
#       "name": team_name,
#       "players": [] }
#  
# }

# team_name = list(teams.keys()[team_num - 1])
  # Primeiro, criar-se uma lista de chaves do dict(teams) que são os nomes dos times
    # Em seguida, usa-se o número do time(team_num) - 1, pois foi adicionado + 1 na interação com enumerate(), assim
    # obtem-se o time correspodente 

    # Em alguns casos, pode ser necessário obter uma cópia da lista de chaves do dicionário, e não apenas uma visualização. Usar a função list() é uma forma de garantir que a lista seja uma nova cópia e não uma referência à estrutura original do dicionário.
        
    # Além disso, se o dicionário for alterado durante o processo de iteração, pode ocorrer um erro. Por exemplo, se a chave for removida durante a iteração, o loop pode tentar acessar uma chave que não existe mais. Ao usar list(teams.keys()), estamos criando uma lista independente da estrutura do dicionário original, evitando esse tipo de problema.

while not done:
  # OPÇÕES NO PROGRAMA
  print('O que você deseja fazer ? ')
  print("1. Adicionar um time")
  print("2. Remover um time")
  print("3. Listar os times cadastrados")
  print("4. Adicionar jogador em um time")
  print("5. Remover um jogador de um time")
  print("6. Lista jogadores de um time")
  print("7. Sair")

  choice = input(">\n")

  if choice == "1":

    os.system('clear')
    team_name = input("Digite o nome do time: ")
    teams[team_name] = {'name': team_name, 'players': [] }
    print('Time cadastrado')

  elif choice == "2":

    os.system('clear')
    # lISTAR OS TIMES, E REMOVER O ESCOLHIDO
    listar_times()
    team_num = int(input("Informe o número do time que deseja remover:\n"))
    if team_num <= len(teams):
  
      team_name = list(teams.keys())[team_num - 1]
      print(team_name)
      del teams[team_name]
      print('Time Removido')
    else:
      print("Número inválido")

  elif choice == "3":
    os.system('clear')
    listar_times()

  elif choice == "4":
    os.system('clear')

    listar_times()
    team_num = int(input("Informe o número do time que deseja adicionar o jogador\n"))
    if team_num <= len(teams):
      team_name = list(teams.keys())[team_num - 1]
      player_name = input("Informe o nome do jogador:\n")
      teams[team_name]['players'].append(player_name)
      print("Jogador adicionado ao time escolhido")
    else:
      print("O número do time está inválido")

  elif choice == "5":

    os.system('clear')
    listar_times()
    team_num = int(input("Informe o número do time que deseja adicionar o jogador\n"))
    if team_num <= len(teams):
      team_name = list(teams.keys())[team_num - 1]
      listar_team_players(teams[team_name])
      player_num = int(input("Informe p número do jogador que deseja remover:\n"))
      if player_num <= len(teams[team_name]['players']):
        del teams[team_name]['players'][player_num - 1]
        print("Jogador removido do time")
      else:
        print("Número inválido")
    else:
      print("Número do time inválido")

  elif choice == "6":

    os.system('clear')
    listar_times()
    team_num = int(input("Informe o número do time que deseja adicionar o jogador\n"))
    if team_num <= len(teams):
      team_name = list(teams.keys())[team_num - 1]
      listar_team_players(teams[team_name])
    else:
      print("Número do time inválido")

  elif choice == "7":
    os.system('clear')
    done = True 
  else:
    print("Opção inválida")



print(teams)








    