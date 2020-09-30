# ------------------------------sistema vendas

print('\n******************CADASTRAR SENHA*******************')
nome = (input('\nDigite seu Nome: '))
senha = (input('Digite uma Senha: '))
print(f'\n\nPronto {nome}, sua senha foi cadastrada')
login_acesso = input('Quer logar agora? Digite sim ou não: ')
verdadeiro = 'sim'
if login_acesso != verdadeiro:
    exit(0)
else:
    print('\n\n******************TELA DE ACESSO*******************')
while True:
    login_nome = input('\nDigite seu nome: ')
    login_senha = input('Digite sua senha: ')
    if login_nome == nome and login_senha == senha:
        break
    else:
        print('Nome ou Senha incorreta')
print(f'\nUsuario {nome} logado...\nSeja bem vindo!\n')
print('Programa para vendedores\n')

desc = 10
comis_vista = 5
comis_parc = 5
print('Menu')
print('1 - Desconco;\n2 - Parcelamento;\n3 - Comissão venda à vista;\n4 - Comissão venda parcelada;\n')

while True:
    menu = int(input('Selecione a opção desejada: '))
    valor = float(input('Valor do produto: R$ '))
    if menu == 1:
        valor_desc = (valor * desc) / 100
        total_desc = valor - valor_desc
        print(f'Total a pagar com desconto 10%: R$ {total_desc}\n')
    if menu == 2:
        valor_parc = valor / 3
        print(f'Valor de parcelamento em 3x sem juros: R$ {valor_parc}\n')
    if menu == 3:
        valor_desc = (valor * desc) / 100
        total_desc = valor - valor_desc
        comissao1 = (total_desc * comis_vista) / 100
        print(f'Comissão vendedor com venda a vista: R$ {comissao1}\n')
    if menu == 4:
        comissao2 = (valor * comis_parc) / 100
        print(f'Comissão vendedor com venda parcelada: R$ {comissao2}\n')
    else:
        print('Menu')
        print('1 - Desconco;\n2 - Parcelamento;\n3 - Comissão venda à vista;\n4 - Comissão venda parcelada;\n')


# -------------------------Colocar no carrinho os produtos

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)


# ---------------------- Jogo Jogar moeda
from random import random


def jogar_moeda():
    # Gerar um número pseudo-randômico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(jogar_moeda())
