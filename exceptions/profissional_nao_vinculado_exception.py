class ProfissionalNaoVinculadoException(Exception):
    def __init__(self, nome_profissional, nome_clinica):
        super().__init__(f"Erro: O profissional {nome_profissional} não está vinculado a clínica {nome_clinica}")