from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import date
from entidade.pagamento import Pagamento

if TYPE_CHECKING:
    from entidade.atendimento import Atendimento

class PagamentoPix(Pagamento):
    def __init__(self, codigo: str, data: date, valor_pago: float, atendimento: Atendimento, cpf_pagador: str) -> None:
        super().__init__(codigo, data, valor_pago, atendimento)
        self.cpf_pagador = cpf_pagador

    @property
    def cpf_pagador(self) -> str:
        return self.__cpf_pagador

    @cpf_pagador.setter
    def cpf_pagador(self, cpf_pagador: str) -> None:
        if not isinstance(cpf_pagador, str):
            raise TypeError("O CPF do pagador deve ser um texto.")
        self.__cpf_pagador = cpf_pagador

    def modalidade(self) -> str:
        return "PIX"