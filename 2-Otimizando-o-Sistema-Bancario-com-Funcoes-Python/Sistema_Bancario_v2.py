LIMITE_SAQUE_QUANTIDADE = 3
LIMITE_SAQUE_VALOR = 500
AGENCIA = "0001"

MENU = """
----------------------------------
Selecione uma opção:
[D] Depositar | [S] Sacar | [E] Extrato | [U] Criar Usuário | [K] Criar conta | [Q] Sair
"""


# A função saque deve receber os argumentos apenas por nome (keyword only)
def sacar(*, saldo, valor, extrato, limite, numero_saque, limite_saques):
    if numero_saque >= limite_saques:
        print('Quantidade de saques excedida.')
    elif valor > limite:
        print('Valor de saque excedido.')
    elif valor <= 0.00:
        print('Valor de saque inválido.')
    elif valor > saldo:
        print('Saldo insuficiente')
    else:
        saldo -= valor
        numero_saque += 1
        extrato.append(f'Saque de R$ {valor:.2f}\n')

    return saldo, extrato


# A função depósito deve receber os argumentos apenas por posição (positional only)
def depositar(saldo, valor, extrato, /):
    if valor <= 0.00:
        print('Valor de depósito inválido.')
    else:
        saldo += valor
        extrato.append(f'Depósito de R$ {valor:.2f}\n')

    return saldo, extrato


# A função extrato deve receber os argumentos por posição e nome (positional only e keyword only).
# Argumentos posicionais: saldo. | Argumentos nomeados: extrato.
def visualizar_extrato(saldo, /, *, extrato):
    print('**********************************\nExtrato\n**********************************')
    if not extrato:
        print('Não foram realizadas movimentações.')
    else:
        print(''.join(extrato))
        print(f'Saldo de R$ {saldo:.2f}')


def calcular_numero_saques(extrato):
    saques = list(filter(lambda t: t.startswith('Saque de R$'), extrato))
    return len(saques)


def cadastrar_usuario(usuarios):
    cpf = input('Digite o cpf do usuário: ')
    if consulta_usuario(usuarios, cpf):
        print('Já existe um usuário com o cpf informado.')
    else:
        print('Informe os outros dados do usuário:')
        nome = input('Nome: ')
        endereco = input('Endereco: ')
        data_nascimento = input('Data de Nascimento: ')

        usuario = {'CPF': cpf, 'Nome': nome, 'Endereco': endereco, 'Data de Nascimento': data_nascimento}
        usuarios.append(usuario)
        print('Usuário cadastrado.')

    return usuarios


def consulta_usuario(usuarios, cpf):
    return list(filter(lambda u: u.get('CPF') == cpf, usuarios))


def cadastrar_conta_bancaria(agencia, numero_conta, usuarios, contas):
    cpf = input('Digite o cpf do usuário: ')
    usuario = consulta_usuario(usuarios, cpf)
    if usuario:
        conta = {'CPF do usuario': cpf, 'Agencia': agencia, 'Numero da Conta': numero_conta}
        contas.append(conta)
        print('Conta criada.')
    else:
        print('Usuário não cadastrado.')
        print('A conta não foi criada.')
    return contas


def exibir_menu(menu):
    return input(menu).upper()


def main():
    extrato = []
    saldo = 0.00
    numero_saques = 0
    usuarios = []
    contas = []

    opcao = exibir_menu(MENU)
    while opcao != 'Q':

        if opcao == 'D':
            deposito = float(input("Qual o valor do depósito?\n"))
            # numero de depositos = ()
            saldo, extrato = depositar(saldo, deposito, extrato)

        elif opcao == 'S':
            saque = float(input("Qual o valor do saque?\n"))

            saldo, extrato = sacar(saldo=saldo, valor=saque, extrato=extrato, limite=LIMITE_SAQUE_VALOR,
                                   numero_saque=numero_saques, limite_saques=LIMITE_SAQUE_QUANTIDADE)

            numero_saques = calcular_numero_saques(extrato)

        elif opcao == 'E':
            visualizar_extrato(saldo, extrato=extrato)

        elif opcao == 'U':
            usuarios = cadastrar_usuario(usuarios)

        elif opcao == 'K':
            numero_conta = len(contas) + 1
            contas = cadastrar_conta_bancaria(AGENCIA, numero_conta, usuarios, contas)

        elif opcao == 'Q':
            print('Fim da execução.')
            break

        else:
            print('Escolha uma opção válida !!!')

        opcao = exibir_menu(MENU)


if __name__ == '__main__':
    main()
