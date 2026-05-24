

from funcionario import Funcinario
from visitante import Visitante

class Sistema:

    def __init__(self):

        self.__listaFuncionarios = []
        self.__listaVisitantes = []


    def gerar_id(self):

        total = len(self.__listaFuncionarios) + len(self.__listaVisitantes)

        return total + 1000


    def cadastrar_funcionario(self):

        print("\n      CADASTRO FUNCIONÁRIO      ")

        nome = input("Nome: ")
        cpf = input("CPF: ")
        identificacao = self.gerar_id()
        email = input("E-mail: ")
        cargo = input("Cargo: ")
        setor = input("Setor: ")

        funcionario = Funcinario(nome, cpf, identificacao,
                                 email, cargo, setor)

        self.__listaFuncionarios.append(funcionario)

        print("\nFuncionário cadastrado")


    def cadastrar_visitante(self):

        print("\n      CADASTRO VISITANTE      ")

        nome = input("Nome: ")
        cpf = input("CPF: ")
        identificacao = self.gerar_id()
        email = input("E-mail: ")
        empresaVisitada = input("Empresa Visitada: ")

        visitante = Visitante(nome, cpf, identificacao,
                              email, empresaVisitada,
                              "18:00", 2)

        self.__listaVisitantes.append(visitante)

        print("\nVisitante cadastrado")


    def listar_funcionarios(self):

        print("\n      FUNCIONÁRIOS      ")

        for funcionario in self.__listaFuncionarios:

            funcionario.exibir_funcionario()

            print("---------------------")


    def listar_visitantes(self):

        print("\n      VISITANTES      ")

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
