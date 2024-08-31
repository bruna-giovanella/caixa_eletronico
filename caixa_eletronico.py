
saldo = 1000
deposito = 0
saque = 0
action = 0

flag = True

while flag == True: 
    print('\n1- Visualizar saldo\n2- Depositar Dinheiro\n3- Sacar dinheiro\n4- Sair\n')
    action = input('Escolha uma opção (1-4): ')

    # 1- Visualizar saldo
    if action == '1':
        print(f'Saldo em conta: R$ {saldo:.2f}')
        voltar = input('Voltar ao menu? (s/n) ').lower()

        while voltar != 's':
            if voltar == 'n':
                print('Saindo...')
                flag = False
                break
            else:
                voltar = input('Informe um valor válido\nVoltar ao menu? (s/n) ').lower()

    # 2- Depositar Dinheiro
    elif action == '2':
        deposito = 0

        while deposito <= 0:
            deposito = int(input('Informe o valor para depósito: R$ '))
            if deposito <= 0:
                voltar = input('Valor inválido\nVoltar ao menu? (s/n) ').lower()
                if voltar == 'n':
                    voltar1 = input('Deseja informar um novo valor para depósito? (s/n) ')
                    if voltar1 == 's':
                        deposito = int(input('Informe o valor para depósito: R$ '))
                    else:
                        print('Saindo...')
                        flag = False
                        break
                elif voltar == 's':
                    break
        saldo += deposito

    # 3- Sacar dinheiro
    elif action == '3':
        saque = 0

        while saque == 0:
            saque = int(input('Informe o valor para saque: R$ '))
            while saque > saldo:
                voltar = input('Valor inválido\nVoltar ao menu? (s/n) ').lower()
                if voltar == 'n':
                    voltar1 = input('Deseja informar um novo valor para saque? (s/n) ')
                    if voltar1 == 's':
                        saque = int(input('Informe o valor para saque: R$ '))
                    else:
                        print('Saindo...')
                        flag = False
                        break
                elif voltar == 's':
                    break
        saldo -= saque

    elif action == '4':
        print('Saindo...')
        flag = False
