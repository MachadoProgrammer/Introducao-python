# Fatorial de um número
# 3! = 3 * 2 * 1 = 6

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

number = int(input('Digite um número para o fatorial: '))
print(f'O fatorial de {number} é {factorial(number)}')


# Soma total de um número
def total_sum(num):
    if num == 1:
        return 1
    else:
        return num + total_sum(num - 1)
num = int(input('Digite um número para a soma total: '))
print(f'A soma total de {num} é {total_sum(num)}')

