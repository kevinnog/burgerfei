from utils import titulo, linha, lerint

def items(option):
    precos = {
        1: {
            'id': 1,
            'nome': 'X-salada',
            'preco': 10.00
        },
        2: {
            'id': 2,
            'nome': 'X-burger',
            'preco': 10.00
        },
        3: {
            'id': 3,
            'nome': 'Cachorro quente',
            'preco': 7.50
        },
        4: {
            'id': 4,
            'nome': 'Cachorro quente',
            'preco': 8.00
        },
        5: {
            'id': 5,
            'nome': 'Cachorro quente',
            'preco': 5.50
        },
        6: {
            'id': 6,
            'nome': 'Cachorro quente',
            'preco': 4.50
        },
        7: {
            'id': 7,
            'nome': 'Cachorro quente',
            'preco': 6.25
        }
    }
    return precos[option]



#função para fazer a contagem dos numeros de cada elemento da lista a ser criada no código main
def menu_opcoes(lista):
    titulo('Menu')
    for index, item in enumerate(lista):
        if(item != 'Sair'):
            print(f'{index +1} - {item}')
        else:
            print('\n')
            print(f'0 - {item}')
    print(linha()) 
    opc = lerint("Escolha uma opção: ")
    return opc

def menu_produtos(lista):
    titulo('Produtos')
    for index, item in enumerate(lista):
        item = items(index+1)
        id = item['id']
        nome = item['nome']
        preco = item['preco']
        print(f'{id} - {nome} - {preco}')
    print(linha()) 
    prod_cod = str(input("Digite o código do produto escolhido: "))
    quantidade = str(input("Digite a quantidade do produto: "))
    return items(int(prod_cod)), quantidade
      