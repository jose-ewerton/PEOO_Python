def converter(hrs,mins):
    hrs = int(input("que horas são: "))
    mins = int(input("quantos minutos: "))

    if hrs > 12:
        result = (hrs - 12)
        print(result, mins, "p.m")
    elif hrs < 12:
        print(result, mins, "a.m")
    elif hrs == 12:
        print(result, mins, "p.m")
def saida():
    cont = 0
    while cont < 1:
    	converter(1,2)

saida()
