import os
from models.abstract.juridico import Juridico

class PrestacaoServico():
    def __init__(self, ContratoInicio: str, ContratoFim: str) -> None:
        self.ContratoInicio = ContratoInicio
        self.ContratoFim = ContratoFim

    def __str__(self) -> str:
         f"\nContrato Inicial: {self.ContratoInicio} \nContrato Final: {self.ContratoFim}"