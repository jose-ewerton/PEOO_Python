def SOMA(soma):
    j = True
    while j == True:
        print('PARA FINALIZAR CLIQUE DUAS VEZES NO ENTER')
        soma = (float(input("Digite um número: ")))
        soma += soma
        print("A atual soma é", soma)


def ACRE(acre):
    a = True
    while a == True:
        print('PARA FINALIZAR CLIQUE DUAS VEZES NO ENTER')
        acre = float(input("Digite um número: "))
        acre = acre * 1.50
        print("Com o acrescimo ficou ", acre)

def cona(*strings):
    print("Adicione um texto na sua importação.")
    co = ""
    for str in strings:
        co += " " + str
    return co
