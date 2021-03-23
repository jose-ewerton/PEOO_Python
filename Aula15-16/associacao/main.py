from classes import Animais, Gato, Cachorro, Vaca

a = Animais()
gato = Gato()
cachorro = Cachorro()
vaca = Vaca()

#  objetos diferentes de classes diferentes
#print(a, gato, cachorro, vaca) 



a.animal = gato #dessa forma eu estou fazendo a associação do objeto gato com o animal

#métodos privados!!?
print(gato.bicho_que_e())  #não é relacionamento é apenas o chamado do metodo desse objeto
print(a.animal.bicho_que_e())
print(a.animal.som_que_faz())
print("Novo atributo para o Animal")


a.animal = cachorro
print(a.animal.bicho_que_e())
print(a.animal.som_que_faz())
print("Novo atributo para o Animal")


a.animal = vaca
print(a.animal.bicho_que_e())
print(a.animal.som_que_faz())


del a
print(gato,cachorro,vaca)
#print(a) erro notdefined

