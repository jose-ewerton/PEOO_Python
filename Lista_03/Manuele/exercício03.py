'''Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve
haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a
informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para
efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um
loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as
vezes que desejar.
'''

def hora(H):
    if H > 12:
        H = H - 12
    return H


def saida(H, Min):
    H = str(H)
    Min = str(Min)
    print("São: ", H,"h", Min,"min")


while True:
    print("\n**** Notação Horária ****")
    H = int(input("Digite as horas:"))
    Min = int(input("Digite os minutos:"))
    saida(hora(H), Min)


    sair = input("Digite s para sair:")
    if sair == 's' or sair == 'S':
        break
