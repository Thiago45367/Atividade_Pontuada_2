import pytest
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def endereco_valido():
    endereco = Endereco("Rua D", 6, "Casa Amarela, Portão Verde", "654331", "Salvador", UnidadeFederativa.SAO_PAULO)
    return endereco

def test_logradouro_valido(endereco_valido):
    assert endereco_valido.logradouro == "Rua D"

def test_numero_valido(endereco_valido):
    assert endereco_valido.numero == 6

def test_complemento_valido(endereco_valido):
    assert endereco_valido.complemento == "Casa Amarela, Portão Verde"

def test_cep_valido(endereco_valido):
    assert endereco_valido.cep == "654331"

def test_cidade_valido(endereco_valido):
    assert endereco_valido.cidade == "Salvador" 

def test_complemento_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O complemento deve se manter como tipo texto."):
        Endereco("Rua D", "6", 78, "1111", "Salvador", UnidadeFederativa.SAO_PAULO)

def test_logradouro_tipo_invalido_retorna_mesagem_erro():
    with pytest.raises(TypeError, match="O logradouro deve se manter como texto."):
        Endereco(93 , "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA)                          