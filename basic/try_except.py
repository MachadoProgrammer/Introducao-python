# Introduction: try except
# try - try to execute the code
# except - if there is an error, execute the code in except

try: 
    print(1/0)
except:
    print("An error occurred!")

# Empacotamento e Desempacotamento
# Packing and Unpacking
    
# tranformando uma lista em uma tupla: packing
dados = 1, 2, 3, 4

# unpacking
a, b, c, d = dados
print(a, b, c, d)

data = input('Digite os valores: ').split()
# a, b, c = ([int(i) for i in data])

# Programação mais funcional 
a, b, c = map(int, data) # map(funcao, iteravel) -> data = map(int, input('Digite os valores: ').split()) one line 
print(type(a), b, c)


# Args and Kwargs
# Args -> arguments
# Kwargs -> keyword arguments
# Args -> *args -> unpacking 
datas = [1, 2, 3, 4, 5]
print(datas)
print(*datas) # the * unpacks the list 

# partial unpacking
a, *b, c = datas
print(a)
print(b)
print(c)

# packing and unpacking functions
# with dict **kwargs
def ats(a,b):
    print(f'a={a} b={b}')
d = {'a': 1, 'b': 2}
ats(**d)