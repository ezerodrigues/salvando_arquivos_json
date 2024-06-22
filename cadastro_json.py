import json

class CadastroCliente:
    def __init__(self):
        self.codigo_cliente = 1
        self.clientes = {}
    
    def adicionar_cliente(self, nome, idade):
        self.clientes[str(self.codigo_cliente)] = {"nome": nome, "idade": idade}
        self.codigo_cliente += 1
    
    def obter_clientes(self):
        return self.clientes
    
    def salvar_em_json(self, caminho_arquivo):
        with open(caminho_arquivo, 'w') as arquivo:
            json.dump(self.clientes, arquivo)
    
    def carregar_de_json(self, caminho_arquivo):
        try:
            with open(caminho_arquivo, 'r') as arquivo:
                self.clientes = json.load(arquivo)
                # Convertendo as chaves para inteiros antes de usar max
                self.codigo_cliente = max(map(int, self.clientes.keys())) + 1 if self.clientes else 0
        except FileNotFoundError:
            print(f"O arquivo {caminho_arquivo} não foi encontrado. Nenhum dado foi carregado.")
    
    def atualizar_cliente(self, codigo_cliente, nome=None, idade=None):
        codigo_cliente = str(codigo_cliente)  # Converter para string para garantir a consistência
        if codigo_cliente in self.clientes:
            if nome is not None:
                self.clientes[codigo_cliente]['nome'] = nome
            if idade is not None:
                self.clientes[codigo_cliente]['idade'] = idade
        else:
            print(f"Cliente com código {codigo_cliente} não encontrado.")

# Exemplo de uso
cadastro_clientes = CadastroCliente()

# Carregar dados de um arquivo JSON (se existir)
cadastro_clientes.carregar_de_json('clientes.json')

# Adicionar novos clientes via input do usuário
while True:
    nome = input("Digite o nome do cliente (ou 'sair' para finalizar): ")
    if nome.lower() == 'sair':
        break
    idade = input("Digite a idade do cliente: ")
    try:
        idade = int(idade)
        cadastro_clientes.adicionar_cliente(nome, idade)
    except ValueError:
        print("Idade inválida. Por favor, insira um número inteiro.")

# Atualizar um cliente existente via input do usuário
codigo_cliente = input("Digite o código do cliente que deseja atualizar (ou 'sair' para pular): ")
if codigo_cliente.lower() != 'sair':
    try:
        codigo_cliente = int(codigo_cliente)
        nome = input("Digite o novo nome do cliente (ou deixe em branco para não alterar): ")
        idade = input("Digite a nova idade do cliente (ou deixe em branco para não alterar): ")
        idade = int(idade) if idade else None
        cadastro_clientes.atualizar_cliente(codigo_cliente, nome if nome else None, idade)
    except ValueError:
        print("Código ou idade inválida. Por favor, insira números inteiros.")

# Salvando os dados no arquivo JSON
cadastro_clientes.salvar_em_json('clientes.json')

print("Dados salvos no arquivo 'clientes.json'.")
