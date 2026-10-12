class TipoAtendimentoInexistenteException(Exception):
    def __init__(self, codigo):
        super().__init__(f'Não existe um tipo de atendimento com o código: {codigo}')