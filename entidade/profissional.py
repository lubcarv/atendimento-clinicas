from pessoa import Pessoa
from datetime import date

class Profissional(Pessoa):
    def __init__(self, nome: str, celular: str, cpf: str, data_nascimento: date, especialidade: str, registro_profissional: str):
        super.__init__(nome, celular, cpf, data_nascimento)

        if not isinstance(especialidade, str):
            raise TypeError('A especialidade precisa estar em formato de string')
        if not isinstance(registro_profissional, str):
            raise TypeError('O registro profissional precisa estar em formato de string')
        self.__especialidade = especialidade
        self.__registro_profissional = registro_profissional

    @property
    def especialidade(self) -> str:
        return self.__especialidade

    @especialidade.setter
    def especialidade(self, especialidade: str) -> None:
        if not isinstance(especialidade, str):
            raise TypeError('A especialidade precisa estar em formato de string')
        self.__especialidade = especialidade

    @property
    def registro_profissional(self) -> str:
        return self.__registro_profissional

    @registro_profissional.setter
    def registro_profissional(self, registro_profissional: str) -> None:
        if not isinstance(registro_profissional, str):
            raise TypeError('O registro profissional precisa estar em formato de string')
        self.__registro_profissional = registro_profissional
