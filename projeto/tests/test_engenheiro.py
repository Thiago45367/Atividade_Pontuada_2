import pytest
from projeto.models.engenheiro import Engenheiro

@pytest.fixture
def engenheiro_valido():
    engenheiro = Engenheiro()