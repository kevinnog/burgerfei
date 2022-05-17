import datetime
from curses.ascii import isdigit
from time import sleep 
from menu import menu_produtos, items as items_dict
from utils import arqExiste, criarArquivo

#Função para cadastrar as pessoas 
def cadastrar_cliente(arq, nome, cpf, senha):
    try: 
        a = open(arq, 'a')
    except:
        print('erro na abertura do arquivo')
    else: 
        try:
            with open(arq) as f:
                lines = f.readlines()
                new_client = True
                senha_invalida = False
                for line in lines:
                    _, cpf_salvo, senha_salva = line.split(';')
                    if str(cpf_salvo).strip() == str(cpf).strip():
                        if str(senha_salva).strip() != str(senha).strip():
                            senha_invalida = True
                        new_client = False
                        print('CPF já cadastrado:', cpf)
                if new_client:
                    a.write(f'{nome} ; {cpf} ; {senha} \n')
                    print('Cliente cadastrado')
                
                if senha_invalida:
                    print('Senha inválida')
                    sleep(2)
                else:
                    print('Indo para tela de pedidos')
                    sleep(2)
                    cadastrar_pedido(cpf)
            
        except:
            print('Erro')
        else: 
            a.close()

#Função para cadastrar os pedidos
def cadastrar_pedido(cpf_cliente):
    produto, quantidade = menu_produtos (['X-salada', 'X-burger' , 'Cachorro quente', \
    'Misto quente', 'Salada de frutas,' , 'Refrigerante', "Suco natural"])
    pedidos_arq = 'pedidos.txt'
    pedido_text = ''
    if not arqExiste(pedidos_arq): 
        criarArquivo(pedidos_arq)
    with open(pedidos_arq, 'r+') as f:
                lines = f.readlines()
                product_id = produto['id']
                string = [f'{product_id}-{quantidade}']
                pedido_text = 'cadastrado'
                if len(lines) == 0:
                    f.write(f'{cpf_cliente} ; {string} \n')
                else:
                    novas_linhas = []
                    foi_atualizado = False
                    for line in lines:
                        cpf_salvo, pedido = line.split(';')
                        if str(cpf_salvo).strip() == str(cpf_cliente).strip():
                            pedido = pedido.replace('[', '').replace(']', '').replace("'", '').split(',')
                            novos_pedidos = []
                            for item in pedido:
                                if item.strip() != ' ' and item.strip() != '':
                                    novos_pedidos.append(item.strip())
                            novos_pedidos.append(f'{product_id}-{quantidade}')
                            novas_linhas.append(f'{cpf_cliente} ; {novos_pedidos} \n')
                            pedido_text = 'atualizado'
                            foi_atualizado = True
                        else:
                            novas_linhas.append(line)
                    if not foi_atualizado:
                        novas_linhas.append(f'{cpf_cliente} ; {string} \n')
                    f.truncate(0)
                    f.seek(0)
                    f.writelines(novas_linhas)

    print(f'Pedido {pedido_text}')
    f.close()

def deletar_pedido(arq, cpf, senha):
    try: 
        a = open(arq, 'a')
    except:
        print('erro na abertura do arquivo')
    else: 
        try:
            with open(arq) as f:
                lines = f.readlines()
                new_client = True
                senha_invalida = False
                for line in lines:
                    _, cpf_salvo, senha_salva = line.split(';')
                    if str(cpf_salvo).strip() == str(cpf).strip():
                        if str(senha_salva).strip() != str(senha).strip():
                            senha_invalida = True
                        new_client = False
                if new_client:
                    print('Cliente nao cadastrado')
                else:
                    if senha_invalida:
                        print('Senha inválida')
                        print('Pedido nao cancelado')
                    else:
                        pedidos_arq = 'pedidos.txt'
                        with open(pedidos_arq, 'r+') as f:
                            lines = f.readlines()
                            if len(lines) == 0:
                                print('Nenhum pedido cadastrado')
                            else:
                                for line in lines:
                                    novas_linhas = []
                                    cpf_salvo, _ = line.split(';')
                                    if str(cpf_salvo).strip() == str(cpf).strip():
                                        pass
                                    else:
                                        novas_linhas.append(line)
                                f.truncate(0)
                                f.seek(0)
                                f.writelines(novas_linhas)
                        print('Pedido cancelado para o cpf:', cpf)

            
        except:
            print('Erro')
        else: 
            a.close()

def inserir_produto(arq, cpf, senha):
    try: 
        a = open(arq, 'a')
    except:
        print('erro na abertura do arquivo')
    else: 
        try:
            with open(arq) as f:
                lines = f.readlines()
                new_client = True
                senha_invalida = False
                for line in lines:
                    _, cpf_salvo, senha_salva = line.split(';')
                    if str(cpf_salvo).strip() == str(cpf).strip():
                        if str(senha_salva).strip() != str(senha).strip():
                            senha_invalida = True
                        new_client = False
                if new_client:
                    print('Cliente nao cadastrado')
                else:
                    if senha_invalida:
                        print('Senha inválida')
                    else:
                        cadastrar_pedido(cpf)

            
        except:
            print('Erro')
        else: 
            a.close()

def cancelar_produto(arq, cpf, senha):
    try: 
        a = open(arq, 'a')
    except:
        print('erro na abertura do arquivo')
    else: 
        try:
            with open(arq) as f:
                lines = f.readlines()
                new_client = True
                senha_invalida = False
                for line in lines:
                    _, cpf_salvo, senha_salva = line.split(';')
                    if str(cpf_salvo).strip() == str(cpf).strip():
                        if str(senha_salva).strip() != str(senha).strip():
                            senha_invalida = True
                        new_client = False
                if new_client:
                    print('Cliente nao cadastrado')
                else:
                    if senha_invalida:
                        print('Senha inválida')
                    else:
                        pedidos_arq = 'pedidos.txt'
                        texto =  'Produto nao encontrado no pedido'
                        with open(pedidos_arq, 'r+') as f:
                            lines = f.readlines()
                            novas_linhas = []
                            produto_id = str(input("Digite o código do produto que deseja cancelar: "))
                            produto_quantidade = str(input("Digite a quantidade do produto que deseja cancelar: "))
                            for line in lines:
                                cpf_salvo, pedidos = line.split(';')
                                if str(cpf_salvo).strip() == str(cpf).strip():
                                    pedidos = pedidos.replace('[', '').replace(']', '').replace("'", '').split(',')
                                    novos_pedidos = []
                                    for pedido in pedidos:
                                        novos_pedidos.append(pedido.strip())
                                    index = False
                                    if f'{produto_id}-{produto_quantidade}' in novos_pedidos:
                                        texto = 'Produto removido do pedido'
                                        index = novos_pedidos.index(f'{produto_id}-{produto_quantidade}')
                                    if index is not False:
                                        novos_pedidos[index] = novos_pedidos[index] + 'c'
                                    novas_linhas.append(f'{cpf} ; {novos_pedidos} \n')
                                    
                            f.truncate(0)
                            f.seek(0)
                            f.writelines(novas_linhas)
                            f.close()
                            print(texto)
        except:
            print('Erro')
        else:

            a.close()

def ver_valor_pedido(arq, cpf, senha):
    try: 
        a = open(arq, 'a')
    except:
        print('erro na abertura do arquivo')
    else: 
        try:
            with open(arq) as f:
                lines = f.readlines()
                new_client = True
                senha_invalida = False
                for line in lines:
                    _, cpf_salvo, senha_salva = line.split(';')
                    if str(cpf_salvo).strip() == str(cpf).strip():
                        if str(senha_salva).strip() != str(senha).strip():
                            senha_invalida = True
                        new_client = False
                if new_client:
                    print('Cliente nao cadastrado')
                else:
                    if senha_invalida:
                        print('Senha inválida')
                    else:
                        pedidos_arq = 'pedidos.txt'
                        with open(pedidos_arq, 'r+') as f:
                            lines = f.readlines()
                            items = []
                            cpfs = []
                            valor = 0
                            for line in lines:
                                cpf_salvo, _ = line.split(';')
                                cpfs.append(str(cpf_salvo).strip())
                            if str(cpf).strip() not in cpfs:
                                print('Nenhum pedido encontrado para o cpf informado')
                            else:
                                for line in lines:
                                    cpf_salvo, pedidos = line.split(';')
                                    if str(cpf_salvo).strip() == str(cpf).strip():
                                        pedidos = pedidos.replace('[', '').replace(']', '').replace("'", '').split(',')
                                        for pedido in pedidos:
                                            items.append(pedido.strip())
                                for item in items:
                                    if 'c' not in item:
                                        id, quantidade = item.split('-')
                                        preco = items_dict(int(id))['preco']
                                        valor += int(quantidade) * float(preco)
                                print('Valor total do pedido:', f'R${valor}')
                            f.close()
                            
        except:
            print('Erro')
        else:

            a.close()

def consultar_extrato(arq, cpf, senha):
    try: 
        a = open(arq, 'a')
    except:
        print('erro na abertura do arquivo')
    else: 
        try:
            with open(arq) as f:
                lines = f.readlines()
                new_client = True
                senha_invalida = False
                for line in lines:
                    nome_salvo, cpf_salvo, senha_salva = line.split(';')
                    if str(cpf_salvo).strip() == str(cpf).strip():
                        if str(senha_salva).strip() != str(senha).strip():
                            senha_invalida = True
                        new_client = False
                if new_client:
                    print('Cliente nao cadastrado')
                else:
                    if senha_invalida:
                        print('Senha inválida')
                    else:
                        pedidos_arq = 'pedidos.txt'
                        with open(pedidos_arq, 'r+') as f:
                            lines = f.readlines()
                            items = []
                            cpfs = []
                            extrato = []
                            valor_total = 0
                            for line in lines:
                                cpf_salvo, _ = line.split(';')
                                cpfs.append(str(cpf_salvo).strip())
                            if str(cpf).strip() not in cpfs:
                                print('Nenhum pedido encontrado para o cpf informado')
                            else:
                                for line in lines:
                                    cpf_salvo, pedidos = line.split(';')
                                    if str(cpf_salvo).strip() == str(cpf).strip():
                                        pedidos = pedidos.replace('[', '').replace(']', '').replace("'", '').split(',')
                                        for pedido in pedidos:
                                            items.append(pedido.strip())
                                for item in items:
                                    cancelado = False
                                    id, quantidade = item.split('-')
                                   
                                    if 'c' in item:
                                        quantidade = quantidade.split('c')[0]
                                        cancelado = True
                                    preco = items_dict(int(id))['preco']
                                    nome_produto = items_dict(int(id))['nome']
                                    valor = int(quantidade) * float(preco)
                                    if 'c' not in item:
                                        valor_total += valor
                                        extrato.append({
                                            'quantidade': quantidade,
                                            'nome_produto': nome_produto,
                                            'preco': preco,
                                            'valor': valor,
                                            'cancelado': cancelado
                                        })
                                    else:
                                        extrato.append({
                                            'quantidade': quantidade,
                                            'nome_produto': nome_produto,
                                            'preco': preco,
                                            'valor': int(quantidade) * int(preco),
                                            'cancelado': cancelado
                                        })

                                print('Nome:', nome_salvo)
                                print('CPF:', cpf)
                                print('Total:', f'R${valor_total}')
                                print('Data:', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                                print('Items do pedido:')
                                for item in extrato:
                                    item_quantidade = item['quantidade']
                                    item_nome = item['nome_produto']
                                    item_preco_unitario = item['preco']
                                    item_preco_total = item['valor']
                                    item_preco_total = "{:.2f}".format(item_preco_total)
                                    item_preco_total = float(item_preco_total)
                                    item_cancelado = item['cancelado']
                                    sinal = '-' if item_cancelado else '+'
                                    cancelado_texto = ' - Cancelado' if item_cancelado else ''
                                    print(f'{item_quantidade} - {item_nome} - Preco unitário: {item_preco_unitario}  Valor: {sinal} {item_preco_total}{cancelado_texto}')
                            f.close()
                            
        except:
            print('Erro')
        else:

            a.close()


    
    