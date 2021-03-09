Nome = str(input("atleta:"))

N = len(Nome)

if N > 1:
	p1 = float(input("1° salto:"))
	p2 = float(input("2° salto:"))
	p3 = float(input("3° salto:"))
	p4 = float(input("4° salto:"))
	p5 = float(input("5° salto:"))
	
	m = (p1 + p2 + p3 + p4 + p5)/5

	print("Resultado:")
	print("Nome do atleta:", Nome)
	print("Saltos:", p1, "-", p2, "-", p3, "-", p4, "-", p5)
	print("Media dos saltos: ",round(m,2), "m")
	
else:
	print("por favor digite o nome do atleta.")