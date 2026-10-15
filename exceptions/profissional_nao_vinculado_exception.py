class ProfissionalNaoVinculadoException(Exception):
    def __init__(self, nome_profissional: str, nome_clinica: str) -> None:
        super().__init__(f"Erro: O profissional {nome_profissional} não está vinculado à clínica {nome_clinica}")