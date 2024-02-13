number = int(input("Digite um número: "))
begin = int(input("Digite o início da tabuada: "))
end = int(input("Digite o fim da tabuada: "))

x = begin 
# while x <= end:
#     print(f'{number} x {x} = {number * x}')
#     x += 1

for x in range(begin, end+1):
    print(f'{number} x {x} = {number * x}')


