class TipoAtendimentoRepetidoException(Exception):
    def __init__(self, codigo: str) -> None:
        super().__init__(f'Já existe um tipo de atendimento com o código: {codigo}')