#Função que verifica se o arquivo txt existe
def arqExiste(nome): 
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

#Função que cria o arquivo txt caso não exista 
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Erro na criação")
    else:
        print(f'arquivo {nome} criado com sucesso')

#função para ler a numeração do menu e interpretar como valor inteiro e depois abrir as opções digitadas
def lerint(msg):
    while True:
        try: 
            n = int(input(msg))
        except (ValueError, TypeError):
            print("Erro Digite um número válido")
            continue
        except (KeyboardInterrupt):
            print("Usuário preferiu não digitar o numero")
            return 0
        else:
            return n

#funções para criar (desenhar as linhas) e adicionar o título - estética
def linha(tam=42):
    return'-' * tam

def titulo(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
              

    