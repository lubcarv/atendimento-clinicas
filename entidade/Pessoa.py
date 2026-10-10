from abc import ABC, abstractmethod
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome: str, celular: str, cpf: str, data_nascimento: date):
        if not isinstance(nome, str):
            raise TypeError('O nome precisa estar em formato de string')
        
        if not isinstance(celular, str):
            raise TypeError('O celular precisa estar em formato de string')
        
        if not isinstance(cpf, str):
            raise TypeError('O cpf precisa estar em formato de string')
        
        if not isinstance(data_nascimento, date):
            raise TypeError('A data de nascimento precisa estar em formato de date')

        self.__nome = nome
        self.__celular = celular
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento

    @property
    @abstractmethod
    def nome(self):
        return self.__nome

    @nome.setter
    @abstractmethod
    def nome(self, nome):
        if not isinstance(nome, str):
            raise TypeError('Nome precisa ser uma string')
        self.__nome = nome

    @property
    @abstractmethod
    def celular(self):
        return self.__celular

    @celular.setter
    @abstractmethod
    def celular(self, celular):
        if not isinstance(celular, str):
            raise TypeError('Celular precisa ser uma string')
        self.__celular = celular

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        cpf = cpf.replace('-', '').replace('.', '')
        
        if not isinstance(cpf, str):
            raise TypeError('CPF precisa ser uma string')
        
        if len(cpf) != 11:
            raise ValueError('O código deve ter exatamente 9 caracteres')
        
        self.__cpf = cpf

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        return data_nascimento

    def idade(self, data_referencia: date) -> int:
        if not isinstance(data_referencia, date):
            raise TypeError('A data de referência tem de ser tipo date')
        if data_referencia < self.__data_nascimento:
            raise ValueError('A data de referência não pode ser anterior ao nascimento')

        # Determina a idade da pessoa em anos.
        idade = data_referencia.year - self.data_nascimento

        # Serve para verificar se o aniversário já passou
        aniversario = (data_referencia.month, data_referencia.day) >= (self.__data_nascimento.month, self.__data_nascimento.day)

        if not aniversario:
            idade -= 1

        return idade

    def maior_de_idade(self, data_referencia: date) -> bool:
        if not isinstance(data_referencia, date):
            raise TypeError('A referência de data tem de estar em formato date')
        idade = data_referencia.year - self.data_nascimento
        if idade >= 18:
            return True
        return False