while True:
    def nun(numero):
        numero = str (numero)
        return len (numero)
    n = int(input("Informe um número: "))
    print("Você digitou o {} e ele tem {} digitos.".format(n, nun(n)))
    print(20*"=")
    cont = (input("Deseja continuar? s/n "))
    if cont != "s": break
