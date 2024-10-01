import os
from models.enums.setor import Setor
from abc import ABC, abstractclassmethod

class Funcionario(ABC):
    def __init__(self, cpf: str, rg: str, matricula: str, setor: Setor, salario: float) -> None:
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = salario


    def calcular_bonus(self) -> float:
        pass

    def __str__(self) -> str:
        return f"Funcionário(Matrícula: {self.matricula}, Setor: {self.setor}, Salário: R${self.salario:.2f})"