import pytest
from projeto.models.abstract.Pessoas import Pessoas

@pytest.fixture
def pessoas_valida():
    Pessoas = Pessoas("Carlinhos", 25, "71 9654832", "thyere@gmail.com", endereco(Endereco))
    return Pessoas



def test_pessoa_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Carlinhos"

def test_pessoa_idade_valido(pessoa_valida):
    assert pessoa_valida.idade == 25  


def test_pessoa_idade_menor_0_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="A idade não pode ser menor que 0"):
        Pessoas("Carlinhos", -1)        