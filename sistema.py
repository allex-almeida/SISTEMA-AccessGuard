

import json
from funcionario import Funcionario
from visitante import Visitante

class Sistema:

    def __init__(self):
        self.__listaFuncionarios = []
        self.__listaVisitantes = []
        self.carregar_dados()

    def gerar_id_funcionario(self):
        total = len(self.__listaFuncionarios)
        return f"FUN{total + 1000}"

    def gerar_id_visitante(self):
        total = len(self.__listaVisitantes)
        return f"VIS{total + 2000}"
    

    def salvar_dados(self):
        dados = {
            "funcionarios": [f.__dict__ for f in self.__listaFuncionarios],
            "visitantes": [v.__dict__ for v in self.__listaVisitantes]
        }

        with open("dados.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
   

        vis_dict = []
        for v in self.__listaVisitantes:
            vis_dict.append({
                "nome": v.nome,
                "cpf": v.cpf,
                "identificacao": v.identificacao,
                "email": v.email,
                "empresaVisitada": v.empresaVisitada
            })

        dados = {
            "funcionarios": func_dict,
            "visitantes": vis_dict
        }

        with open("dados.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    def carregar_dados(self):
        try:
            with open("dados.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                
                if dados and "funcionarios" in dados:
                    for f in dados["funcionarios"]:
                        func = Funcionario(f["nome"], f["cpf"], f["identificacao"], f["email"], f["cargo"], f["setor"])
                        self.__listaFuncionarios.append(func)
                
                if dados and "visitantes" in dados:
                    for v in dados["visitantes"]:
                        vis = Visitante(v["nome"], v["cpf"], v["identificacao"], v["email"], v["empresaVisitada"], "18:00", 6)
                        self.__listaVisitantes.append(vis)
        except (FileNotFoundError, KeyError, json.JSONDecodeError):
            self.__listaFuncionarios = []
            self.__listaVisitantes = []
            

    def cadastrar_funcionario(self):
        print("\n ===== CADASTRO FUNCIONÁRIO =====")
        print(f"\n")        

        nome = input("Nome: ")
        cpf = input("CPF: ")
        identificacao = self.gerar_id_funcionario()
        email = input("E-mail: ")
        cargo = input("Cargo: ")
        setor = input("Setor: ")

        funcionario = Funcionario(nome, cpf, identificacao, email, cargo, setor)
        self.__listaFuncionarios.append(funcionario)
        
        self.salvar_dados()

        print("\n      FUNCIONÁRIO CADASTRADO COM SUCESSO      ")
        print(f"Nome: {nome}")
        print(f"CPF: {cpf}")
        print(f"E-mail: {email}")
        print(f"Cargo: {cargo}")
        print(f"Setor: {setor}")
        print(f"ID gerada: {identificacao}")

    def cadastrar_visitante(self):
        print("\n ===== CADASTRO VISITANTE =====")
        print("\n")

        nome = input("Nome: ")
        cpf = input("CPF: ")
        identificacao = self.gerar_id_visitante()
        email = input("E-mail: ")
        empresaVisitada = input("Empresa Visitada: ")

        visitante = Visitante(nome, cpf, identificacao, email, empresaVisitada, "18:00", 6)
        self.__listaVisitantes.append(visitante)
        
        self.salvar_dados()

        print("\n ===== VISITANTE CADASTRADO COM SUCESSO =====")
        print("\n")
        print(f"Nome: {nome}")
        print(f"CPF: {cpf}")
        print(f"E-mail: {email}")
        print(f"Empresa Visitada: {empresaVisitada}")
        print(f"ID gerada: {identificacao}")

    def listar_funcionarios(self):
        print("\n ===== FUNCIONÁRIOS ===== ")
        print("\n")
        for funcionario in self.__listaFuncionarios:
            funcionario.exibir_funcionario()
            print("---------------------")

    def listar_visitantes(self):
        print("\n ===== VISITANTES ===== ")
        print("\n")
        for visitante in self.__listaVisitantes:
            visitante.exibir_visitante()
            print("---------------------")

    def menu(self):
        opcao = 0
        while opcao != 5:
            print("\n ===== SISTEMA PORTARIA ===== ")
            print("\n")
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