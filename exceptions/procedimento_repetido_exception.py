class ProcedimentoRepetidoException(Exception):
    def __init__(self, codigo: str) -> None:
        super().__init__(f"Erro: Já existe um procedimento cadastrado com o código '{codigo}'")