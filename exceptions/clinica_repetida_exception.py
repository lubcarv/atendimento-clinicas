class ClinicaRepetidaException(Exception):
    def __init__(self, codigo):
        super().__init__(f"Erro: Já existe uma clínica cadastrada com o código '{codigo}'")