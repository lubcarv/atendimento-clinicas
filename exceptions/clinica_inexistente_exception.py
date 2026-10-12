class ClinicaInexistenteException(Exception):
    def __init__(self, codigo):
        super().__init__(f'Não foi possível encontrar uma clínica com o código: {codigo}')