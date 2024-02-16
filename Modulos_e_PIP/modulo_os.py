# MODULO OS
# O módulo os fornece uma maneira de usar funcionalidades dependentes do sistema operacional.
import os

# Consultar as funções disponíveis no módulo os
# help('os')

# Retonar o diretório atual
print(f'O diretória atual é: {os.getcwd()}')

# Listar arquivos e diretórios
print(f'Os arquivos e diretórios são: {os.listdir()}')

# Vesão do SO
print(os.uname())

# Limpar tela
# os.system('clear')