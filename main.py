import db
from termcolor import colored
import mensagens as msg
from mensagens import (LojaComprando, LojaVendendo, AreaRestrita, Cliente, Compra_Venda, Fornecedor)
import graficos as gr

def main():
  termina = 0
  while termina != 1:
    msg.exibir_cabecalho()
    recebe_opcoes = msg.exibir_opcoes()
    novoLojaVendendo = LojaVendendo("id_funcionario", "id_carro")
    novoLojaComprando = LojaComprando("id_carro","modelo", "marca", "ano", "cor", "quilometragem", "preco")
    novoAreaRestrita = AreaRestrita("id_funcionario", "nome", "cargo", "salario")
    novoCliente = Cliente("id_cliente", "nome", "idade", "email", "telefone")
    novaAcao = Compra_Venda("id_acao", "preco", "descricao")
    novoFornecedor = Fornecedor("id_fornecedor", "marca", "quantidade")


    #loja vendendo carros
    match recebe_opcoes:
      case 1: 
        print ("{:^75}".format (colored("VENDA DE CARROS", 'cyan', attrs=['bold'])))
        print ("-" * 63)
        info_compra = input("O cliente deseja comprar um carro novo ou usado?\n--> ")
          
        while info_compra.upper() != "USADO" and info_compra.upper() != "NOVO":
            info_compra = input("O cliente deseja comprar um carro novo ou usado?\n--> ")

        if info_compra.upper() == "NOVO":
          msg.show_carroNovoTable()
          novoLojaVendendo.remove_carroNovo()
        else:
          msg.show_carroUsadoTable()
          novoLojaVendendo.remove_carroUsado()

        msg.cabecalho_cadastro()
        resposta_cliente = input("O cliente já possui cadastro?\n--> ")
        while resposta_cliente.upper() != "SIM" and resposta_cliente.upper() != "NAO":
          print(colored("Entre apenas com 'sim' ou 'nao'!\n", 'red', attrs=['underline','bold']))
          resposta_cliente = input("O cliente já possui cadastro?\n--> ")

        if resposta_cliente.upper() == "SIM":
          novoCliente.already_registered()
        else:
          novoCliente.get_info_cliente()

        msg.cabecalho_pagamento()
        novaAcao.get_info_acao()

      #loja comprando carros 
      case 2:
        print ("{:^75}".format (colored("COMPRA DE CARROS", 'cyan', attrs=['bold'])))
        print ("-" * 63)
        #perguntar se a compra foi de um cliente ou de uma fornecedora
        recebe_compra = 0
        recebe_compra = int(input("Selecione:\n- 1 para realizar uma compra da fornecedora\n- 2 para uma compra do cliente\n--> "))
        while recebe_compra != 1 and recebe_compra != 2:
          try: recebe_compra = int(input("Selecione 1 para realizar uma compra da fornecedora, e 2 para uma compra do cliente\n--> "))
          except: print("Valor inválido, tente 1 ou 2")
              
        if recebe_compra == 1:
          #2
          msg.cabecalho_fornecedora()
          novoFornecedor.get_info_fornecedor()
          msg.cabecalho_carro()
          novoLojaComprando.adiciona_carroNovo()
          msg.cabecalho_pagamento()
          novaAcao.get_info_acao()

        else: 
          msg.cabecalho_cliente()
          novoCliente.get_info_cliente()
          msg.cabecalho_carro()
          novoLojaComprando.adiciona_carroUsado()
          msg.cabecalho_pagamento()
          novaAcao.get_info_acao()

      #area restrita
      case 3:
        recebe_resposta = msg.menu_areaRestrita()
        match recebe_resposta:
          case 1:
            novoAreaRestrita.adiciona_Funcionario()
          case 2:
            novoAreaRestrita.remove_funcionario()
          case 3:
            msg.show_listaFornecedoras()
          case 4:
            msg.show_listaFuncionarios()
          case 5:
            gr.grafico_carros()
          case 6:
            gr.grafico_funcionarios()
          case 7:
            msg.show_lucro()
        

      case 4:
        print(colored("PROGRAMA ENCERRADO", 'red', attrs=['bold', 'underline']))
        termina = 1

if __name__ == "__main__":
  #inicializa as tabelas do banco de dados
  db.criar_tabelas()
  main()
