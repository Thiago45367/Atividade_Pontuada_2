import os
from models.abstract.Fisica import Fisica

class Cliente():
    def __init__(self, protocoloAtendimento: int) -> None:
        self.protocoloAtendimento = protocoloAtendimento

    def __str__(self) -> str:
         f"\nProtocolo de Atendimento: {self.protocoloAtendimento}"