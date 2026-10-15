from limite.tela_abstrata import TelaAbstrata


class TelaSistema(TelaAbstrata):

    def tela_opcoes(self) -> int:
        print("\n" + "=" * 40)
        print("   SISTEMA DE ATENDIMENTO DE CLÍNICAS")
        print("=" * 40)
        print("Cadastros")
        print("   1 - Pacientes")
        print("   2 - Profissionais")
        print("   3 - Clínicas")
        print("   4 - Tipos de atendimento")
        print("Registros")
        print("   5 - Atendimentos")
        print("   6 - Procedimentos")
        print("   7 - Pagamentos")
        print("Consultas")
        print("   8 - Relatórios")
        print()
        print("   0 - Finalizar sistema")
        print("-" * 40)
        return self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5, 6, 7, 8])