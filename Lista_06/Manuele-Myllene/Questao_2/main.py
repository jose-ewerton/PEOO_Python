from revista import Revista
from edicao import Edicao

e = Edicao("01","30/04/2020", "7")

r = Revista("1234", "Manu e Myllene", "Garotas inteligentes",e)
r.add_edicao("02","30/02/1986", "9")
r.add_edicao("03","05/02/1940", "8")

r.exibir_revista()





