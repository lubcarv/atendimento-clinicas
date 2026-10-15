from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import date
from entidade.pagamento import Pagamento

if TYPE_CHECKING:
    from entidade.atendimento import Atendimento

class PagamentoCartao(Pagamento):
    def __init__(self, codigo: str, data: date, valor_pago: float, atendimento: Atendimento, numero_cartao: str, bandeira: str):
        super().__init__(codigo, data, valor_pago, atendimento)
        self.numero_cartao = numero_cartao
        self.bandeira = bandeira

    @property
    def numero_cartao(self) -> str:
        return self.__numero_cartao

    @numero_cartao.setter
    def numero_cartao(self, numero_cartao: str) -> None:
        if not isinstance(numero_cartao, str):
            raise TypeError("Número de cartão deve ser um texto.")
        numero_cartao = numero_cartao.replace(" ", "")
        if not numero_cartao.isdigit():
            raise ValueError("Número de cartão deve ser numérico")
        self.__numero_cartao = numero_cartao

    @property
    def bandeira(self) -> str:
        return self.__bandeira

    @bandeira.setter
    def bandeira(self, bandeira: str) -> None:
        if not isinstance(bandeira, str):
            raise TypeError("Bandeira deve ser um texto.")
        self.__bandeira = bandeira

    def modalidade(self) -> str:
        return "Cartão de crédito"