#forma 1
#o usuario nn escolhe a quantidade de valores que deseja digitar.
def soma(*valores):
    global resultado
    global soma
    resultado=0
    soma=0
    resultado=len(valores)
    soma= sum(valores)
valor_1=float(input("digite um valor: "))
valor_2=float(input("digite um valor: "))
valor_3=float(input("digite um valor: "))
soma(valor_1,valor_2,valor_3)
print("resultado da soma dos valores: ",soma)
print("resultado da quantidade de valores: ",resultado)

#forma 2
def so(numeros):
    global quantidade
    quantidade=0
    quantidade=len(numeros)
    return sum(numeros)
lista=[]
c=0
while c==0:
    lista.append(float(input("digite algum valor: ")))
    pergunta=input("deseja parar(sim ou nao)? ").upper()
    if pergunta=="SIM":
        c+=1
print("resultado da soma dos valores escolhidos: ",so(lista))
print("resultado da quantidade de valores escolhidos: ",quantidade)



