from datetime import date, time
from paciente import Paciente
from profissional import Profissional
from clinica import Clinica


class Atendimento:
    def __init__(self, codigo: int, clinica: Clinica, paciente: Paciente, acompanhante: Acompanhante, profissional: Profissional,
                 tipo_atendimento: TipoAtendimento, data: date, horario_inicio: time, horario_fim: time,
                 valor: float):
        
        if not isinstance(codigo, int):
            raise TypeError('O código precisa ser um texto (string)')
        
        if not isinstance(clinica, Clinica):
            raise TypeError('A clinica precisa estar em formato Clinica')
        
        if not isinstance(paciente, Paciente):
            raise TypeError('O paciente precisa estar em formato Paciente')
        
        if not isinstance(acompanhante, Acompanhante):
            raise TypeError('O acompanhante precisa estar em formato Acompanhante')
        
        if not isinstance(profissional, Profissional):
            raise TypeError('O profissional precisa estar em formato Profissional')
        
        if not isinstance(tipo_atendimento, TipoAtendimento):
            raise TypeError('O tipo de atendimento precisa estar em formato TipoAtendimento')
        
        if not isinstance(data, date):
            raise TypeError('A data precisa estar em formato de date')
        
        if not isinstance(horario_inicio, time):
            raise TypeError('Horário de Início precisa estar em formato de time')
        
        if not isinstance(horario_fim, time):
            raise TypeError('Horário de Fim precisa estar em formato de time')
        
        if not isinstance(valor, float):
            raise TypeError('Valor precisa estar em formato de float')
        
        self.__codigo = codigo
        self.__clinica = clinica
        self.__paciente = paciente
        self.__acompanhante = acompanhante
        self.__profissional = profissional
        self.__tipo_atendimento = tipo_atendimento
        self.__data = data
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__valor = valor
        self.__procedimentos = []
        self.__pagamentos = []

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int) -> None:
        if not isinstance(codigo, int):
            raise TypeError('código tem de estar em formato de inteiro')
        self.codigo = codigo

    @property
    def clinica(self) -> Clinica:
        return self.__clinica

    @clinica.setter
    def clinica(self, clinica: Clinica) -> None:
        if not isinstance(clinica, Clinica):
            raise TypeError('clínica tem de ser tipo Clinica')
        self.__clinica = clinica

    @property
    def paciente(self) -> Paciente:
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente: Paciente) -> None:
        if not isinstance(paciente, Paciente):
            raise TypeError('paciente tem de ser tipo Paciente')
        self.__paciente = paciente

    @property
    def acompanhante(self) -> Acompanhante:
        return self.__acompanhante

    @acompanhante.setter
    def acompanhante(self, acompanhante: Acompanhante) -> None:
        if not isinstance(acompanhante, Acompanhante):
            raise TypeError('acompanhante tem ser tipo Acompanhante')
        self.__acompanhante = acompanhante

    @property
    def profissional(self) -> Profissional:
        return self.__profissional

    @profissional.setter
    def profissional(self, profissional: Profissional) -> None:
        if not isinstance(profissional, Profissional):
            raise TypeError('profissional tem de ser tipo Profissional')
        self.__profissional = profissional

    @property
    def tipo_atendimento(self) -> TipoAtendimento:
        return self.__tipo_atendimento

    @tipo_atendimento.setter
    def tipo_atendimento(self, tipo_atendimento: TipoAtendimento) -> None:
        if not isinstance(tipo_atendimento, TipoAtendimento):
            raise TypeError('tipo_atendimento tem de ser tipo TipoAtendimento')
        self.__tipo_atendimento = tipo_atendimento

    @property
    def data(self) -> date:
        return self.__data

    @data.setter
    def data(self, data: date) -> None:
        if not isinstance(data, date):
            raise TypeError('data tem de ser tipo datetime.date')
        self.__data = data

    @property
    def horario_inicio(self) -> time:
        return self.__horario_inicio

    @horario_inicio.setter
    def horario_inicio(self, horario_inicio: time) -> None:
        if not isinstance(horario_inicio, time):
            raise TypeError('horario_inicio tem de ser tipo datetime.time')
        self.__horario_inicio = horario_inicio

    @property
    def horario_fim(self) -> time:
        return self.__horario_fim

    @horario_fim.setter
    def horario_fim(self, horario_fim: time) -> None:
        if not isinstance(horario_fim, time):
            raise TypeError('horario_fim tem de ser tipo datetime.time')
        self.__horario_fim = horario_fim

    @property
    def valor(self) -> float:
        return self.__valor

    @valor.setter
    def valor(self, valor: float) -> None:
        if not isinstance(valor, float):
            raise TypeError('valor tem de ser tipo float')
        self.__valor = valor

    @property
    def procedimentos(self) -> list[Procedimento]:
        return self.__procedimentos

    @procedimentos.setter
    def procedimentos(self, procedimentos: list[Pagamento]) -> None:
        if not isinstance(procedimentos, list):
            raise TypeError('Valor precisa ser uma lista')
        self.__procedimentos = procedimentos

    @property
    def pagamentos(self) -> list[Pagamento]:
        return self.__pagamentos

    @pagamentos.setter
    def pagamentos(self, pagamentos: list[Pagamento]) -> None:
        if not isinstance(pagamentos, list):
            raise TypeError('Valor precisa ser uma lista')
        self.__pagamentos = pagamentos

    
