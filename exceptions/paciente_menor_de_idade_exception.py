class PacienteMenorDeIdadeException(Exception):
    def __init__(self, nome_paciente):
        super().__init__(f"Erro: O paciente '{nome_paciente}' é menor de idade e não tem um acompanhante válido")
        