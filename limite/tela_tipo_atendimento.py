from limite.tela_abstrata import TelaAbstrata

class TelaTipoAtendimento(TelaAbstrata):
    def tela_opcoes(self) -> int:
        print('====== SISTEMA DE TIPOS DE ATENDIMENTO ======')
        print('1. Incluir Tipo de Atendimento')
        print('2. Alterar Tipo de Atendimento')
        print('3. Listar Tipos de Atendimento')
        print('4. Excluir Tipo de Atendimento')
        print('0. Retornar')
        return self.le_num_inteiro('Escolha a opção: ', [0, 1, 2, 3, 4])

    def pega_dados_tipo_atendimento(self) -> dict:
        print('====== DADOS DO TIPO DE ATENDIMENTO ======')
        codigo = self.le_texto('CÓDIGO DO TIPO DE ATENDIMENTO: ')
        nome = self.le_texto('NOME DO TIPO DE ATENDIMENTO: ')

        return {'código': codigo, 'nome': nome}

    def mostra_tipo_atendimento(self, dados_tipo_atendimento) -> None:
        print(f'CÓDIGO DO TIPO DE ATENDIMENTO: {dados_tipo_atendimento['código']}')
        print(F'NOME DO TIPO DE ATENDIMENTO: {dados_tipo_atendimento['nome']}')
        print('\n')

    def seleciona_tipo_atendimento(self) -> int:
        codigo = self.le_texto('CÓDIGO DO TIPO DE ATENDIMENTO QUE DESEJA SELECIONAR: ')
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)