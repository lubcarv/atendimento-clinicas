from datetime import date
from entidade.pagamento import Pagamento


class PagamentoDinheiro(Pagamento):
    def __init__(self, codigo: str, data: date, valor_pago: float, atendimento: "Atendimento"):
        super().__init__(codigo, data, valor_pago, atendimento)

    def modalidade(self) -> str:
        return "Dinheiro"