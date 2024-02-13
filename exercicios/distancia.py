passageiroDistancia = float(input("Digite a distância que o passageiro deseja pecorrer: "))
if passageiroDistancia <= 200: 
    precoKmh = 0.5
    preco = passageiroDistancia * precoKmh
    print(f"O preço da corrida é {preco}")
else:
    precoKmhExtra = 0.45  
    precoKmh = 0.5 + precoKmhExtra
    preco = passageiroDistancia * precoKmh  
    print(f"O preço da corrida é {preco}")