from tela_abstrata import TelaAbstrata


class TelaClinica(TelaAbstrata):
    def tela_opcoes(self) -> int:
        print('====== Sistema de Clínicas ======')
        print('1. Procurar Clínica por Código')
        print('2. Incluir Clínica')
        print('3. Alterar Clínica')
        print('4. Lista de Clínicas')
        print('5. Excluir Clínica')
        print('6. Vincular Profissional')
        print('7. Desvincular Profissional')
        print('0. Retornar')

        opcao = int(input('Escolha a opção: '))
        return opcao

    def pega_dados_clinica(self) -> dict:
        print("====== DADOS DA CLÍNICA ======")
        codigo = input('Código: ')
        nome = input('Nome: ')
        localizacao = input('Localização: ')
        descricao = input('Descrição: ')
        horario_abertura = self.le_horario('Horário de Abertura (HH:MM): ')
        horario_fechamento = self.le_horario('Horário de Fechamento (HH:MM): ')

        return {'código': codigo,
                'nome': nome,
                'localização': localizacao,
                'descrição': descricao,
                'horário_abertura': horario_abertura,
                'horário_fechamento': horario_fechamento}

    def mostra_clinica(self, dados_clinica: dict) -> None:
        print('====== DETALHES DA CLÍNICA ======')
        print(f'NOME DA CLÍNICA: {dados_clinica["nome"]}')
        print(f'LOCALIZAÇÃO DA CLÍNICA: {dados_clinica['localização']}')
        print(f'DESCRIÇÃO: {dados_clinica['descrição']}')
        print(f'HORÁRIO: Das {dados_clinica['horário_abertura']} às {dados_clinica['horário_fechamento']}')
        print('\n')

        profissionais = [profissional.nome for profissional in dados_clinica['profissionais']]
        if len(profissionais) == 0:
            print('Nenhum profissional vinculado no momento')
        else:
            print(f'PROFISSIONAIS VINCULADOS: {profissionais}')

    def seleciona_clinica(self) -> int:
        codigo = input('Código da clínica que deseja selecionar: ')
        return codigo

    def mostra_mensagem(self, msg) -> None:
        print(msg)

    

        
