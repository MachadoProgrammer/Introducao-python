# Problemas com ponto flutuantes
# 3 Solutions to avoid problems with floating point numbers
# In case you need to work with floating point numbers, you can use the following solutions to avoid problems with floating point numbers:
# Need to be precuse 

# Final result formatted to 2 decimal places
numero_1 = 0.1
numero_2 = 0.2
resultado = numero_1 + numero_2
print(f'{resultado:.2f}')

# Using the round() function
print(round(resultado, 2))

# Using the decimal module
# Last case 
from decimal import Decimal

numero_1 = Decimal('0.1')
numero_2 = Decimal('0.2')
resultado = numero_1 + numero_2
print(resultado)


# Random numbers
import random
aleatorio = random.randint(0,9)
print(f'O numero é {aleatorio}')