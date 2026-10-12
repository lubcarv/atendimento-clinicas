class ProcedimentoInexistenteException(Exception):
    def __init__(self, codigo):
        super().__init__(f"Erro: Não existe um procedimento com o código '{codigo}'")