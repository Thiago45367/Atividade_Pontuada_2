import os
from models.abstract.juridico import Juridico

class Fornecedor():
    def __init__(self, produto: str) -> None:
        self.produto = produto

    def __str__(self) -> str:
         f"\nProduto: {self.produto}"