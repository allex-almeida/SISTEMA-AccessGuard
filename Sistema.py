

from funcionario import Funcinario
from visitante import Visitante

class Sistema:

    def __init__(self):

        self.__listaFuncionarios = []
        self.__listaVisitantes = []


    def gerar_id_funcionario(self):

        total = len(self.__listaFuncionarios)

        return f"FUN{total + 1000}"


    def gerar_id_visitante(self):

        total = len(self.__listaVisitantes)

        return f"VIS{total + 2000}"


    def cadastrar_funcionario(self):

        print("\n      CADASTRO FUNCIONÁRIO      ")

        nome = input("Nome: ")
        cpf = input("CPF: ")

        identificacao = self.gerar_id_funcionario()

        email = input("E-mail: ")
        cargo = input("Cargo: ")
        setor = input("Setor: ")

        funcionario = Funcinario(
            nome,
            cpf,
            identificacao,
            email,
            cargo,
            setor
        )

        self.__listaFuncionarios.append(funcionario)

        print("\n===== FUNCIONÁRIO CADASTRADO COM SUCESSO =====")

        print(f"Nome: {nome}")
        print(f"CPF: {cpf}")
        print(f"E-mail: {email}")
        print(f"Cargo: {cargo}")
        print(f"Setor: {setor}")

        print(f"ID gerada: {identificacao}")


    def cadastrar_visitante(self):

        print("\n      CADASTRO VISITANTE      ")

        nome = input("Nome: ")
        cpf = input("CPF: ")

        identificacao = self.gerar_id_visitante()

        email = input("E-mail: ")
        empresaVisitada = input("Empresa Visitada: ")

        visitante = Visitante(
            nome,
            cpf,
            identificacao,
            email,
            empresaVisitada,
            "18:00",
            6
        )

        self.__listaVisitantes.append(visitante)

        print("\n      VISITANTE CADASTRADO COM SUCESSO      ")

        print(f"Nome: {nome}")
        print(f"CPF: {cpf}")
        print(f"E-mail: {email}")
        print(f"Empresa Visitada: {empresaVisitada}")

        print(f"ID gerada: {identificacao}")


    def listar_funcionarios(self):

        print("\n===== FUNCIONÁRIOS =====")

        for funcionario in self.__listaFuncionarios:

            funcionario.exibir_funcionario()

            print("---------------------")


    def listar_visitantes(self):

        print("\n===== VISITANTES =====")

        for visitante in self.__listaVisitantes:

            visitante.exibir_visitante()

            print("---------------------")


    def menu(self):

        opcao = 0

        while opcao != 5:

            print("\n      SISTEMA PORTARIA      ")

            print("1 - Cadastrar Funcionário")
            print("2 - Cadastrar Visitante")
            print("3 - Listar Funcionários")
            print("4 - Listar Visitantes")
            print("5 - Sair")

            opcao = int(input("\nEscolha: "))

            if opcao == 1:

                self.cadastrar_funcionario()

            elif opcao == 2:

                self.cadastrar_visitante()

            elif opcao == 3:

                self.listar_funcionarios()

            elif opcao == 4:

                self.listar_visitantes()

            elif opcao == 5:

                print("\nSistema encerrado")

            else:

                print("\nOpção inválida")
