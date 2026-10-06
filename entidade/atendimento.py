import datetime

class Atendimento:
    def __init__(self, codigo: int, clinica: Clinica, paciente: Paciente, acompanhante: Acompanhante, profissional: Profissional,
                 tipo_atendimento: TipoAtendimento, data: datetime.date, horario_inicio: datetime.time, horario_fim: datetime.time,
                 valor: float):
        
        if isinstance(codigo, int):
            self.__codigo = codigo
        if isinstance(clinica, Clinica):
            self.__clinica = clinica
        if isinstance(paciente, Paciente):
            self.__paciente = paciente
        if isinstance(acompanhante, Acompanhante):
            self.__acompanhante = acompanhante
        if isinstance(profissional, Profissional):
            self.__profissional = profissional
        if isinstance(tipo_atendimento, TipoAtendimento):
            self.__tipo_atendimento = tipo_atendimento
        if isinstance(data, datetime.date):
            self.__data = data
        if isinstance(horario_inicio, datetime.time):
            self.__horario_inicio = horario_inicio
        if isinstance(horario_fim, datetime.time):
            self.__horario_fim = horario_fim
        if isinstance(valor, float):
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
    def data(self) -> datetime.date:
        return self.__data

    @data.setter
    def data(self, data: datetime.date) -> None:
        if not isinstance(data, datetime.date):
            raise TypeError('data tem de ser tipo datetime.date')
        self.__data = data

    @property
    def horario_inicio(self) -> datetime.time:
        return self.__horario_inicio

    @horario_inicio.setter
    def horario_inicio(self, horario_inicio: datetime.time) -> None:
        if not isinstance(horario_inicio, datetime.time):
            raise TypeError('horario_inicio tem de ser tipo datetime.time')
        self.__horario_inicio = horario_inicio

    @property
    def horario_fim(self) -> datetime.time:
        return self.__horario_fim

    @horario_fim.setter
    def horario_fim(self, horario_fim: datetime.time) -> None:
        if not isinstance(horario_fim, datetime.time):
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

    
