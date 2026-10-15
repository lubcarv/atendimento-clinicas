from abc import ABC, abstractmethod
from datetime import date

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, celular: str, cpf: str, data_nascimento: date) -> None:
        self.nome = nome
        self.celular = celular
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome) -> None:
        if not isinstance(nome, str):
            raise TypeError('Nome precisa ser uma string')
        self.__nome = nome

    @property
    def celular(self) -> str:
        return self.__celular

    @celular.setter
    def celular(self, celular: str) -> None:
        if not isinstance(celular, str):
            raise TypeError('Celular precisa ser uma string')
        self.__celular = celular

    @property
    def cpf(self) -> None:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str) -> None:
        if not isinstance(cpf, str):
            raise TypeError('CPF precisa ser uma string')
        cpf = cpf.replace('-', '').replace('.', '')
        if not isinstance(cpf, str):
            raise ValueError('O CPF deve ter exatamente 11 dígitos')
        if not cpf.isdigit() or len(cpf) != 11:
            raise ValueError('O código deve ter exatamente 9 caracteres')
        
        self.__cpf = cpf

    @property
    def data_nascimento(self) -> date:
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date) -> None:
        if not isinstance(data_nascimento, date):
            raise TypeError('A data de nascimento precisa ser do tipo date')
        self.__data_nascimento = data_nascimento

    def idade(self, data_referencia: date) -> int:
        if not isinstance(data_referencia, date):
            raise TypeError('A data de referência tem de ser tipo date')
        if data_referencia < self.__data_nascimento:
            raise ValueError('A data de referência não pode ser anterior ao nascimento')

        # Determina a idade da pessoa em anos.
        idade = data_referencia.year - self.__data_nascimento.year

        # Serve para verificar se o aniversário já passou
        aniversario = (data_referencia.month, data_referencia.day) >= (self.__data_nascimento.month, self.__data_nascimento.day)

        if not aniversario:
            idade -= 1

        return idade

    def maior_de_idade(self, data_referencia: date) -> bool:
        if not isinstance(data_referencia, date):
            raise TypeError('A referência de data tem de estar em formato date')
        idade = data_referencia.year - self.__data_nascimento.year
        if (data_referencia.month, data_referencia.day) < (self.__data_nascimento.month, self.__data_nascimento.day):
            idade -= 1
        return idade >= 18