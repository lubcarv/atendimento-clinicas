class PacienteRepetidoException(Exception):
    def __init__(self, cpf_paciente: str) -> None:
        super().__init__(f"Erro: Já existe um paciente cadastrado com este cpf: '{cpf_paciente}'")