import pytest
from projeto.models.advogado import Advogado

@pytest.fixture
def advogado_valido():
    advogado = Advogado("987654")
    return advogado

def test_oab_valido(advogado_valido):
    assert advogado_valido.oab == "987654"

def test_oab_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="Oab deve se manter como tipo texto."):
        Advogado(987654)    