from getpass import getpass
from termcolor import colored
import db

MENU = 'voltar'
QTD_COLUNAS = 63

lista_carroNovo = db.show_carroNovo()
lista_carroUsado = db.show_carroUsado()
lista_funcionario = db.show_funcionario()
lista_fornecedor = db.show_fornecedor()
lista_maisVendidos = db.show_maisVendidos()
lista_vendasFuncionario = db.show_vendasFuncionario()
lista_cliente = db.return_cpf()

#exibe o menu 
def exibir_cabecalho():
    """ imprime o cabeçalho no terminal utilizando o tamanho maximo de 60 caracteres """
    print ("-" * QTD_COLUNAS)
    print ("{:^80}".format (colored("COMPRA E VENDA DE CARROS", 'yellow', attrs=['underline', 'bold'])))
    print ("-" * QTD_COLUNAS)

def menu_areaRestrita():
  print ("-" * QTD_COLUNAS)
  print ("{:^80}".format (colored("ÁREA RESTRITA", 'red', attrs=['underline', 'bold'])))
  print ("-" * QTD_COLUNAS)
  print(colored("- Atividades disponíveis:", 'cyan', attrs=['bold']))
  resposta = 0
  while resposta != 1 and resposta != 2 and resposta != 3 and resposta != 4 and resposta != 5 and resposta != 6 and resposta !=7:
    try:
      resposta = int(input("1. Cadastro de um novo funcionário\n2. Demitir funcionário\n3. Fornecedoras com quem trabalhamos\n4. Funcionários que trabalham na loja\n5. Exibir gráfico dos carros mais vendidos\n6. Exibir gráfico dos funcionários que mais venderam carros\n7. Exibir o lucro da loja no mês\n--> "))
    except ValueError:
      print(colored("Opção não reconhecida, por favor informar um número\n", 'red', attrs=['underline','bold']))
    if resposta < 1 or resposta > 7:
      print(colored("Opção inválida, selecione um valor válido!\n", 'red', attrs=['underline', 'bold']))
    
  print ("-" * QTD_COLUNAS)
  return resposta

#mostra as opções disponiveis de serem efetuadas na loja
def exibir_opcoes():
  """ mostra a opcao de compra ou de venda de carros """
  opcoes = 0
  while opcoes != 1 and opcoes != 2 and opcoes != 3 and opcoes != 4:
    try: 
      opcoes = int(input("Selecione:\n- 1 para venda de carros\n- 2 para compra de carros\n- 3 para área restrita\n- 4 para encerrar o programa\n--> "))
      if opcoes == 1:
        print ("-" * QTD_COLUNAS)
        return 1
      elif opcoes == 2: 
        print ("-" * QTD_COLUNAS)
        return 2
      elif opcoes == 3:
        print ("-" * QTD_COLUNAS)
        return 3
      elif opcoes == 4:
        print ("-" * QTD_COLUNAS)
        return 4
      else: 
        print(colored("Opção inválida, selecione um valor válido!\n", 'red', attrs=['underline', 'bold']))
    except ValueError:
      print(colored("Opção não reconhecida, por favor informar um número\n", 'red', attrs=['underline','bold']))
    except Exception:
              exit(0)

def cabecalho_fornecedora():
  print ("-" * QTD_COLUNAS)
  print("{:^76}".format (colored("Informações da fornecedora", "yellow", attrs=['bold'])))
  print ("-" * QTD_COLUNAS)

def cabecalho_cliente():
  print ("-" * QTD_COLUNAS)
  print("{:^76}".format (colored("Informações do cliente", "yellow", attrs=['bold'])))
  print ("-" * QTD_COLUNAS)

def cabecalho_carro():
  print ("-" * QTD_COLUNAS)
  print("{:^76}".format (colored("Informações do carro", "yellow", attrs=['bold'])))
  print ("-" * QTD_COLUNAS)

def cabecalho_pagamento():
  print ("-" * QTD_COLUNAS)
  print("{:^76}".format (colored("Forma de pagamento", "green", attrs=['bold'])))
  print ("-" * QTD_COLUNAS)

def cabecalho_cadastro():
  print ("-" * QTD_COLUNAS)
  print("{:^76}".format (colored("CADASTRO DO CLIENTE", "yellow", attrs=['bold'])))
  print ("-" * QTD_COLUNAS)

def confirmacao_infos():
  print('')
  print(colored("- Informações para confirmação:", "yellow", attrs=['bold', 'underline']))
  print('')

class LojaVendendo:

  def __init__(self, id_funcionario, id_carro):
    self.id_funcionario = id_funcionario
    self.id_carro = id_carro

  
  #remove carros da lista de carros novos quando há uma compra de um cliente
  def remove_carroNovo(self):
    id_maisVendidos = 0
    existe_carro = 0
    quantidade_funcionario = db.quantidade_funcionario()
    quantidade_carroNovo = db.quantidade_carroNovo()
    id_funcionario = 0 
    id_carro = 0
    while id_funcionario > quantidade_funcionario or id_funcionario < 1:
      try:
        id_funcionario = int(input("Antes de efetuar a venda, coloque sua identificação: "))
      except ValueError:
        print(colored("Opção não reconhecida, por favor informar o id do funcionário!\n", 'red', attrs=['underline','bold']))
    
    while id_carro > quantidade_carroNovo or id_carro < 1:
      try:
        id_carro = int(input("Insira o id do carro desejado pelo cliente: "))
      except ValueError:
        print(colored("Opção não reconhecida, por favor informar o id do carro!\n", 'red', attrs=['underline','bold']))
 
    for i in lista_carroNovo:
        if id_carro == i[0]:
          modelo = i[1]
    db.update_vendasFuncionario(id_funcionario)
    
    for i in lista_maisVendidos:
      if modelo == i[1]:
        db.update_carrosVendidos(modelo)
        existe_carro = 1
    
    if existe_carro == 0:
      quantidade = 1
      for i in lista_maisVendidos:
        id_maisVendidos = int(i[0])
      id_maisVendidos += 1 
      tupla = (id_maisVendidos, modelo, quantidade)
      db.add_carrosVendidos(tupla)

    db.remove_carroNovo(id_carro)

  #remove carros da lista de carros usados quando há uma compra de um cliente
  def remove_carroUsado(self):
    id_maisVendidos = 0
    quantidade = 0
    quantidade_funcionario = db.quantidade_funcionario()
    quantidade_carroUsado = db.quantidade_carroUsado()
    id_funcionario = 0
    id_carro = 0
    existe_carro = 0
    while id_funcionario > quantidade_funcionario or id_funcionario < 1:
      try:
        id_funcionario = int(input("Antes de efetuar a venda, coloque sua identificação: "))
      except ValueError:
        print(colored("Opção não reconhecida, por favor informar o id do funcionário!\n", 'red', attrs=['underline','bold']))
    while id_carro > quantidade_carroUsado or id_carro < 1:
      try:
        id_carro = int(input("Insira o id do carro desejado pelo cliente: "))
      except ValueError:
        print(colored("Opção não reconhecida, por favor informar o id do carro!\n", 'red', attrs=['underline','bold']))

    lista_maisVendidos = db.show_maisVendidos()
    lista_carroUsado = db.show_carroUsado()
    
    for i in lista_carroUsado:
        if id_carro == i[0]:
          modelo = i[1]
    db.update_vendasFuncionario(id_funcionario)
    
    for i in lista_maisVendidos:
      if modelo == i[1]:
        db.update_carrosVendidos(modelo)
        existe_carro = 1
    
    if existe_carro == 0:
      quantidade = 1
      for i in lista_maisVendidos:
        id_maisVendidos = int(i[0])
      id_maisVendidos += 1 
      tupla = (id_maisVendidos, modelo, quantidade)
      db.add_carrosVendidos(tupla)

    db.remove_carroUsado(id_carro)

class LojaComprando:

  def __init__(self, id_carro, modelo, marca, ano, cor, quilometragem, preco):
    self.id_carro = id_carro
    self.modelo = modelo 
    self.marca = marca
    self.ano = ano
    self.cor = cor
    self.quilometragem = quilometragem
    self.preco = preco

  def adiciona_carroNovo(self):
 
    #descobrir o proximo id_Carro para o auto_increment
    preco = 0
    for i in lista_carroNovo:
      id_carro = int(i[0])
    id_carro += 1
    modelo = input("Insira o modelo do carro: ")
    marca = input('Insira a marca do carro: ')
    while True:
      try:
        ano = int(input('Insira o ano do carro: '))
        break
      except ValueError:
        print(colored("Opção não reconhecida, por favor informar o ano!\n", 'red', attrs=['underline','bold']))
    cor = input('Insira a cor do carro: ')
    while preco < 1:
      try:
        preco = int(input('Qual o valor do carro? '))
      except ValueError:
        print(colored("Opção não reconhecida, por favor informar o preço!\n", 'red', attrs=['underline','bold']))
    tupla = (id_carro, modelo, marca, ano, cor, 0, preco + preco * 11 / 100)
    lista_carroNovo.append(tupla)
    db.addCarro_fornecedora(tupla)
  
  #Quando a loja compra carro de um cliente, ele é adicionado a lista de carros usados
  def adiciona_carroUsado(self):

    #descobrir o proximo id_Carro para o auto increment
    preco = 0
    quilometragem = 0
    for i in lista_carroUsado:
      id_carro = int(i[0])
    id_carro += 1

    modelo = input("Insira o modelo do carro: ")
    marca = input('Insira a marca do carro: ')
    while True:
      try:
        ano = int(input('Insira o ano do carro: '))
        break
      except ValueError:
        print(colored("Opção não reconhecida, por favor informar o an!\n", 'red', attrs=['underline','bold']))
    while quilometragem < 1:
      try:
        quilometragem = int(input('Insira a quilometragem do carro: '))
      except ValueError:
        print(colored("Opção não reconhecida, por favor informar a quilometragem!\n", 'red', attrs=['underline','bold']))
    cor = input('Insira a cor do carro: ')
    while preco < 1:
      try:
        preco = int(input('Qual o valor do carro? '))
      except ValueError:
        print(colored("Opção não reconhecida, por favor informar o preço!\n", 'red', attrs=['underline','bold']))
    tupla = (id_carro, modelo, marca, ano, quilometragem, cor, preco + preco * 11/100)
    lista_carroUsado.append(tupla)
    db.addCarro_cliente(tupla)

class AreaRestrita:

  def __init__(self, id_funcionario, nome, cargo, salario):
    self.id_funcionario = id_funcionario
    self.nome = nome
    self.cargo = cargo
    self.salario = salario


  #Permitir apenas o dono para adicionar funcionario
  #Contratação de funcionários
  def adiciona_Funcionario(self):
    id_funcionario = 0
    print("{:^80}".format(colored("CADASTRO DE FUNCIONÁRIOS NOVOS", 'cyan', attrs = ['bold'])))
    senha = "senha"
    while id_funcionario != 1:
      try:
        id_funcionario = int(input("Insira seu id: "))
      except ValueError:
        print(colored("Opção não reconhecida, por favor informar o id do dono!\n", 'red', attrs=['underline','bold']))
    #getpass esconde a senha
    tentativa_senha = getpass("Insira a sua senha: ")
    while tentativa_senha != senha:
      tentativa_senha = getpass(colored("Senha incorreta. Tente novamente: ", 'red', attrs = ['underline', 'bold']))

    print(colored("Conta do dono logada com sucesso!", 'green', attrs = ['bold', 'underline']))

    #descobrir o proximo id_funcionario para o auto_increment
    salario = 0
    id_funcionario=0
    for i in lista_funcionario:
      id_funcionario = int(i[0])
    id_funcionario += 1

    nome = input("Entre com o nome do novo funcionário: ")
    cargo = input("Entre com o cargo do novo funcionário: ")
    while salario < 1:
      try:
        salario = int(input("Entre com o salario do novo funcionário: "))
      except ValueError:
        print(colored("Opção não reconhecida, por favor informar o salário!\n", 'red', attrs=['underline','bold']))

    #adiciona funcionário ao banco de dados e na lista
    tupla = (id_funcionario, nome, cargo, salario)
    db.add_novoFuncionarioVendas((id_funcionario, 0))
    db.add_novoFuncionario(tupla)
    lista_funcionario.append(tupla)
    print ("-" * QTD_COLUNAS)

  #Permitir apenas o dono para demitir funcionario
  #Demissão de funcionários
  def remove_funcionario(self):
    id = 0
    id_funcionario = 0
    print ("{:^80}".format (colored("DEMISSÃO DE FUNCIONÁRIOS", 'red', attrs=['underline', 'bold'])))
    print ("-" * QTD_COLUNAS)
    senha = "senha"
    while id_funcionario != 1:
      try:
        id_funcionario = int(input("Insira seu id: "))
      except ValueError:
        print(colored("Opção não reconhecida, por favor informaro id do dono!\n", 'red', attrs=['underline','bold']))
    tentativa_senha = getpass("Insira a sua senha: ")
    while tentativa_senha != senha:
      tentativa_senha = getpass(colored("Senha incorreta. Tente novamente: ", 'red', attrs = ['underline', 'bold']))

    print(colored("Conta do dono logada com sucesso!", 'green', attrs = ['bold', 'underline']))

    for i in lista_funcionario:
      ultimo_id = i[0]
    while id < 2 or id > ultimo_id:
      try:
        id = int(input("Insira o id do funcionário que deseja demitir: "))
      except ValueError:
        print(colored("Opção não reconhecida, por favor informar o id do funcionário!\n", 'red', attrs=['underline','bold']))
    
    #remove o funcionario do banco de dados 
    db.remove_funcionario(id)
    db.remove_funcionarioVendas(int(id))
    print ("-" * QTD_COLUNAS)

class Cliente:
 
  def __init__(self, id_cliente, nome, idade, email, telefone):
    self.id_cliente = id_cliente 
    self.nome = nome
    self.idade = idade
    self.email = email
    self.telefone = telefone

  def get_info_cliente(self):
    id_cliente = 0
    idade = 0
    telefone = 111111111111
    nome = ''
    while len(str(id_cliente)) != 11:
      try:
        id_cliente = int(input("CPF do cliente(sem pontos e traços): "))
      except ValueError:
        print(colored("Opção não reconhecida, por favor informar um CPF!\n", 'red', attrs=['underline','bold']))
    nome = input("Nome do cliente: ")
    while idade < 18:
      try:
        idade = int(input("Idade do cliente: "))
        if idade < 18:
          print(colored("O cliente não tem idade para comprar um carro!\n", 'red', attrs=['underline','bold']))
      except ValueError:
        print(colored("Opção não reconhecida, por favor informar um número\n", 'red', attrs=['underline','bold']))
      

    email = input("Email do cliente: ")
    while len(str(telefone)) > 11:
      try:
        telefone = int(input("Telefone para contato(com DDD): "))
      except ValueError:
        print(colored("Opção não reconhecida, por favor informar um telefone!\n", 'red', attrs=['underline','bold']))
    tupla_cliente = (id_cliente, nome, idade, email, telefone)
    lista_cliente.append(tupla_cliente)
    db.add_cliente(tupla_cliente)

  def already_registered(self):
    existe_cpf = False
    existe_nome = False
    while existe_nome == False:
      print(lista_cliente)
      nome = input("Informe o nome do cliente: ")
      for i in lista_cliente:
        if nome == i[1]:
          existe_nome = True
    
    while existe_cpf == False:
      try:
        id_cliente = int(input("Informe o CPF do cliente: "))
      except ValueError:
        print(colored("Opção não reconhecida, por favor informar um CPF!\n", 'red', attrs=['underline','bold']))

      for i in lista_cliente:
        if id_cliente == i[0]:
          existe_cpf = True
    print(colored("Cliente já cadastrado!", "green", attrs=['bold', 'underline']))
  
class Compra_Venda:

  def __init__(self, id_acao, preco, descricao):
    self.id_acao = id_acao
    self.preco = preco
    self.descricao = descricao
  def get_info_acao(self):
    preco = 0
    id_acao = db.descobre_idAcao()
    
    while preco < 1:
      try:
        preco = int(input("Valor da compra ou venda: "))
      except ValueError:
        print(colored("Opção não reconhecida, por favor informar apenas o preço!\n", 'red', attrs=['underline','bold']))
  
    descricao = input("Foi efetuada uma venda de carros ou uma compra? ")
    while descricao.upper() != "COMPRA" and descricao.upper() != "VENDA":
       try:
        descricao = input("Foi efetuada uma venda de carros ou uma compra? ")
       except ValueError:
        print('Valor inválido, tente apenas "venda" ou "compra"!')
    tupla_acao = (id_acao, preco, descricao)
    db.add_compraEVenda(tupla_acao)
    print ("-" * QTD_COLUNAS)

  def get_info_acao_fornecedora(self):
    id_acao = db.descobre_idAcao()
    preco = int(input("Valor da compra ou venda: "))
    forma_pagamento = input("Qual foi a forma de pagamento: ")
    id_carro = input("Indique a identificação do carro comprado: ")
    id_funcionario = int(input("Identificação do funcionário que efetuou a venda/compra: "))
    id_fornecedor = int(input("Identificação da fornecedora: "))
    descricao = input("Foi efetuada uma venda de carros ou uma compra? ")
    while descricao.upper() != "COMPRA" and descricao.upper() != "VENDA":
      try:
        descricao = input("Foi efetuada uma venda de carros ou uma compra? ")
      except ValueError:
        print('Valor inválido, tente apenas "venda" ou "compra"!')
    tupla_acao = (id_acao, preco, forma_pagamento, id_carro, id_funcionario, id_fornecedor, descricao)
    db.add_compraEVenda(tupla_acao)
    print ("-" * QTD_COLUNAS)
    
class Fornecedor:

  def __init__(self, id_fornecedor, marca, modelos):
    self.id_fornecedor = id_fornecedor
    self.marca = marca
    self.modelos = modelos 

  def get_info_fornecedor(self):
    id_fornecedor = 0
    quantidade = 0
    existe_fornecedora = 0
    lista_fornecedor = db.show_fornecedor()
    for i in lista_fornecedor:
      id_fornecedor = i[0]
    id_fornecedor += 1
    marca = input("Insira o nome da fornecedora(marca): ")
    for i in lista_fornecedor:
      if marca == str(i[1]):
        db.update_fornecedor(marca)
        existe_fornecedora = 1
    if existe_fornecedora == 0:
      quantidade = 1
      tupla_fornecedor = (id_fornecedor, marca, quantidade)
      db.add_fornecedor(tupla_fornecedor)
    print ("-" * QTD_COLUNAS)

#exibe as informações dos carros novos disponíveis
def show_carroNovoTable():
  print ("-" * QTD_COLUNAS)
  print("{:^75}".format (colored("TABELA DE CARROS 0KM", "cyan", attrs=['bold'])))
  print('')
  print("{:^60}".format ("ID | MODELO | MARCA | ANO | COR"))
  print ("-" * QTD_COLUNAS)
  for i in db.show_carroNovo():
    print(i)
  print ("-" * QTD_COLUNAS)

#exibe as informações dos carros usados disponíveis
def show_carroUsadoTable():
  print ("-" * QTD_COLUNAS)
  print("{:^75}".format (colored("TABELA DE CARROS USADOS", "cyan", attrs=['bold'])))
  print("{:^60}".format ("ID | MODELO | MARCA | ANO | COR"))
  print ("-" * QTD_COLUNAS)
  for i in db.show_carroUsado():
    print(i)
  print ("-" * QTD_COLUNAS)

#exibe a lista de funcionários no menu 
def show_listaFuncionarios():
  lista_nomeFuncionarios = db.show_nomeFuncionarios()
  id_funcionario = 1
  print("{:^75}".format (colored("FUNCIONÁRIOS", "cyan", attrs=['bold'])))
  print ("-" * QTD_COLUNAS)
  for i in lista_nomeFuncionarios:
    for j in i:
      print(f"{id_funcionario}- {j}")
    id_funcionario += 1

#exibe a lista de fornecedoras no menu 
def show_listaFornecedoras():
  lista_nomeFornecedoras = db.show_nomeFornecedora()
  id_fornecedora = 1
  print("{:^75}".format (colored("FORNECEDORAS", "cyan", attrs=['bold'])))
  print ("-" * QTD_COLUNAS)
  for i in lista_nomeFornecedoras:
    for j in i:
      print(f"{id_fornecedora}- {j}")
    id_fornecedora += 1

def show_lucro():
  vendas = db.sum_superavit()
  compras = db.sum_deficit()
  for i in vendas:
    soma_vendas = i[0]
  for i in compras:
    soma_compras = i[0]
  lucro = soma_vendas - soma_compras

  if lucro >= 0:
    print("A LOJA OBTEVE UM LUCRO DE:\n")
    print(colored('█'*30, 'green'))
    print(f'R$ {lucro}')
  else:
    print("A LOJA OBTEVE UM PREJUÍZO DE:\n")
    print(colored('█'*30, 'red'))
    print(f'R$ {lucro}')

  


  