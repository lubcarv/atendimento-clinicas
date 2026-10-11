class CadastroRepetidoException(Exception):
    def __init__(self, entidade: str, chave):
        super().__init__(f"Erro: Já existe um cadastro de {entidade.lower()} com o identificador '{chave}'.")