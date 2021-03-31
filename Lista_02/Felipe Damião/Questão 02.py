i = []
a = str(input('Atleta: '))
h = ("")
if a == h:
    print('Programa encerrado. Motivo: O nome do atleta precisa ser inserido.')
else:
    print('')
    b = float(input('Primeiro salto(em metros): ')) 
    i.append(b)
    c = float(input('Segundo salto(em metros): '))
    i.append(c)
    d = float(input('Terceiro salto(em metros): '))
    i.append(d)
    e = float(input('Quarto salto(em metros): '))
    i.append(e)
    f = float(input('Quinto salto(em metros): '))
    i.append(f)

    print('')
    print('Resultado:')
    print('Atleta:', a)
    print('Saltos:',b,'-',c,'-',d,'-',e,'-',f)
    j = sum(i)
    print('Média dos saltos:',j/5)

