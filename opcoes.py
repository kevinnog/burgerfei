from alteracoes import *

def novo_pedido(arq):
    nome = str(input("Digite seu nome: "))
    cpf = str(input("Digite seu cpf: "))
    senha = str(input("Digite uma senha: "))
    if senha == '' or cpf == '' or nome == '':
        print('Campos nao podem estar em branco')
    elif not cpf.isdecimal():
        print('CPF só pode conter números')
    elif len(cpf) != 11:
        print('CPF deve conter 11 dígitos')
    else:
        cadastrar_cliente(arq, nome, cpf, senha)

def cancela_pedido(arq):
    cpf = str(input("Digite seu cpf: "))
    senha = str(input("Digite uma senha: "))
    if senha == '' or cpf == '':
        print('Campos nao podem estar em branco')
    else:
        deletar_pedido(arq, cpf, senha)

def insere_produto(arq):
    cpf = str(input("Digite seu cpf: "))
    senha = str(input("Digite uma senha: "))
    if senha == '' or cpf == '':
        print('Campos nao podem estar em branco')
    else:
        inserir_produto(arq, cpf, senha)

def cancela_produto(arq):
    cpf = str(input("Digite seu cpf: "))
    senha = str(input("Digite uma senha: "))
    if senha == '' or cpf == '':
        print('Campos nao podem estar em branco')
    else:
        cancelar_produto(arq, cpf, senha)

def ver_valor(arq):
    cpf = str(input("Digite seu cpf: "))
    senha = str(input("Digite uma senha: "))
    if senha == '' or cpf == '':
        print('Campos nao podem estar em branco')
    else:
        ver_valor_pedido(arq, cpf, senha)

def consulta_extrato(arq):
    cpf = str(input("Digite seu cpf: "))
    senha = str(input("Digite uma senha: "))
    if senha == '' or cpf == '':
        print('Campos nao podem estar em branco')
    else:
        consultar_extrato(arq, cpf, senha)
