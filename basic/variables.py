# Variables are used to store information to be referenced and manipulated in a computer program.
# Variables are created when first assigned a value.
# Variables must be assigned before being referenced.
# The value stored within a variable can be changed.
# Variables can be assigned to different data types.
# Variables can be reassigned to different memory locations.
# Numbers with a decimal point are called floating-point numbers (or floats).

name = "Star Wars: Episode IV - A New Hope"
yearLauch = 1977
director = "George Lucas"
budget = 11000000
bestFilm = True # Boolean

# Identifie the type of variable
print(type(name))
print(type(yearLauch))
print(type(director))
print(type(budget))
print(type(bestFilm))

# str, int, float, bool são dados imutáveis
# algumas vezes a resposta está na docmentação 

# Constant 
# A constant is a type of variable whose value cannot be changed.

velocidade = 61
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1 

if velocidade > RADAR_1: 
    print("Você foi multado!")

if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
    print("Você está na área de radar!")

# Métodos de str, number, bool
string = "Hello, World!"
number = 18
bollean = True
print(string) # com o '.' acessa métodos e propriedades 
print(number) # same 
print(bollean) # same 


print(string.zfill(20))
    

