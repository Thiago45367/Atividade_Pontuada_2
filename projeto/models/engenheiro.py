import os
from models.abstract.funcionario import Funcionario

class Engenheiro():
    def __init__(self, crea: str) -> None:
        self.crea = crea

    def __str__(self) -> str:
         f"\nCREA: {self.crea}"