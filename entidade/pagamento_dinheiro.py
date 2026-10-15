from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import date
from entidade.pagamento import Pagamento

if TYPE_CHECKING:
    from entidade.atendimento import Atendimento

class PagamentoDinheiro(Pagamento):
    def __init__(self, codigo: str, data: date, valor_pago: float, atendimento: Atendimento) -> None:
        super().__init__(codigo, data, valor_pago, atendimento)

    def modalidade(self) -> str:
        return "Dinheiro"