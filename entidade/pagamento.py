from abc import abstractmethod, ABC
from datetime import date


class Pagamento(ABC):

    def __init__(self, codigo: int, data: date, valor_pago: float, atendimento: "Atendimento"):
        if not  isinstance(codigo, int):
            raise TypeError("O código deve ser um número inteiro.")
        self.__codigo = codigo
        self.data = data
        self.valor_pago = valor_pago
        self.__atendimento = atendimento

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def data(self) -> date:
        return self.__data

    @data.setter
    def data(self, data: date):
        if not isinstance(data, date):
            raise TypeError("A data do pagamento deve ser uma data.")
        self.__data = data

    @property
    def valor_pago(self) -> float:
        return self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, valor_pago: float):
        if not isinstance(valor_pago, (int, float)):
            raise TypeError("Valor_pago deve ser um número.")
        if valor_pago <= 0:
            raise ValueError("Valor_pago deve ser maior que zero.")
        self.__valor_pago = valor_pago

    @property
    def atendimento(self) -> "Atendimento":
        return self.__atendimento

    @property
    def paciente(self) -> "Paciente":
        return self.__atendimento.paciente

    @abstractmethod
    def modalidade(self) -> str:
        pass