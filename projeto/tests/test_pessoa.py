import pytest
from projeto.models.abstract.Pessoas import Pessoas
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def pessoas_valida():
    Pessoas = Pessoas("Carlinhos", 25, "71 9654832", "thyere@gmail.com", Endereco("Rua D", 6, "Casa Amarela, Portão Verde", "654331", "Salvador", UnidadeFederativa.SAO_PAULO))
    return Pessoas



def test_pessoa_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Carlinhos"

def test_pessoa_idade_valido(pessoa_valida):
    assert pessoa_valida.idade == 25

def test_pessoa_telefone_valido(pessoas_valida):
    assert pessoas_valida.telefone == "71 9654832" 

def test_pessoa_email_valido(pessoas_valida):
    assert pessoas_valida.email == "thyere@gmail.com"


def test_pessoa_idade_menor_0_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="A idade não pode ser menor que 0."):
        Pessoas("Carlinhos", -1, "71 9654832", "thyere@gmail.com", Endereco("Rua D", 6, "Casa Amarela, Portão Verde", "654331", "Salvador", UnidadeFederativa.SAO_PAULO))

def test_nome_vazio_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O nome não pode estar vazio."):
        Pessoas("", -1, "71 9654832", "thyere@gmail.com", Endereco("Rua D", 6, "Casa Amarela, Portão Verde", "654331", "Salvador", UnidadeFederativa.SAO_PAULO))

def test_telefone_pouco_numero_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O telefone não pode ter poucos números."):
        Pessoas("Carlinhos", 25, "71", "thyere@gmail.com", Endereco("Rua D", 6, "Casa Amarela, Portão Verde", "654331", "Salvador", UnidadeFederativa.SAO_PAULO))