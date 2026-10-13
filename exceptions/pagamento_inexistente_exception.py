class PagamentoInexistenteException(Exception):
    def __init__(self, codigo):
        super().__init__(f"Erro: Não existe um pagamento com o código '{codigo}'")