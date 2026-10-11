class AcompanhanteMenorDeIdadeException(Exception):
    def __init__(self, nome_acompanhante):
        super().__init__(f"Erro: O acompanhante vinculado: {nome_acompanhante} é menor de idade e precisa de um acompanhante maior de idade. ")