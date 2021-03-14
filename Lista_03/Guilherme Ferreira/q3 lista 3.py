def Converter(Hr,Mn):
	Hr = int(input("Que horas são:"))
	
	Mn = int(input("E os minutos:"))
	
	if Hr > 12:
		Resultado = (Hr - 12)
		print(Resultado, "H", Mn, "Min", "P.M.")
	elif Hr < 12:
		print(Hr, "H", Mn, "Min", "A.M.")
	elif Hr == 12:
		print(Hr, "H", Mn, "Min", "P.M.")
def Saida():
	cont = 0
	while cont <1:
		Converter(1,2)
		
Saida()
