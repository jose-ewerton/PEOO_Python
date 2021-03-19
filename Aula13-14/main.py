from editora import Editora
from livro import Livro

editora = Editora('1444','Editora JovemL TDA','jovemeditora@mail.com',"99999-9999")
livro = Livro('12345','Breve descrição sobre essa obra...','A mulher torta',editora)
livro.editora = editora
print(livro.descricao)
print(livro.editora.razao_social)
print(editora.razao_social)
