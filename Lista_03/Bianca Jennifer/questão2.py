def contagem(valor):
    valor=str(valor)
    return len(valor)
v=int(input("digite algum valor: "))
print("quantidade de digitos do valor escolhido: ",contagem(v))
