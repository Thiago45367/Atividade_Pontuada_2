import os
from models.abstract.endereco import Endereco
from abc import ABC 

class Pessoas(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self) -> str:
        f"\nNome: {self.nome} \nTelefone: {self.telefone} \nEmail: {self.email} \nEndereco: {self.endereco}"            