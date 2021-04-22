from Pessoa import Endereco, Pessoa

local=Endereco(34,"Manoel","Pureza", "RN","Brasil")
local2=Endereco(55,"Nova Descoberta", "Pureza","RN","Brasil")
pessoa=Pessoa(123,"Ana",5738372)
pessoa.adicionar_endereco(local)
pessoa.adicionar_endereco(local2)
pessoa.apresentar()
pessoa.remover_local(34)
pessoa.apresentar()