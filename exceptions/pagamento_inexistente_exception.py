class PagamentoInexistenteException(Exception):
    def __init__(self, codigo):
        super().__init__(f'Não foi possível encontrar pagamento com o código: {codigo}')