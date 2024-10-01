from enum import Enum

class UnidadeFederativa(Enum):
    BAHIA = "Bahia", "Ba"
    RIO_JANEIRO = "Rio De Janeiro", "R3"
    SAO_PAULO = "São Paulo", "SP"

    def __init__(self, nome: str, sigla : str) -> None:
        self.nome = nome
        self.sigla = sigla