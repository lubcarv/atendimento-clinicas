class AcompanhanteMenorDeIdadeException(Exception):
    def __init__(self, nome_acompanhante: str) -> None:
        super().__init__(f"Erro: O acompanhante {nome_acompanhante} é menor de idade. O acompanhante precisa ser maior de idade.")