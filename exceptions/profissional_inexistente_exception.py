class ProfissionalInexistenteException(Exception):
    def __init__(self, cpf_profissional: str) -> None:
        super().__init__(f'Não existe nenhum profissional vinculado com o cpf: {cpf_profissional}')