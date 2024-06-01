import textwrap


def menu():
    menu = """\n
    
    ================= MENU ===================  

    [d]\tDepósito
    [s]\tSaque
    [e]\tExtrato
    [nu]\tNovo Usuário
    [nc]\tNova Conta
    [lc]\tListar Contas
    [q]\tSair

    => """
    return input(textwrap.dedent(menu))


def deposito(saldo, valor, extrato, /):
     
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \tR$ {valor:.2f}\n"
        print(f"Depósito no valor R$ {valor:.2f} realizado com sucesso.")
 
    else: 
        print("Ops, algo deu errado! O valor informado é inválido.")
 
    return saldo, extrato


def saque(*, saldo, valor, extrato, limite_valor, numero_saques, limite_saques):

    saldo_insuficiente = valor > saldo

    exedeu_limite = valor > limite_valor

    exedeu_saques = numero_saques >= limite_saques

    if saldo_insuficiente:
        print("Ops, algo deu errado! Você não tem saldo suficiente.")
        
    elif exedeu_limite:
        print("Ops, algo deu errado! O valor do saque exede o limite.")
        
    elif exedeu_saques:
        print("Ops, algo deu errado! Numero máximo de saques exedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: \t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso")


    else:
        print("Operação falhou, valor digitado é inválido.")   

    return saldo, extrato



def exibir_extrato(saldo, /, *, extrato):

     print("================ EXTRATO =================")
     print("Não foram realizadas movimentações." if not extrato else extrato)
     print(f"\nSaldo:\t\tR$ {saldo:.2f}")
     print("==========================================")
     


def filtrar_usuario(cpf, usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    
    return usuarios_filtrados[0] if usuarios_filtrados else None



def novo_usuario(usuarios):

    cpf = input("Digite o numero do cpf por favor (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
      print(" Ops, algo deu errado ! Já existe usuario com este CPF")
      
      return
    
    nome = input("Informe o nome completo por favor: ")
    data_nascimento = input("Informe a data de nascimento por favor (dd-mm-aaaa): ") 
    endereco = input("Informe o endereço por favor (logradouro, nro - bairro - cidade/sigla estado: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
 
    print("Usuário criado com sucesso !")


def nova_conta(agencia, numero_conta, usuarios):

    cpf = input("Informe o CPF por favor: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Ops, algo deu errado! Usuário não encontrado")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
              Agência:\t{conta['agencia']}
              C/C:\t\t{conta['numero_conta']}
              Titular:\t{conta['usuario']['nome']}
        """

        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"    
    
    saldo = 0
    limite_valor = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []


    while True:

        opcao = menu()

        if opcao == "d":

           valor = float(input("Digite o valor para depósito: "))

           saldo, extrato = deposito(saldo, valor, extrato)           


        elif opcao == "s":
          
            valor = float(input("Digite o valor do saque: "))
             
            saldo, extrato = saque(
                saldo= saldo,
                valor= valor,
                extrato= extrato,
                limite_valor= limite_valor,
                limite_saques= LIMITE_SAQUES,
                numero_saques= numero_saques,
            )

              
        elif opcao == "e":

            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            novo_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "q":
            break
    
        else:
         print("Operação invalida, por favor selecione novamente a operação desejada.")

main()