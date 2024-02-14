# O módulo serve para organizar o código em arquivos separados e reutilizáveis.
# Um módulo com maior manutenibilidade e legibilidade.

# MODULO DE CALCULO (+, -, *, /)

# Para importar o módulo, basta usar o import

# Importa o módulo inteiro
import calc 

# Importa apenas a função divisao
from calc import divisao

print(calc.soma(10,2))
print(calc.subtracao(10,2))
print(calc.multiplicacao(10,2))
print(calc.divisao(10,2))

print(divisao(10,5))