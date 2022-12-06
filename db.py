import sqlite3

# conecta ao banco de dados 'todo-app'
# caso o banco não exista ele será criado
conn = sqlite3.connect("todo-app.db")
cursor = conn.cursor()

def criar_tabelas():
  
    conn.execute("""
    create table if not exists CARRO_NOVO(
      id_carro integer primary key autoincrement,
      modelo text, 
      marca text, 
      ano integer,
      cor text,
      quilometragem integer, 
      preco integer
    )
    """)
    conn.commit()

    conn.execute("""
    create table if not exists CLIENTE(
      id_cliente integer primary key,
      nome text,
      idade integer,
      email text, 
      telefone integer
    )
    """)
    conn.commit()
    conn.execute("""
    create table if not exists CARRO_USADO(
      id_carro integer primary key autoincrement,
      modelo text,
      marca text,
      ano integer,
      cor text,
      quilometragem integer, 
      preco integer
    )
    """)
    conn.commit()
    conn.execute("""
    create table if not exists FUNCIONARIO(
      id_funcionario integer primary key,
      nome text, 
      cargo text,
      salario integer
    )
    """)
    conn.commit()
    conn.execute("""
    create table if not exists COMPRA_E_VENDA(
      id_acao integer primary key,
      preco decimal(10,2),
      descricao text
    )
    """)
    conn.commit()
    conn.execute("""
    create table if not exists FORNECEDOR(
      id_fornecedor integer primary key,
      marca text,
      quantidade integer 
    )
    """)
    conn.commit()

    conn.execute("""
    create table if not exists CARROS_VENDIDOS(
      id primary key,
      modelo text,
      quantidade integer
    )
    """)
    conn.commit()

    conn.execute("""
    create table if not exists VENDAS_FUNCIONARIO(
      identificacao integer primary key,
      vendas integer
    )
    """)

#funções para adicionar algo no banco de dados
def add_cliente(tupla_cliente):
  conn.execute("insert or replace into CLIENTE (id_cliente, nome, idade, email, telefone) values(?,?,?,?,?)",       
  (tupla_cliente))
  conn.commit()

def add_compraEVenda(tupla_acao):
  conn.execute("insert into COMPRA_E_VENDA (id_acao, preco,  descricao) values(?,?,?)", (tupla_acao))
  conn.commit()

def add_fornecedor(tupla_fornecedor):
  conn.execute("insert into FORNECEDOR (id_fornecedor, marca, quantidade) values(?,?,?)", (tupla_fornecedor))
  conn.commit()

def addCarro_fornecedora(tupla):
  conn.execute("insert into CARRO_NOVO (id_carro, modelo, marca, ano, cor, quilometragem, preco) values(?,?,?,?,?,?,?)", (tupla))
  conn.commit()

def addCarro_cliente(tupla):
  conn.execute("insert into CARRO_USADO (id_carro , modelo, marca, ano, quilometragem, cor, preco) values(?,?,?,?,?,?,?)", (tupla))
  conn.commit()

def add_novoFuncionario(tupla):
  conn.execute("insert into FUNCIONARIO (id_funcionario, nome, cargo, salario) values (?,?,?,?)", (tupla))
  conn.commit()

def add_novoFuncionarioVendas(tupla):
  conn.execute("insert into VENDAS_FUNCIONARIO (identificacao, vendas) values (?,?)", (tupla))
  conn.commit()

def add_carrosVendidos(tupla):
  conn.execute("insert into CARROS_VENDIDOS (id, modelo, quantidade) values(?,?,?)", (tupla))
  conn.commit()

#funções que retornam algum valor do banco de dados
def show_carroNovo():
  cursor.execute("select id_carro as 'ID DO CARRO', modelo, marca, ano, cor, preco from CARRO_NOVO")
  rows = cursor.fetchall()

  return rows

def show_carroUsado():
  cursor.execute("select id_carro, modelo, marca, ano, quilometragem, cor, preco from CARRO_USADO")
  rows = cursor.fetchall()

  return rows

def show_funcionario():
   cursor.execute("select id_funcionario, nome, cargo, salario from FUNCIONARIO")
   rows = cursor.fetchall()

   return rows

def show_fornecedor():
  cursor.execute("""select id_fornecedor, marca, quantidade from FORNECEDOR""")
  rows = cursor.fetchall()

  return rows

def show_maisVendidos():
  cursor.execute("select id, modelo, quantidade from CARROS_VENDIDOS")
  rows = cursor.fetchall()

  return rows

def show_vendasFuncionario():
  cursor.execute("select * from VENDAS_FUNCIONARIO")
  rows = cursor.fetchall()

  return rows

def return_cpf():
   cursor.execute("select id_cliente, nome from CLIENTE")
   rows = cursor.fetchall()

   return rows

def cliente_infos():
  return conn.execute("select id_cliente, nome, idade, email, telefone from cliente")

def quantidade_funcionario():
   cursor.execute("select id_funcionario from FUNCIONARIO")
   i = 0
   rows = cursor.fetchall()
   for row in rows:
    i += 1
   return i

def quantidade_carroNovo():
  cursor.execute("select id_carro from CARRO_NOVO")
  i = 0
  rows = cursor.fetchall()
  for row in rows: 
    i = row[0]
  return i

def quantidade_carroUsado():
  cursor.execute("select id_carro from CARRO_USADO")
  i = 0
  rows = cursor.fetchall()
  for row in rows: 
    i = row[0]
  return i

def descobre_idAcao():
  cursor.execute("select id_acao from COMPRA_E_VENDA")
  i = 0
  rows = cursor.fetchall()
  for row in rows:
    i += 1 
  return i + 1

def funcionarios_maisVendas():
   cursor.execute("""select * from VENDAS_FUNCIONARIO""")
   rows = cursor.fetchall()

   return rows

def carros_maisVendidos():
  cursor.execute("""select * from CARROS_VENDIDOS""")
  rows = cursor.fetchall()

  return rows

def show_nomeFuncionarios():
  cursor.execute("select nome from FUNCIONARIO")
  rows = cursor.fetchall()

  return rows

def show_nomeFornecedora():
  cursor.execute("select marca from FORNECEDOR")
  rows = cursor.fetchall()
  
  return rows

def sum_superavit():
  cursor.execute("""select sum(preco) from COMPRA_E_VENDA where descricao = 'venda'""")
  rows = cursor.fetchall()

  return rows

def sum_deficit():
  cursor.execute("select sum(preco) from COMPRA_E_VENDA where descricao = 'compra'")
  rows = cursor.fetchall()

  return rows
   
#funções para deletar um dado do banco
def remove_carroNovo(id_carro):
  conn.execute(f"delete from CARRO_NOVO where id_carro = {id_carro}")
  conn.commit()

def remove_carroUsado(id_carro):
  conn.execute(f"delete from CARRO_USADO where id_carro = {id_carro}")
  conn.commit()


def remove_funcionario(id_funcionario):
  conn.execute(f"delete from FUNCIONARIO where id_funcionario = {id_funcionario}")
  conn.commit()

def remove_funcionarioVendas(id_funcionario):
  conn.execute(f"delete from VENDAS_FUNCIONARIO where identificacao = {id_funcionario}")
  conn.commit()

#funções para atualizar uma informação do banco de dados
def update_carrosVendidos(modelo):
  conn.execute(f"update CARROS_VENDIDOS set quantidade = quantidade + 1 where modelo = '{modelo}'")
  conn.commit()

def update_vendasFuncionario(id_funcionario):
  conn.execute(f"update VENDAS_FUNCIONARIO set vendas = vendas + 1 where identificacao = {id_funcionario}")
  conn.commit()

def update_fornecedor(marca):
  conn.execute(f"update FORNECEDOR set quantidade = quantidade + 1 where marca = '{marca}'")
  conn.commit()


