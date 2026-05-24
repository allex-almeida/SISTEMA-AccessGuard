class Pessoa:
    def __init__(self, nome,cpf , identificacao, email):
        self.__nome = nome
        self.__cpf = cpf
        self.__identificacao =  identificacao
        self.__email = email
        self.__ativo = True
        

        
    def get_nome(self):
        return self.__nome
        
    def get_cpf(self):
        return self.__cpf
        
    def get_identificacao(self):
        return self.__identificacao
        
    def get_email(self):
        return self.__email
        
    def get_ativo(self):
        return self.__ativo
        

    
    def set_nome(self, nome):
        self.__nome
        
    def set_cpf(self, cpf):
        self.__cpf
        
    def set_identificacao(self, identificacao):
        self.__identificacao
        
    def set_email(self, email):
        self.__email
        if self.validar_email(email):
            self.__email = email
        
    def set_ativo(self, ativo):
        self.__ativo

    
    def exibir_dados(self):
        print(f"    DADOS DA PESSOA     ")
        print(f"\nNome: {self.nome}")
        print(f"\nCPF: {self.cpf}")
        print(f"ID: {self.identificacao}")
        print(f"E-mail: {self.email}")
        
        if self.ativo:
            print(f"Status : ATIVO")
        else: 
            print(f"Status : INATIVO")
            
            
    def validar_cpf(self):
        if len(self.cpf) == 11 and self.cpfisdigit():
            return True
        return False
        
        
    def validar_email(self, email):
        if "@" in email and ".com" in email:
            return True
        return False

    