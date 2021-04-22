#Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exem-
#plo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve
#haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a
#informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para
#efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um
#loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

print('___________________________________________________')

def X(Y, Z):
    Y= int(input("Digite a hora desejada:"))
    Z= int(input("Agora digite os minutos desejados:"))
    if Y>12 and 23>=Y:
        Y= (Y-12)
        print('Foi convertida a',Y,Z,'PM')
        Y= "PM"
    else:
        print('Essa hora é AM')
        Y= "PM"
def XYZ():
    c = 0
    while c < 1:
        X(1,2)

XYZ()

print('___________________________________________________')