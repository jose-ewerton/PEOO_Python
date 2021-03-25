from classes import Mamifero,Cachorro,Boi,Gato

print('----------CLASSE PAI------------')
m  = Mamifero("Porco",60)
print(m.nome,m.peso)
m.alimentacao_filhote()
print()

print('----------CLASSE FILHA SEM CONSTUTOR------------')
g = Gato()
print(g.nome,g.peso)
g.alimentacao_filhote()
g.alimentacao_adulta()
print()

print('----------CLASSE FILHA COM CONSTUTOR------------')
b = Boi("Boi",400)   
print(b.nome,b.peso,b.som)
b.alimentacao_filhote()
b.alimentacao_adulta()
print()

print('----------CLASSE FILHA COM CONSTUTOR------------')
c = Cachorro("Cachorro",30)
print(c.nome,c.peso,c.som)
c.alimentacao_filhote()
c.alimentacao_adulta()