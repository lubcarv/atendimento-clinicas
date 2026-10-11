class ClinicaInexistenteException(Exception):
    def __init__(self, codigo):
        super().__init__(f"Erro: Não existe uma clínica com o código '{codigo}'")