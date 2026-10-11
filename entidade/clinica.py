from datetime import datetime, time
from profissional import Profissional

class Clinica:
    def __init__(self, codigo: int, nome: str, localizacao: str, descricao: str, horario_abertura: time, horario_fechamento: time) -> None:
        
        if not isinstance(codigo, int):
            raise TypeError('O código precisa estar em formato de string')

        if not isinstance(nome, str):
            raise TypeError('O nome precisa estar em formato de string')

        if not isinstance(localizacao, str):
            raise TypeError('A localização precisa estar em formato de string')

        if not isinstance(descricao, str):
            raise TypeError('A descrição precisa estar em formato de string')

        if not isinstance(horario_abertura, time):
            raise TypeError('O horário de abertura precisa estar em formato de time')

        if not isinstance(horario_fechamento, time):
            raise TypeError('O horário de fechamento precisa estar em formato de time')

        if horario_abertura >= horario_fechamento:
            raise ValueError('O horário de início deve ser menor que o horário de fim')

        self.__codigo = codigo
        self.__nome = nome
        self.__localizacao = localizacao
        self.__descricao = descricao
        self.__horario_abertura = horario_abertura
        self.__horario_fechamento = horario_fechamento
        self.__profissionais = []

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int) -> None:
        if not isinstance(codigo, int):
            raise TypeError('O código precisa ser tipo inteiro')
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
        if horario_abertura >= self.horario_fechamento:
            raise ValueError('O horário de abertura precisa ser menor que o horário de fechamento')
        self.__horario_abertura = horario_abertura

    @property
    def horario_fechamento(self) -> time:
        return self.__horario_fechamento

    @horario_fechamento.setter
    def horario_fechamento(self, horario_fechamento: time) -> None:
        if not isinstance(horario_fechamento, time):
            raise TypeError('O horário de fechamento precisa estar em formato time')
        if self.__horario_abertura >= horario_fechamento:
            raise ValueError('O horário de fechamento precisa ser maior que o horário de abertura')
        self.__horario_fechamento = horario_fechamento

    @property
    def profissionais(self) -> list[profissionais]:
        return self.__profissionais

    @profissionais.setter
    def profissionais(self, profissionais: list[Profissional]):
        if not isinstance(profissionais, list):
            raise TypeError('O parâmetro profissionais precisa ser uma lista')
        self.__profissionais = profissionais

    def incluir_profissional(self, profissional):
        if not isinstance(profissional, Profissional):
            raise TypeError('O parâmetro profissional precisa ser do tipo Profissional')
        self.__profissionais.append(profissional)

    def excluir_profissional(self, profissional):
        if not isinstance(profissional, Profissional):
            raise TypeError('O parâmetro profissional precisa ser do tipo Profissional')
        self.__profissionais.remove(profissional)

    def esta_aberta(self):
        horario_atual = datetime.now().time()

        if self.__horario_abertura <= horario_atual <= self.horario_fechamento:
            return True
        else:
            return False


