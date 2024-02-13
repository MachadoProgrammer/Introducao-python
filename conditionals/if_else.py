# IF ELSE, Identação é importante

# in, not in, retorna true or false
# or, precisa de uma condição verdadeira
# and, precisa que todas as condições sejam verdadeiras
# not, inverte o valor da condição
# ==, comparação de igualdade
# !=, comparação de diferença
# >, maior que
# <, menor que
# >=, maior ou igual
# <=, menor ou igualX
    
numb1 = float(input("Insira o primeiro numero: "))
numb2 = float(input("Insira o primeiro numero: "))

valide_number = numb1 and numb2
if not valide_number:
    print("Número inválido")
    exit()

operation = input("Qual a operção a realizar ? (+ - *  / ) ")
if operation == "+": 
    result = numb1 + numb2
elif operation == "-": 
    result = numb1 - numb2
elif operation == "*":
    result = numb1 * numb2
elif operation == "/": 
    result = numb1 / numb2 
else: 
    print("Operação é inválida ")
    result = 0
print(f"Resultado é {result}")



entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = input('Digite a senha: ')
senha = '123456'

if entrada == 'E' and senha_digitada == senha:
    print('Acesso permitido')
else:
    print('Acesso negado')


# IF ELSE TERNÁRIO

# <valor> if <condição> else <outro valor>
    
digito = 9
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)