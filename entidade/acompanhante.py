from datetime import date
from entidade import Pessoa


class Acompanhante(Pessoa):

    def __init__(self, nome: str, celular: str, cpf: str, data_nascimento: date):
        super().__init__(nome, celular, cpf, data_nascimento)