id = []
comentario = []
i = 0

while i < 15:
    print ("Para seu comentario use 5 para ótimo, 3 para bom e 1 para regular.")
    id.append (int (input ("Diga sua idade:")))
    comentario.append (int (input ("Diga seu comentario:")))
    i += 1

total = sum (id)

print ("A média da idade dos participantes foi de", total / len (id))

P = []
N = []
for cont in comentario:
    if ((cont % 2 != 0) and (cont == 1)):
        N.append (cont)
    if (cont % 2 == 0):
           p.append (cont)

print (list (id))
print (list (comentario))

P = (len (p) / 15) * 100
print ("O numero de pessoas que responderam regular foi", len (N))
print (round (P), "% que votaram bom.")
