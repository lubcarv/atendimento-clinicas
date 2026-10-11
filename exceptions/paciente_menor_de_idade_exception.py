class PacienteMenorDeIdadeException(Exception):
    def __init__(self, nome_paciente):
        super().__init__(f"Erro: Já existe um paciente cadastrado com este nome. '{nome_paciente}'")
        