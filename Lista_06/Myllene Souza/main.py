from Pessoa_3 import Pessoa
from Endereco import Endereco

e1 = Endereco ( "N" "22", "Maria Augusta", "Ceará-mirim","Rn", "Brasil")
e2 = Endereco ( "23", "Capitão da Penha", "Natal","Rn", "Brasil")
e3 = Endereco ( "24", "São José", "Massaranbuba","Rn", "Brasil")
e4 = Endereco ( "25", "Rafael Rodriguis", "Ceará-mirim","Rn", "Brasil")
#e.endereco_detalar ()

p= Pessoa ("Juremisvaldo", "000.000.000-00", e1,e2,e3,e4) 
p.detalhar_pessoa ()

