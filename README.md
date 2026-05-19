# 🏢 AccessGuard - Sistema de Controle de Acesso Inteligente

**Programação Orientada a Objetos (POO)** | **Universidade Federal de Minas Gerais (UFMG)**

---

## 📌 Sobre o Projeto
O **AccessGuard** é um software desktop desenvolvido para o gerenciamento e controle de fluxo de pessoas em ambientes corporativos. A solução foi projetada como trabalho final da disciplina de POO, sob orientação da Profa. Luiza Bernardes Real - DEE/UFMG .

O sistema tem um propósito duplo: replicar e propor uma possível solução para um problema real de segurança patrimonial corporativa e, principalmente, demonstrar de forma prática e rigorosa o domínio sobre os pilares fundamentais da Programação Orientada a Objetos.

## ⚠️ O Problema
Atualmente, o controle de acesso físico ainda existente em muitas empresas de médio porte, depende de métodos manuais, pranchetas ou sistemas legados que não diferenciam os perfis de usuários. Esse cenário torna a gestão:
* Vulnerável a acessos não autorizados.
* Suscetível a erros de registro de ponto de funcionários.
* Ineficiente no rastreio temporal de visitantes.

## 🎯 Solução
O software automatiza o fluxo de validação na portaria/catraca/recepção e registra logs imutáveis para auditoria. A arquitetura do sistema foi construída estritamente sob os seguintes conceitos:

* **Abstração & Interfaces:** Uso de classes base abstratas (via módulo `abc`) para definir o contrato genérico de usuários do sistema.
* **Encapsulamento:** Proteção de dados sensíveis (como CPF e IDs) com acesso seguro validado via métodos e *properties*.
* **Herança:** Especialização de usuários genéricos através das subclasses `Funcionario` e `Visitante`.
* **Polimorfismo:** Implementação de regras de validação de acesso distintas sob a mesma assinatura de método (`validar_acesso()`):
  * *Colaboradores:* Validação baseada em vínculo ativo e horário de expediente.
  * *Visitantes:* Validação baseada no prazo de expiração da credencial temporária.
* **Composição:** Estruturação dos logs de acesso (registro de ponto), compostos por instâncias diretas de usuários.

## 🧩 Stack Tecnológica e Escopo
A aplicação é totalmente baseada em Python e conta com:
* **Back-end (Lógica de Negócios):** Python 3.x puro.
* **Front-end (Interface Gráfica):** `CustomTkinter` para a criação de uma interface moderna de Totem/Catraca e de um Painel Administrativo.
* **Persistência de Dados:** Banco de dados local `SQLite` para armazenamento persistente de cadastros e logs.
* **Modelagem:** Diagramas de Classes (UML) detalhando as relações arquiteturais do sistema.

## 👥 Equipe

* **Alex Barbosa Almeida — alexbarbosa@ufmg.br**
* **Maike Moreira da silva — maikems.ufmg@gmail.com**

## 🔄 Padrão de Desenvolvimento

Para mantermos o histórico organizado e garantir a qualidade do código, adotamos um fluxo de trabalho colaborativo rigoroso:
Padrões de Commit (Conventional Commits)

* **`feat:`** Novas funcionalidades (ex: feat: implementa polimorfismo no método validar_acesso da classe Visitante)
* **`fix:`** Correção de bugs (ex: fix: corrige erro de gravação de log no SQLite)
* **`docs:`** Alterações na documentação (ex: docs: adiciona diagrama UML atualizado na pasta docs)
* **`chore:`** Tarefas de manutenção ou configuração (ex: chore: adiciona CustomTkinter no requirements.txt)

Fluxo de Pull Request (PR)
* Nenhum **`commit`** direto na **`main:`** A branch principal deve estar sempre rodando sem erros.
* Criação de **`Branch:`** Antes de iniciar a codificação de uma nova classe ou tela, crie uma branch: git checkout -b feature/classe-funcionario.
* **`Pull Request:`** Ao finalizar a lógica, faça o push da branch e abra um PR no GitHub detalhando os métodos criados.
* Revisão Obrigatória: 1 colega de equipe deve revisar o código, verificando especialmente se os princípios de POO (como o encapsulamento) foram respeitados antes de aprovar o merge.

## 🚀 Como executar o projeto

1. Clone este repositório:
   ```bash
   git clone [https://github.com/allex-almeida/SISTEMA-AccessGuard.git](https://github.com/allex-almeida/SISTEMA-AccessGuard.git)
