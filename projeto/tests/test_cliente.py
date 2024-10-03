import pytest
from projeto.models.cliente import Cliente

@pytest.fixture
def cliente_valido():
    cliente = Cliente(87092)
    return cliente

def test_protocolo_de_atendimento_valido(cliente_valido):
    assert cliente_valido.protocoloatendimento == 87092

def test_protocolo_de_atendimento_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O protocolo de atendimento deve conter números inteiros!"):
        Cliente("87092")    