class AtendimentoRepetidoException(Exception):
    def __init__(self, codigo):
        super().__init__(f"Erro: Já existe um atendimento cadastrado com o código '{codigo}'")