import db
import mensagens as msg
import matplotlib.pyplot as plt

def grafico_carros():
  lista = db.carros_maisVendidos()
  lista_nome, lista_quant = [], []

  #fazendo a lista de cada um dos itens
  for i in lista:
    lista_nome.append(i[1])
    lista_quant.append(i[2])

  fig = plt.figure(figsize = (10, 5))

  plt.bar(lista_nome, lista_quant, color='maroon', width = 0.4)

  plt.xlabel("Carros mais vendidos")
  plt.ylabel("Quantidade de vendas")
  plt.title("Gráfico de Carros mais vendidos")
  plt.show()

def grafico_funcionarios():
  lista = db.funcionarios_maisVendas()
  lista_id, lista_quant = [], []

  #fazendo a lista de cada item
  for i in lista:
    lista_id.append(i[0])
    lista_quant.append(i[1])

  fig = plt.figure(figsize = (10, 5))

  plt.bar(lista_id, lista_quant, color='maroon', width = 0.4)

  plt.xlabel("Funcionários que mais venderam")
  plt.ylabel("Quantidade de vendas")
  plt.title("Gráfico de funcionários que mais venderam")
  plt.show()
     
