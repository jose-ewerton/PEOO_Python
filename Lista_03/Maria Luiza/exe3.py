"""Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros.
Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída.
Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para
efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um
loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as
vezes que desejar."""


def converter_hora(h, m):
    if 0 < h <= 12 and 0 < m < 60:
        print('\033[32m'f'{h}:{m} AM''\033[m')
    elif 12 < h < 24 and 0 < m < 60:
        print('\033[32m'f'{h - 12}:{m} PM''\033[m')
    else:
        print('\033[31m''Valor inválido''\033[m')



while True:
    print('=' * 42)
    print("CONVERTA A HORA DA NOTAÇÃO DE 24H PARA 12H")
    print('\033[7m'"(Para encerrar o programa digite '111')"'\033[m')
    print('=' * 42)

    h = int(input("Digite a hora (\033[32m__\033[m:00): "))
    if h == 111:
        break
    m = int(input(f"Digite os minutos ({h}:\033[32m__\033[m):"))
    converter_hora(h, m)