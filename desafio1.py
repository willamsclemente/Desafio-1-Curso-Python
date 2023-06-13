menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo+= valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou:o valor informado é inválido.")

    elif opcao == 's':
        valor = float(input("Informe o valor do saque: "))
    
        if valor > saldo:
            print("Operação falhou: Você não tem saldo suficiente.")
        elif valor > limite:
            print("Operação falhou: O valor do saque excedeu o limite.")
        elif numero_saques >= LIMITE_SAQUE:
            print("Operação falhou: Número de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou: Valor informado é invaálido.")
    
    elif opcao == 'e':
        print("\n========== EXTRATO ==========\n")
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("\n=============================")
    
    elif opcao == 'q':
        break;

    else:
        print("Operação inválida: Por favor selecione novamente a operação desejada.")