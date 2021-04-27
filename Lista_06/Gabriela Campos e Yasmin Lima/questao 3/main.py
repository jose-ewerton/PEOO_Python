from pessoa import Endereco, Pessoa

local=Endereco(235,"Gabriela","Ceará-Mirim", "RN","Brasil")
local2=Endereco(23,"Cohab", "Ceará-Mirim","RN","Brasil")
pessoa=Pessoa(100,"Yasmin",10325467)
pessoa.adicionar_endereco(local)
pessoa.adicionar_endereco(local2)
pessoa.apresentar()
pessoa.remover_local(23)
pessoa.apresentar()
