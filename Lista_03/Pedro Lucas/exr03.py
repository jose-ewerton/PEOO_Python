def Converter(H,M):
    H = int(input("Que horas são?:"))

    M = int(input("E os minutos?:"))

    if H > 12:
        Resultado = (H - 12)
        print(Resultado, "H", M, "Min", "A.M.")
    elif H < 12:
        print(H, "H", M, "Min", "A.M.")
    elif H == 12:
        print(H, "H", M, "Min", "A.M.")
def Saida():
    i = 0
    while i <1:
        Converter(1,2)

Saida()

