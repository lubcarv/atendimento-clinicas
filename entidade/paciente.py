from entidade.pessoa import Pessoa
from datetime import date

class Paciente(Pessoa):
    def __init__(self, nome: str, celular: str, cpf:str, data_nascimento: date):
        super().__init__(nome, celular, cpf, data_nascimento)