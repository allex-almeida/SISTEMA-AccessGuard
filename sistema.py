import json

from funcionario import Funcionario
from visitante import Visitante


class Sistema:

    def __init__(self):

        self.__listaFuncionarios = []
        self.__listaVisitantes = []

        self.__contadorFuncionarios = 1000
        self.__contadorVisitantes = 2000

        self.__idsRemovidos = []

        self.carregar_dados()

    def gerar_id_funcionario(self):

        self.__contadorFuncionarios += 1

        return f"FUN{self.__contadorFuncionarios}"

    def gerar_id_visitante(self):

        self.__contadorVisitantes += 1

        return f"VIS{self.__contadorVisitantes}"

    def salvar_dados(self):

        func_dict = []

        for f in self.__listaFuncionarios:

            func_dict.append({

                "nome": f.get_nome(),
                "cpf": f.get_cpf(),
                "identificacao": f.get_identificacao(),
                "email": f.get_email(),

                "cargo": f.get_cargo(),
                "setor": f.get_setor(),

                "ativo": f.get_ativo(),

                "dataCadastro": f.get_dataCadastro()

            })

        vis_dict = []

        for v in self.__listaVisitantes:

            vis_dict.append({

                "nome": v.get_nome(),
                "cpf": v.get_cpf(),
                "identificacao": v.get_identificacao(),
                "email": v.get_email(),

                "empresaVisitada": v.get_empresaVisitada(),

                "ativo": v.get_ativo(),

                "dataVisita": v.get_dataVisita()

            })

        dados = {

            "contadorFuncionarios": self.__contadorFuncionarios,
            "contadorVisitantes": self.__contadorVisitantes,

            "idsRemovidos": self.__idsRemovidos,

            "funcionarios": func_dict,
            "visitantes": vis_dict

        }

        with open("dados.json", "w", encoding="utf-8") as arquivo:

            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    def carregar_dados(self):

        try:

            with open("dados.json", "r", encoding="utf-8") as arquivo:

                dados = json.load(arquivo)

                self.__contadorFuncionarios = dados.get(
                    "contadorFuncionarios", 1000
                )

                self.__contadorVisitantes = dados.get(
                    "contadorVisitantes", 4000
                )

                self.__idsRemovidos = dados.get(
                    "idsRemovidos", []
                )

                if "funcionarios" in dados:

                    for f in dados["funcionarios"]:

                        func = Funcionario(

                            f["nome"],
                            f["cpf"],
                            f["identificacao"],
                            f["email"],

                            f["cargo"],
                            f["setor"],

                            f.get("dataCadastro")

                        )

                        self.__listaFuncionarios.append(func)

                if "visitantes" in dados:

                    for v in dados["visitantes"]:

                        vis = Visitante(

                            v["nome"],
                            v["cpf"],
                            v["identificacao"],
                            v["email"],

                            v["empresaVisitada"],

                            "18:00",

                            6,

                            v.get("dataVisita")

                        )

                        self.__listaVisitantes.append(vis)

        except (FileNotFoundError, KeyError, json.JSONDecodeError):

            self.__listaFuncionarios = []
            self.__listaVisitantes = []

    def cadastrar_funcionario(self):

        print("\n===== CADASTRO FUNCIONÁRIO =====\n")

        nome = input("Nome: ")
        cpf = input("CPF: ")

        identificacao = self.gerar_id_funcionario()

        email = input("E-mail: ")
        cargo = input("Cargo: ")
        setor = input("Setor: ")

        funcionario = Funcionario(

            nome,
            cpf,
            identificacao,
            email,

            cargo,
            setor

        )

        self.__listaFuncionarios.append(funcionario)

        self.salvar_dados()

        print("\n===== FUNCIONÁRIO CADASTRADO COM SUCESSO =====")

        print(f"Nome: {nome}")
        print(f"CPF: {cpf}")

        print(f"E-mail: {email}")

        print(f"Cargo: {cargo}")
        print(f"Setor: {setor}")

        print(f"ID gerada: {identificacao}")

    def cadastrar_visitante(self):

        print("\n===== CADASTRO VISITANTE =====\n")

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

        self.salvar_dados()

        print("\n===== VISITANTE CADASTRADO COM SUCESSO =====")

        print(f"Nome: {nome}")
        print(f"CPF: {cpf}")

        print(f"E-mail: {email}")

        print(f"Empresa Visitada: {empresaVisitada}")

        print(f"ID gerada: {identificacao}")

    def listar_funcionarios(self):

        print("\n===== FUNCIONÁRIOS =====\n")

        if len(self.__listaFuncionarios) == 0:

            print("Nenhum funcionário cadastrado.")

            return

        for funcionario in self.__listaFuncionarios:

            funcionario.exibir_funcionario()

            print("---------------------")

    def listar_visitantes(self):

        print("\n===== VISITANTES =====\n")

        if len(self.__listaVisitantes) == 0:

            print("Nenhum visitante cadastrado.")

            return

        for visitante in self.__listaVisitantes:

            visitante.exibir_visitante()

            print("---------------------")

    def buscar_funcionario_por_id(self):

        print("\n===== BUSCAR FUNCIONÁRIO =====\n")

        id_busca = input("Digite o ID do funcionário: ")

        for funcionario in self.__listaFuncionarios:

            if funcionario.get_identificacao() == id_busca:

                print("\nFUNCIONÁRIO ENCONTRADO\n")

                funcionario.exibir_funcionario()

                return

        print("\nFuncionário não encontrado.")

    def buscar_visitante_por_cpf(self):

        print("\n===== BUSCAR VISITANTE =====\n")

        cpf_busca = input("Digite o CPF do visitante: ")

        encontrou = False

        for visitante in self.__listaVisitantes:

            if visitante.get_cpf() == cpf_busca:

                print("\nVISITANTE ENCONTRADO\n")

                visitante.exibir_visitante()

                print("---------------------")

                encontrou = True

        if not encontrou:

            print("\nVisitante não encontrado.")

    def apagar_cadastro(self):

        print("\n===== APAGAR CADASTRO =====\n")

        id_busca = input("Digite o ID do cadastro: ")

        for funcionario in self.__listaFuncionarios:

            if funcionario.get_identificacao() == id_busca:

                self.__idsRemovidos.append(
                    funcionario.get_identificacao()
                )

                self.__listaFuncionarios.remove(funcionario)

                self.salvar_dados()

                print("\nFuncionário removido com sucesso.")

                return

        for visitante in self.__listaVisitantes:

            if visitante.get_identificacao() == id_busca:

                self.__idsRemovidos.append(
                    visitante.get_identificacao()
                )

                self.__listaVisitantes.remove(visitante)

                self.salvar_dados()

                print("\nVisitante removido com sucesso.")

                return

        print("\nCadastro não encontrado.")

    def listar_ids_removidos(self):

        print("\n===== IDS REMOVIDOS =====\n")

        if len(self.__idsRemovidos) == 0:

            print("Nenhum ID removido.")

            return

        for id_removido in self.__idsRemovidos:

            print(id_removido)

    def menu(self):

        opcao = 0

        while opcao != 9:

            print("\n===== SISTEMA PORTARIA =====\n")

            print("1 - Cadastrar Funcionário")
            print("2 - Cadastrar Visitante")

            print("3 - Listar Funcionários")
            print("4 - Listar Visitantes")

            print("5 - Buscar Funcionário por ID")
            print("6 - Buscar Visitante por CPF")

            print("7 - Apagar Cadastro")

            print("8 - Listar IDs removidos")

            print("9 - Sair")

            try:

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

                    self.buscar_funcionario_por_id()

                elif opcao == 6:

                    self.buscar_visitante_por_cpf()

                elif opcao == 7:

                    self.apagar_cadastro()

                elif opcao == 8:

                    self.listar_ids_removidos()

                elif opcao == 9:

                    print("\nSistema encerrado")

                else:

                    print("\nOpção inválida")

            except ValueError:

                print("\nDigite apenas números!")