class AtendimentoInexistenteException(Exception):
    def __init__(self, codigo: str) -> None:
        super().__init__(f"Erro: Não existe um atendimento com o código '{codigo}'")