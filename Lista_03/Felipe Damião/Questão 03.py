def Converter(H,M):
    h = int(input('Que horas são: '))
    m = int(input('E os minutos: '))

    resultado = (h-12)
    
    if h>12:
        print(resultado,'H',m,'Min','P.M.')
    elif h<12:
        print(resultado,'H',m,'Min','P.M.')
    elif h==12:
        print(resultado,'H',m,'Min','P.M.')

def Saida():
    i=0
    while i<1:
        Converter(1,2)

Saida()
