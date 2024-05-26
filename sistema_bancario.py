menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


"""

saldo = 0
limite_valor = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)

    if opcao == "d":

        valor = float(input("Digite o valor para depósito: "))

        if valor > 0:
           saldo += valor
           extrato += f"Depósito: R$ {valor:.2f}\n"

        else: 
            print("Ops, algo deu errado! O valor informado é inválido.")


    elif opcao == "s":
          
        valor = float(input("Digite o valor do saque: "))

        saldo_insuficiente = valor > saldo

        exedeu_limite = valor > limite_valor

        exedeu_saques = numero_saques >= LIMITE_SAQUES

        if saldo_insuficiente:
            print("Ops, algo deu errado! Você não tem saldo suficiente.")
        
        elif exedeu_limite:
            print("Ops, algo deu errado! O valor do saque exede o limite.")
        
        elif exedeu_saques:
            print("Ops, algo deu errado! Numero máximo de saques exedido.")

        elif valor > 0:
             saldo -= valor
             extrato += f"Saque: R$ {valor:.2f}\n"
             numero_saques += 1


        else:
            print("Operação falhou, valor digitado é inválido.")         


      
    elif opcao == "e":

        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")


        
    elif opcao == "q":
         break
    
    else:
         print("Operação invalida, por favor selecione novamente a operação desejada.")
