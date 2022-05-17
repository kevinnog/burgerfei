#importações necessárias
import menu
from time import sleep 
from utils import *
from opcoes import *

#verificar se o arquivo com os dados das pessoas existe e se não existir cria o arquivo
arq = "cadastrados.txt"
if not arqExiste(arq): 
    criarArquivo(arq)

#loop para verificar as opções que serão escolhidas
restart = False
i = 0
while i < 3:
    #variavel que contem a lista de opções
    resposta = menu.menu_opcoes (['Novo Pedido', 'Cancela Pedido' , 'Insere Produto', \
    'Cancela Produto', 'Valor do Pedido' , 'Extrato do pedido', "Sair"])

    #variavel com o nome das funcoes que serao executadas dependendo do input
    opcoes = {
        0: 'sair',
        1: 'novo_pedido',
        2: 'cancela_pedido',
        3: 'insere_produto',
        4: 'cancela_produto',
        5: 'ver_valor',
        6: 'consulta_extrato'
    }

    if resposta in opcoes:
        #variavel com o nome da funcao selecionada
        func_name = opcoes[resposta]

        if resposta == 0:
            print("Saindo do sistema..")
            break

        #funcao escolhida sendo executada
        locals()[func_name](arq)
        
        sleep(2)
    else:
        print('Opcao nao encontrada!')
    
    