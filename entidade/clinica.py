from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import time
from entidade.profissional import Profissional

if TYPE_CHECKING:
    from entidade.atendimento import Atendimento

class Clinica:
    def __init__(self, codigo: str, nome: str, localizacao: str, descricao: str, horario_abertura: time, 
                 horario_fechamento: time) -> None:
        self.codigo = codigo
        self.nome = nome
        self.localizacao = localizacao
        self.descricao = descricao
        self.profissionais = []
        
        if not isinstance(horario_abertura, time):
            raise TypeError('O horário de abertura precisa estar em formato time')
        if horario_abertura >= horario_fechamento:
            raise ValueError('O horário de abertura precisa ser menor que o horário de fechamento')
        self.__horario_abertura = horario_abertura
        self.__horario_fechamento = horario_fechamento

    @property
    def codigo(self) -> str:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: str) -> None:
        if not isinstance(codigo, str):
            raise TypeError('O código precisa ser tipo string')
        self.__codigo = codigo

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        if not isinstance(nome, str):
            raise TypeError('O nome precisa ser tipo string')
        self.__nome = nome

    @property
    def localizacao(self) -> str:
        return self.__localizacao

    @localizacao.setter
    def localizacao(self, localizacao: str) -> None:
        if not isinstance(localizacao, str):
            raise TypeError('A localização precisa ser tipo string')
        self.__localizacao = localizacao

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str) -> None:
        if not isinstance(descricao, str):
            raise TypeError('A descrição precisa ser tipo string')
        self.__descricao = descricao

    @property
    def horario_abertura(self) -> time:
        return self.__horario_abertura

    @horario_abertura.setter
    def horario_abertura(self, horario_abertura: time) -> None:
        if not isinstance(horario_abertura, time):
            raise TypeError('O horário de abertura precisa estar em formato time')
        if horario_abertura >= self.__horario_fechamento:
            raise ValueError('O horário de abertura precisa ser menor que o horário de fechamento')
        self.__horario_abertura = horario_abertura

    @property
    def horario_fechamento(self) -> time:
        return self.__horario_fechamento

    @horario_fechamento.setter
    def horario_fechamento(self, horario_fechamento: time) -> None:
        if not isinstance(horario_fechamento, time):
            raise TypeError('O horário de abertura precisa estar em formato time')
        if horario_fechamento <= self.__horario_abertura:
            raise ValueError('O horário de abertura precisa ser menor que o horário de fechamento')
        self.__horario_fechamento = horario_fechamento

    @property
    def profissionais(self) -> list[Profissional]:
        return self.__profissionais

    @profissionais.setter
    def profissionais(self, profissionais: list[Profissional]):
        if not isinstance(profissionais, list):
            raise TypeError('O parâmetro profissionais precisa ser uma lista')
        self.__profissionais = profissionais

    def incluir_profissional(self, profissional: Profissional) -> None:
        if not isinstance(profissional, Profissional):
            raise TypeError('O parâmetro profissional precisa ser do tipo Profissional')
        if profissional in self.__profissionais:
            raise ValueError('Este profissional já está vinculado à clínica')
        self.__profissionais.append(profissional)

    def excluir_profissional(self, profissional: Profissional) -> None:
        if not isinstance(profissional, Profissional):
            raise TypeError('O parâmetro profissional precisa ser do tipo Profissional')
        if profissional not in self.__profissionais:
            raise ValueError('Este profissional não está vinculado à clínica')
        self.__profissionais.remove(profissional)

    def esta_aberta(self, atendimento: Atendimento) -> None:
        inicio = atendimento.horario_inicio
        fim = atendimento.horario_fim

        if self.__horario_abertura <= inicio and fim <= self.__horario_fechamento:
            return True
        return False


