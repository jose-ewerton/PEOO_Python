from revista import Revista
from edicao import Edicao

revista1 = Revista('00001','Compre o Curso','mineração','#10',)
edicao1 = Edicao('70','12/02/22','45')
revista1.add_revista(edicao1)
revista1.listar_edicoes()