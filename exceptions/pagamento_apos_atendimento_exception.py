from datetime import date

class PagamentoAposAtendimentoException(Exception):
    def __init__(self, data_pagamento: date, data_atendimento: date) -> None:
        super().__init__(f"Erro: O pagamento deve ser feito até a data do atendimento. "
                         f"Atendimento: {data_atendimento.strftime('%d/%m/%Y')}, e Pagamento: {data_pagamento.strftime('%d/%m/%Y')}")