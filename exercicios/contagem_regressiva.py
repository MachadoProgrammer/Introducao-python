# Contagem regressiva for e while

from time import sleep
for count in range(10, -1, -1):
    print(count)
    sleep(0.7)
print('Beep!')

# import winsound 
# for count in range(10, -1, -1):
#     print(count)
#     winsound.Beep(2500, 500)
# print('Beep!')'''

# import winsound 
# x = 10
# while x >= 0:
#   print(x)
#   x -= 1
# winsound.Beep(2500, 500)

# THERE IS NO WINDSOUND FOR MAC
i = 0
novo_nome = ''
nome = 'Machado'
while i < len(nome):
  letra = nome[i]
  novo_nome += f'*{letra}'
  i += 1

print(novo_nome)


 



          
      
    