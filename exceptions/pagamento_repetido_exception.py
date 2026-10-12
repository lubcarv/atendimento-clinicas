class PagamentoRepetidoException(Exception):
    def __init__(self, codigo):
        super().__init__(f"Erro: Já existe um pagamento cadastrado com o código '{codigo}'")