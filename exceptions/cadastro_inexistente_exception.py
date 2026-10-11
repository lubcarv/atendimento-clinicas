class CadastroInexistenteException(Exception):
    def __init__(self, entidade: str, chave):
        super().__init__(f"Erro: Não existe cadastro de {entidade.lower()} com o identificador '{chave}'.")