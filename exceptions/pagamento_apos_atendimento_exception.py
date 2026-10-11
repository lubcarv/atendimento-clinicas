class PagamentoAposAtendimentoException(Exception):
    def __init__(self, data_pagamento, data_atendimento):
        super().__init__(f"Erro: O pagamento deve ser feito até a data do atendimento."
                         f"Atendimento: {data_atendimento.strftime('%d/%m/%Y')}, e Pagamento: {data_pagamento.strftime('%d/%m/%Y')}")