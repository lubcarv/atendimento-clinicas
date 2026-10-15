from datetime import date, time
from entidade.acompanhante import Acompanhante
from entidade.paciente import Paciente
from entidade.pagamento import Pagamento
from entidade.pagamento_cartao import PagamentoCartao
from entidade.pagamento_dinheiro import PagamentoDinheiro
from entidade.pagamento_pix import PagamentoPix
from entidade.procedimento import Procedimento
from entidade.profissional import Profissional
from entidade.clinica import Clinica
from entidade.tipo_atendimento import TipoAtendimento
from exceptions.acompanhante_menor_de_idade_exception import AcompanhanteMenorDeIdadeException
from exceptions.pagamento_apos_atendimento_exception import PagamentoAposAtendimentoException
from exceptions.valor_pago_excedente_exception import ValorPagoExcedenteException


class Atendimento:
    def __init__(self, codigo: str, clinica: Clinica, paciente: Paciente, profissional: Profissional,
                 tipo_atendimento: TipoAtendimento, data: date, horario_inicio: time, horario_fim: time,
                 valor: float):
        if not isinstance(codigo, str):
            raise TypeError("O código deve ser um texto.")
        self.__codigo = codigo
        self.clinica = clinica
        self.paciente = paciente
        self.profissional = profissional
        self.tipo_atendimento = tipo_atendimento
        self.data = data
        self.horario_inicio = horario_inicio
        self.horario_fim = horario_fim
        self.valor = valor
        self.__acompanhante = None
        self.__procedimentos = []
        self.__pagamentos = []

    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def clinica(self) -> Clinica:
        return self.__clinica

    @clinica.setter
    def clinica(self, clinica: Clinica):
        if not isinstance(clinica, Clinica):
            raise TypeError('clínica tem de ser tipo Clinica.')
        self.__clinica = clinica

    @property
    def paciente(self) -> Paciente:
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente: Paciente):
        if not isinstance(paciente, Paciente):
            raise TypeError('paciente tem de ser tipo Paciente.')
        self.__paciente = paciente

    @property
    def acompanhante(self) -> Acompanhante:
        return self.__acompanhante

    @property
    def profissional(self) -> Profissional:
        return self.__profissional

    @profissional.setter
    def profissional(self, profissional: Profissional):
        if not isinstance(profissional, Profissional):
            raise TypeError('profissional tem de ser tipo Profissional.')
        self.__profissional = profissional

    @property
    def tipo_atendimento(self) -> TipoAtendimento:
        return self.__tipo_atendimento

    @tipo_atendimento.setter
    def tipo_atendimento(self, tipo_atendimento: TipoAtendimento) -> None:
        if not isinstance(tipo_atendimento, TipoAtendimento):
            raise TypeError('tipo_atendimento tem de ser tipo TipoAtendimento.')
        self.__tipo_atendimento = tipo_atendimento

    @property
    def data(self) -> date:
        return self.__data

    @data.setter
    def data(self, data: date):
        if not isinstance(data, date):
            raise TypeError('data tem de ser tipo datetime.date.')
        self.__data = data

    @property
    def horario_inicio(self) -> time:
        return self.__horario_inicio

    @horario_inicio.setter
    def horario_inicio(self, horario_inicio: time):
        if not isinstance(horario_inicio, time):
            raise TypeError('horario_inicio tem de ser tipo datetime.time.')
        self.__horario_inicio = horario_inicio

    @property
    def horario_fim(self) -> time:
        return self.__horario_fim

    @horario_fim.setter
    def horario_fim(self, horario_fim: time):
        if not isinstance(horario_fim, time):
            raise TypeError('horario_fim tem de ser tipo datetime.time.')
        if horario_fim <= self.__horario_inicio:
            raise ValueError("O horário de fim deve ser depois do horário de início.")
        self.__horario_fim = horario_fim

    @property
    def valor(self) -> float:
        return self.__valor

    @valor.setter
    def valor(self, valor: float):
        if not isinstance(valor, (float, int)):
            raise TypeError('valor tem de ser numérico.')
        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")
        self.__valor = valor

    @property
    def procedimentos(self) -> list[Procedimento]:
        return self.__procedimentos

    @property
    def pagamentos(self) -> list[Pagamento]:
        return self.__pagamentos

    def incluir_acompanhante(self, nome: str, celular: str, cpf: str, data_nascimento: date):
        acompanhante = Acompanhante(nome, celular, cpf, data_nascimento)
        if not acompanhante.maior_de_idade(self.__data):
            raise AcompanhanteMenorDeIdadeException(nome)
        self.__acompanhante = acompanhante

    def excluir_acompanhante(self):
        self.__acompanhante = None

    def incluir_procedimento(self, codigo: str, descricao: str, custo: float, profissional: Profissional):
        procedimento = Procedimento(codigo, descricao, custo, profissional)
        self.__procedimentos.append(procedimento)

    def excluir_procedimento(self, procedimento: Procedimento):
        if procedimento not in self.__procedimentos:
            raise ValueError("Este procedimento não pertence a este atendimento.")
        if self.valor_total() - procedimento.custo < self.valor_pago():
            raise ValueError("Não é possível excluir: o valor já pago ficaria maior que o total do atendimento.")
        self.__procedimentos.remove(procedimento)

    def incluir_pagamento_dinheiro(self, codigo: str, data: date, valor_pago: float):
        if data > self.__data:
            raise PagamentoAposAtendimentoException(data, self.__data)
        if valor_pago > self.valor_restante():
            raise ValorPagoExcedenteException(valor_pago, self.valor_restante())
        self.__pagamentos.append(PagamentoDinheiro(codigo, data, valor_pago, self))

    def incluir_pagamento_pix(self, codigo: str, data: date, valor_pago: float, cpf_pagador: str):
        if data > self.__data:
            raise PagamentoAposAtendimentoException(data, self.__data)
        if valor_pago > self.valor_restante():
            raise ValorPagoExcedenteException(valor_pago, self.valor_restante())
        self.__pagamentos.append(PagamentoPix(codigo, data, valor_pago, self, cpf_pagador))

    def incluir_pagamento_cartao(self, codigo: str, data: date, valor_pago: float, numero_cartao: str, bandeira: str):
        if data > self.__data:
            raise PagamentoAposAtendimentoException(data, self.__data)
        if valor_pago > self.valor_restante():
            raise ValorPagoExcedenteException(valor_pago, self.valor_restante())
        self.__pagamentos.append(PagamentoCartao(codigo, data, valor_pago, self, numero_cartao, bandeira))

    def excluir_pagamento(self, pagamento: Pagamento):
        if pagamento not in self.__pagamentos:
            raise ValueError("Este pagamento não pertence a este atendimento.")
        self.__pagamentos.remove(pagamento)

    def valor_procedimentos(self) -> float:
        return sum(procedimento.custo for procedimento in self.__procedimentos)

    def valor_total(self) -> float:
        return self.__valor + self.valor_procedimentos()

    def valor_restante(self) -> float:
        return self.valor_total() - self.valor_pago()

    def valor_pago(self) -> float:
        return sum(pagamento.valor_pago for pagamento in self.__pagamentos)