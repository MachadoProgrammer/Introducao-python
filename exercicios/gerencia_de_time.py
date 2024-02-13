times = {}

def incluir_time():
    indice = int(input('Digite a numeração do time: '))
    time = input('Digite o nome do time: ')
    qtdJogadores = int(input('Digite a quantidade de jogadores: '))
    if time in times:
        print('Time já cadastrado')
        print()
    else:
        times[time] = {
            'nome': time,
            'indice': indice,
            'qtdJogadores': qtdJogadores}

def listar_times():
    for k, v in times.items():
        print(f'{v["indice"]} - {k} - {v["qtdJogadores"]} jogadores')
    
    
def excluir_time():
    listar_times()
    time = input('Digite o nome do time que deseja excluir: ')
    if time in times:
        del times[time]
    else:
        print('Time não encontrado')

def menu():
    while True:
        print('Selecione uma opção: ')
        opcao = input('[I]ncluir time\n[L]istar times\n[E]xcluir time\n[S]air\n')
        if opcao == 'I':
            incluir_time()
        elif opcao == 'L':
            listar_times()
        elif opcao == 'E':
            excluir_time()
        elif opcao == 'S':
            break
        else:
            print('Opção inválida')
            continue

menu()
print('Fim do programa')