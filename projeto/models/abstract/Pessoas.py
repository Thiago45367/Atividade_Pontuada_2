import os
from projeto.models.endereco import Endereco
from abc import ABC 

class Pessoas(ABC):
    def __init__(self, nome: str, idade : int, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.idade = self._verificar_idade(idade)
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        

    def _verificar_idade(self, valor):
        self._verificar_idade_menor_0(valor) 

        self.idade = valor
        return self.idade  

    def _verificar_idade_menor_0(self, valor):
        if valor < -1:
            raise ValueError("A idade não pode ser menor 0.")          