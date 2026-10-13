class CadastroEmUsoException(Exception):
    def __init__(self, entidade: str, chave):
        super().__init__(f"Erro: O cadastro de {entidade.lower()} '{chave}' não pode ser excluído porque está em uso em um atendimento.")