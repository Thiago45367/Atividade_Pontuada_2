from enum import Enum

class Setor(Enum):
      ENGENHARIA = "Engenharia"
      SAUDE = "Saúde"
      JURIDICA = "Juridica"
      OPERACOES = "Operações"
      
      def __init__(self, nome: str, sigla : str) -> None:
        self.nome = nome
        self.sigla = sigla  