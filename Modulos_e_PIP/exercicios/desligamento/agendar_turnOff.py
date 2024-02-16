import os

# Agendar desligamento

#  No macOS e no Linux, você pode usar o comando shutdown para agendar o desligamento do computador.
#  O comando shutdown é usado para desligar ou reiniciar o computador.
#  Ele também pode ser usado para agendar o desligamento do computador.
#  O comando shutdown é um comando de terminal e deve ser executado como root.
#  O comando shutdown pode ser usado com várias opções.
#  Aqui estão algumas opções comuns:
#  -h: Desligar o computador.
#  -r: Reiniciar o computador.
#  -c: Cancelar o desligamento ou reinicialização.
#  -s: Agendar o desligamento.
#  -k: Enviar uma mensagem de desligamento.
#  -t: Tempo para desligamento ou reinicialização.
#  Aqui estão alguns exemplos de como usar o comando shutdown:
#  sudo shutdown -h now # desligar o computador
#  sudo shutdown -r now # reiniciar o computador
#  sudo shutdown -c # cancelar o desligamento ou reinicialização
#  sudo shutdown -s +{time} # agendar desligamento


# sudo shutdown -s +{time} # agendar desligamento
# sudo shutdown -k now # cancelar desligamento



# def agendar_desligamento():
#     tempo = int(input('Digite o tempo para desligamento em minutos: '))
#     os.system(f'sudo shutdown -s +{tempo}')

# def cancelar_desligamento():
#     comando('sudo shutdown -k now')


# def comando(cmd):
#     os.system(cmd)

# done = False
# while not done:
#     print('1 - Agendar desligamento')
#     print('2 - Cancelar desligamento')
#     print('3 - Sair')
#     opcao = int(input('Digite a opção desejada: '))
#     if opcao == 1:
#         agendar_desligamento()
#     elif opcao == 2:
#         cancelar_desligamento()
#     elif opcao == 3:
#         done = True
#     else:
#         print('Opção inválida!')