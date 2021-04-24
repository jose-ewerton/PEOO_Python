def soma(*valores):
    """"def soma função de somar todos os valores que a pessoa desejar."""
    return sum(valores)

def porcentagem(valor):
    """"def porcentagem retorna o valor inicial somado com 50% desse valor"""
    return (valor*50)/100+valor

def concatenar(*valores):
    """vai concatenar as strings que a pessoa digitar."""
    resultado=""
    for elemento in valores:
        resultado+=elemento
    return resultado

def chave_valor(**sequencia):
    """vai apresentar a ultima chave e seu elemento guardado de um dicionario."""
    lista=0
    for k,v in sequencia.items():
        lista=k,v
    return lista
if __name__=="__main__":
    print("teste 1")
    valor1=float(input("digite algum valor: "))
    valor2=float(input("digite algum valor: "))
    valor3=float(input("digite algum valor: "))
    print("resultado da soma: ",soma(valor1,valor2,valor3))

    print("teste 2")
    numero=float(input("digite um valor: "))
    print("resultado da soma do valor digitado mais 50%: ",porcentagem(numero))

    print("teste 3")
    string1=input("digite qualquer palavra: ")
    string2=input("digite qualquer palavra: ")
    string3=input("digite qualquer palavra: ")
    print("resultado ao concatenar tudo o que foi digitado antes: ",concatenar(string1,string2,string3))

    print("teste 4")
    nome1=input("digite um nome: ")
    nome2=input("digite um nome: ")
    nome3=input("digite um nome: ")
    print("nome da chave e o elemento dentro dela: ",chave_valor(chave01=nome1, chave02=nome2, chave03=nome3))
