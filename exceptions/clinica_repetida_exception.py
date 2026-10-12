class ClinicaRepetidaException(Exception):
    def __init__(self, codigo_clinica):
        super.__init__(f'Já existe uma clínica com o código: {codigo_clinica}')