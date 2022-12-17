# Importa nosso arquivo Pessoa.py no diretório model/
from model.Pessoa import Pessoa
# precisa importar o Database e o PessoaDAO
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

# Instanciando um objeto do tipo Pessoa no Python...
poyatos = Pessoa(1, "Henrique Poyatos")
#O atributo está privado..aqui dá erro..
#print(poyatos.__nome)
print(poyatos)

# a partir de agora, vamos para o acesso a banco..
print("ACESSO A BANCO....")

#Chama o objeto de banco de dados
db = Database()

#Instancia um objeto do tipo PessoaDAO
pessoaDAO = PessoaDAO(db.conexao, db.cursor)

#Quero exibir na tela todos os atores, atrizes e diretores(as) do banco...
pessoas = pessoaDAO.getAll()

for pessoa in pessoas:
  print(pessoa)
  



