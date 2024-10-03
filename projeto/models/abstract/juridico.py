import os
from models.abstract.Pessoas import Pessoas
from abc import ABC

class Juridico(Pessoas, ABC):
     def __init__(self, cnpj: str, inscricaoEstadual: str) -> None:
         self.cnpj = cnpj
         self.inscricaoEstadual = inscricaoEstadual

     def __str__(self) -> str:
          f"\nCNPJ: {self.cnpj}, \nInscricaoEstadual: {self.inscricaoEstadual}"    