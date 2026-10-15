from limite.tela_abstrata import TelaAbstrata

class TelaRelatorio(TelaAbstrata):
    def tela_opcoes(self) -> int:
        print('\n====== SISTEMA DE RELATÓRIOS ======')
        print('1. Clinicas com Mais Atendimentos')
        print('2. Atendimentos Mais Caros e Mais Baratos')
        print('3. Procedimentos Mais Realizados')
        print('4. Procedimentos Mais Caros e Mais Baratos')
        print('0. Retornar')
        return self.le_num_inteiro('Escolha a opção: ', [0, 1, 2, 3, 4])

    def mostra_relatorio(self, titulo: str, linhas: list) -> None:
        print(f'====== {titulo} ======')
        for linha in linhas:
            print(linha)

        print('=' * (len(titulo) + 14))

    def pega_dados_relatorio(self) -> tuple:
        titulo = self.le_texto('Título do relatório: ').strip()
        while True:
            qtd_linhas = self.le_num_inteiro('Quantidade de linhas: ')
            if qtd_linhas > 0:
                break
            print('A quantidade de linhas deve ser maior que zero.')

        return titulo, qtd_linhas

        