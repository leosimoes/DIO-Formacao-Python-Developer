LIMITE_SAQUE_QUANTIDADE = 3
LIMITE_SAQUE_VALOR = 500

operacoes_lista = []
saldo = 0.00
numero_saques = 0
saques = []
depositos = []
opcao = ''

MENU = """
----------------------------------
Selecione uma opção:
[D] Depositar | [S] Sacar | [E] Extrato | [Q] Sair
"""

while opcao != 'Q':
    opcao = input(MENU).upper()

    if opcao == 'D':
        deposito = float(input("Qual o valor do depósito?\n"))
        if deposito <= 0.00:
            print('Valor de depósito inválido.')
        else:
            saldo += deposito
            depositos.append(deposito)
            operacoes_lista.append(f'Depósito de R$ {deposito:.2f}\n')

    elif opcao == 'S':
        saque = float(input("Qual o valor do saque?\n"))
        if numero_saques >= LIMITE_SAQUE_QUANTIDADE:
            print('Quantidade de saques excedida.')
        elif saque > LIMITE_SAQUE_VALOR:
            print('Valor de saque excedido.')
        elif saque <= 0.00:
            print('Valor de saque inválido.')
        elif saque > saldo:
            print('Saldo insuficiente')
        else:
            saldo -= saque
            saques.append(saque)
            numero_saques += 1
            operacoes_lista.append(f'Saque de R$ {saque:.2f}\n')

    elif opcao == 'E':
        print('**********************************\nExtrato\n**********************************')
        if not operacoes_lista:
            print('Não foram realizadas movimentações.')
        else:
            print(''.join(operacoes_lista))
            print(f'Saldo de R$ {saldo:.2f}\n')

    elif opcao == 'Q':
        print('Fim da execução.')
        break

    else:
        print('Escolha uma opção válida !!!')