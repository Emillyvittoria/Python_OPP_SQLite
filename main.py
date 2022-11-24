#Importa nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa

#Exemplo de uso
emilly = Pessoa(1, "Emilly Vittória")
print(emilly)

#Quero mostrar só o nome
print(emilly.nome)