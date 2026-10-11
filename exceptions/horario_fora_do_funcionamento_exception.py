class HorarioForaDoFuncionamentoException(Exception):
    def __init__(self, nome_clinica):
        super().__init__(f"Erro: O horário escolhido está fora do funcionamento da clinica {nome_clinica}.")