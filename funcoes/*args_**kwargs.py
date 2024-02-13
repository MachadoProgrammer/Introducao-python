# *Args - Utilizamos quando não sabemos quantos argumentos serão passados para a função

# **Kwargs - Além dos valores, podemos passar também as respectivas chaves para cada argumento
# Os argumentos são passados como um dicionário


# Função para somar
def sum(*num):
    total = 0
    for i in num:
        total += i
    return total
print(f'A soma total é {sum(1, 2, 3, 4, 5)}')
    

# Apresentação de cursos com **kwargs
def show_courses(**data):
    for key, value in data.items():
        print(f'{key} = {value}')

# Passando valores como dict
show_courses(name='Python', duration='3 months', price=1000.00)


# Desempcotamento em chamadas, de métodos e funções

lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
for nome in lista:
    print(f'{nome}', end=' ')

print('-' * 20)

salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda']
]

print(*salas, sep='\n')