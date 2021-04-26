def Converter(hr,mn):
	mr = int(input("hora: "))
	
	mn = int(input("minutos: "))
	
	if hr > 12:
		Resultado = (hr - 12)
		print(Resultado, "H", mn, "Min", "P.M.")
	elif hr < 12:
		print(hr, "H", mn, "Min", "A.M.")
	elif hr == 12:
		print(hr, "H", mn, "Min", "P.M.")
def Saida():
	cont = 0
	while cont <1:
		Converter(1,2)
		
Saida()
