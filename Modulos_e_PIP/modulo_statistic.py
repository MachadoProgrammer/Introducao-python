import statistics
# Serve para fazer cálculos estatísticos
# Média, mediana, moda, desvio padrão, entre outros
# DATA SCIENCE E MACHINE LEARNING - ESTATÍSTICA
# statstics model 

# Aplicar media

def media(lista):
    return statistics.mean(lista)
  
print(media([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Aplicar mediana

def mediana(lista):
    return statistics.median(lista)

print(mediana([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Aplicar moda

def moda(lista):
    return statistics.mode(lista)
  
print(moda([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Desvio padrão 
# O desvio padrão é uma medida de dispersão em torno da média populacional de uma variável aleatória.
# Quanto mais próximo de zero, mais homogêneo é o conjunto de dados.

def desvio_padrao(lista):
    return statistics.stdev(lista)
  
print(desvio_padrao([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))