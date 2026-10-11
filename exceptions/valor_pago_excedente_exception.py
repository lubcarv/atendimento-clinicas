class ValorPagoExcedenteException(Exception):
    def __init__(self, valor_pago, valor_restante):
        super().__init__(f"Erro: O valor pago (R$ {valor_pago:.2f}) é maior que o valor restante (R$ {valor_restante:.2f}).")