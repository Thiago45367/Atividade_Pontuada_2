import os
from models.abstract.funcionario import Funcionario

class Advogado():
    def __init__(self, oab: str) -> None:
        self.oab = oab

    def __str__(self) -> str:
         f"\nOAB: {self.oab}"