#Importar o arquivo Pessoa.py do diretório model
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

#Exemplo de uso
poyatos = Pessoa(1, "Henrique Poyatos")
print(poyatos)

#Chamar só nome
print(poyatos.nome)

print("DAQUI PRA FRENTE É ACESSO AO BANCO: ")

#Chamar o objeto do banco de dados
db = Database()

#Instancia o objeto
pessoaDAO = PessoaDAO(db.conexao, db.cursor)

#Carregar lista com info do banco de dados, trocar de (False) para (True)
pessoas = pessoaDAO.getAll(False)
for pessoa in pessoas:
  print(pessoa)


#Criar um objeto com qualquer ator/atriz/diretor/diretora
novo = Pessoa(0, "Denzel Washington")

#Olha que simples...
novo = pessoaDAO.save(novo)

#Consulta banco de novo
pessoas = pessoaDAO.getAll(False)
for pessoa in pessoas:
  print(pessoa)  