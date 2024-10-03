import os
from models.abstract.funcionario import Funcionario

class Medico():
    def __init__(self, crm: str) -> None:
        self.crea = crm

    def __str__(self) -> str:
         f"\nCRM: {self.crm}"