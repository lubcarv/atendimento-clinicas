class ProfissionalRepetidoException(Exception):
    def __init__(self, cpf_profissional):
        super().__init__(f'Já existe um profissional com o CPF: {cpf_profissional}')