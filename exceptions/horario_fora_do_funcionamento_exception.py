class HorarioForaDoFuncionamentoException(Exception):
    def __init__(self, nome_clinica: str) -> None:
        super().__init__(f"Erro: O horário escolhido está fora do funcionamento da clínica {nome_clinica}.")