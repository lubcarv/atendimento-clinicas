class PacienteInexistenteException(Exception):
    def __init__(self, cpf_paciente):
        super().__init__(f"Erro: Não existe um paciente com o CPF: '{cpf_paciente}'")