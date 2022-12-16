# Importa nosso arquivo Pessoa.py no diretório model/
from model.Pessoa import Pessoa

# Instanciando um objeto do tipo Pessoa no Python...
poyatos = Pessoa(1, "Henrique Poyatos")
#O atributo está privado..aqui dá erro..
#print(poyatos.__nome)
print(poyatos)



