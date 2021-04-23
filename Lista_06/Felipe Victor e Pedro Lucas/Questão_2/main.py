from revista import Revista
from edição import Edicao

revista1 = Revista('01','Adiquira o Curso','espanhol','#2000',)
edicao1 = Edicao('69','20/02/29','24')
revista1.adc_revista(edicao1)
revista1.listar()