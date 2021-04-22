'''Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exem-
plo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve

haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a
informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para
efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um
loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as
vezes que desejar.'''


def converter(h, m):
    h = int(input("Que horas sao? "))
    m = int(input("E quantos minutos? "))

    if h > 12:
        resultado = (h - 12)
        print(resultado, "h", m, "min", "P.M.")

    elif h < 12:
        print(h, "h", m, "min", "A.M.")

    elif h == 12:
        print(h, "h", m, "min", "P.M.")

def saida():
    i = 0
    while i < 1:
        converter(1, 2)

saida()