# 1
numero = int(input('Digite um numero inteiro: '))
print(numero)
# 2
numero = float(input('Digite um numero real: '))
print(numero)
# 3
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))
print(f'A soma é: {num1+num2+num3}')
# 4
numero = float(input('Digite um numero real: '))
numero = numero*numero
print(numero)
# 5
numero = float(input('Digite um numero real: '))
numero = numero/5
print(numero)
# 6
c = float(input('Digite a temperatura em graus Celsius: '))
f = c*(9.0/5.0)+32.0
print(f'Convertido em graus Fahrenheit {f}')
# 7
f = float(input('Digite a temperatura em graus Fahrenheit: '))
c = 5.0 * (f-32.0)/9.0
print(f'Convertido em graus Celsius {c}')
# 8
k = float(input('Digite a temperatura em graus Kelvin: '))
c = k - 273.15
print(f'Convertida em graus Celsius {c}')
# 9
c = float(input('Digite a temperatura em graus Celsius: '))
k = c + 273.15
print(f'Convertida em graus Kelvin {k}')
# 10
k = float(input('Digite a velocidade em km/h: '))
m = k / 3.6
print(f'Velocidade convertida em m/s: {m}')
# 11
m = float(input('Digite a velocidade em m/s: '))
k = m * 3.6
print(f'Velocidade convertida em k/h: {k}')
# 12
m = float(input('Digite a distância em milhas: '))
k = 1.61 * m
print(f'Distância convertida em quilômetros: {k}')
# 13
k = float(input('Digite a distância em quilômetros: '))
m = k / 1.61
print(f'Distância convertida em milhas: {m}')
# 14
g = float(input('Digite o valor do ângulo em graus: '))
r = g * 3.14 / 180
print(f'Conversão em radianos: {r}')
# 15
r = float(input('Digite o valor do radiano: '))
g = r * 180 / 3.14
print(f'Conversão eem ângulo graus: {g}')
# 16
p = float(input('Digite o comprimento em polegadas: '))
c = p * 2.54
print(f'Convertido em centimetroa: {c}')
# 17
c = float(input('Digite o centimetro: '))
p = c / 2.54
print(f'Convertido em comprimento em polegada: {p}')
# 18
M = float(input('Digite o volume em metros cúbicos: '))
L = 1000 * M
print(f'Convertido em litros: {L}')
# 19
L = float(input('Digite o volume em litros: '))
M = 1000 * L
print(f'Convertido em metros cúbicos: {M}')
# 21
L = float(input('Digite o valor da massa em libras: '))
K = L * 0.45
print(f'Convertido em quilogramas: {K}')
# 22
J = float(input('Digite o comprimento em jardas: '))
M = 0.91 * J
print(f'Convertido em metros: {M}')
# 23
M = float(input('Digite comprimento em metros: '))
J = M / 0.91
print(f'Convertido em jardas: {J}')
# 24
M = float(input('Digite valor em metros quadrados: '))
A = M * 0.000247
print(f'Convertido em acres: {A}')
# 25
A = float(input('Digite valor em acres: '))
M = A * 4048.58
print(f'Convertido em metros quadrados: {M}')
# 26
M = float(input('Digite o valor da area em metros quadrados: '))
H = M * 0.0001
print(f'Convertido em hectares: {H}')
# 27
H = float(input('Digite o valor em hectares: '))
M = H * 10000
print(f'Convertido em metros quadrados: {M}')
# 28
soma1 = int(input('Primeiro numero: '))
soma2 = int(input('Segundo numero: '))
soma3 = int(input('Terceiro numero: '))
print(f'Soma = {soma1+soma2+soma3}')
# 29
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
nota4 = float(input('Quarta nota: '))
resultado = nota1+nota2+nota3+nota4
print(f'Resultado = {resultado / resultado}')
# 30
real = float(input('Digite o valor em Reais (R$): '))
cot = float(input('Digite a cotação do Dolar: '))
dolar = real * cot
print(f'Valor em Dolar: {dolar}')
# 31
num = int(input('Digite o numero para saber seu antecessor e seu sucessor: '))
print(f'antecessor: {num-1}, sucessor {num+1}')
# 32
num = int(input('Digite numero inteiro: '))
print(f'sucessor: {num+1}, triplo: {num*3}')
# 34
r = 3.141592
raio = float(input('Digite valor do raio: '))
circulo = r * (raio * 2)
print(f'A Area do circulo é {circulo}')
# 35
a = input('Digite o valor a: ')
b = input('Digite o valor b: ')
hipotenusa = (a * 2) + (b * 2)
print(f'O valor da hipotenusa é {hipotenusa}')
# 36
raio = float(input('Digite a raio: '))
altura = float(input('Digite a altura: '))
r = 3.141592
raio = raio * 2
v = (r * raio) * altura
print(f'O volume de um circulo circular é: {v}')
# 37
preco = float(input('Digite o Preço do Produto: R$ '))
porcentagem = 12
novo_preco = (preco * porcentagem) / 100
desconto = preco - novo_preco
print(f'Valor com desconto: R$ {desconto}')
# 38
salario = float(input('Digite o saltário do funcionário: R$ '))
porcentagem = 25
novo_salario = (salario * porcentagem) / 100
aumento = salario + novo_salario
print(f'Novo salário do funcionário: R$ {aumento}')
# 39
print('Premio Toral: R$ 780.000,00\n')
premio = 780000.00
porc1 = 46
porc2 = 32
# Primeiro ganhador
valor1 = (premio * porc1) / 100
ganhador1 = premio - valor1
print(f'O primeiro ganhador recebe: R$ {ganhador1}\n')
# Segundo ganhador
valor2 = (premio * porc2) / 100
ganhador2 = premio - valor2
print(f'O segundo ganhador recebe: R$ {ganhador2}\n')
# Terceiro ganhador
ganhador3 = (ganhador1 + ganhador2) - premio
print(f'O terceiro ganhador recebe: R$ {ganhador3}')
# 40
dias = int(input('Digite o numeros de dias trabalhado: '))
valor = 30.00
descontos = 8
valor_total = dias * valor
impostos = (valor_total * descontos) / 100
pagar = valor_total - impostos
print(f'Valor do serviço com desconto do imposto de renda: R$ {pagar}')
# 41
valor = float(input('Qual o valor da hora trabalhada? '))
hora = float(input('Quantas horas trabalhadas? '))
adicional = 10
total = hora * valor
acrecimos = (total * adicional) / 100
pagar = total + acrecimos
print(f'Valor a ser pago ao funcionário: R$ {pagar}')
# 42
sal_base = float(input('Qual o salário Base: R$ '))
gratificacao = 5
imposto = 7
# Gratificação 5%
adicionar = (sal_base * gratificacao) / 100
print(f'Adicional a receber: R$ {adicionar}')
# Imposto 7%
desconto = (sal_base * imposto) / 100
print(f'Imposto a pagar: R$ {desconto}')
# Resultado
resultado = (sal_base + adicionar) - desconto
print(f'Salário a receber: R$ {resultado}')
# 43
print('Programa para vendedores\n')
valor = float(input('Valor do produto: '))
desc = 10
comis_vista = 5
comis_parc = 5
# Desconto 10%
valor_desc = (valor * desc) / 100
total_desc = valor - valor_desc
print(f'Total a pagar com desconto 10%: R$ {total_desc}')
# Valor da parcela
valor_parc = valor / 3
print(f'Valor de parcelamento em 3x sem juros: R$ {valor_parc}')
# Comissão vendedor venda a vista
comissao1 = (total_desc * comis_vista) / 100
print(f'Comissão vendedor, venda a vista: R$ {comissao1}')
# Comissão vendedor venda parcelada
comissao2 = (valor * comis_parc) / 100
print(f'Comissão vendedor, venda parcelada: R$ {comissao2}')
# Invenção
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
print(f'\nUsuario {nome} logado...\nSeja bem vindo\n!')
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