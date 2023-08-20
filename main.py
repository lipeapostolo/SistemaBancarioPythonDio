#Passgem parametro por posição
def deposita(saldo, extrato, /):
    valor = solicita_valor()
    if verifica_valor(valor):
        print("\n### Operação falhou! O valor informado é inválido. ###")
        return

    saldo += valor
    extrato.append(f"Depósito: R$ {valor:.2f}")
    print("\n*** Depósito realizado com sucesso! ***") 
    
    return saldo, extrato

#Passagem por nome
def saca(*, saldo, extrato, limite, numero_saques, limite_saques):
    valor = solicita_valor()
    if verifica_valor(valor):
        return saldo, extrato, numero_saques
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("#### Você não tem saldo suficiente. ####")
        return saldo, extrato, numero_saques

    elif excedeu_limite:
        print("#### O valor do saque excede o limite. ####")
        return saldo, extrato, numero_saques

    elif excedeu_saques:
        print("#### Número máximo de saques excedido. ####")
        return saldo, extrato, numero_saques
    
    saldo -= valor
    numero_saques += 1
    print("### Saque realizado com sucesso! ###")
    extrato.append(f"R$ -{valor:,.2f}")

    return saldo, extrato, numero_saques

#Passagem do parametro posição e por nome
def imprime_extrato(saldo, /, *, extrato):
    print("*********** EXTRATO ***********")
    if len(extrato) == 0:
        print("Não foram realizadas movimentações.")

    for operacao in extrato:
        print(operacao)

    print(f"Saldo atual R$ {saldo:,.2f}")
    print("*******************************")

def solicita_valor() -> float:
    valor_inputado = float(input("Digite Valor:"))
    print("\n")
    return valor_inputado

def verifica_valor(valor) -> bool:
    nao_valido = valor <= 0
    
    if nao_valido:
        print("Digite um valor válido.")
    
    return nao_valido

def busca_usuario(cpf, usuarios):
    usuarios_encontrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_encontrados[0] if usuarios_encontrados else None

def cria_usuario(usuarios):
    cpf = pede_cpf()
    usuario = busca_usuario(cpf, usuarios)

    if(usuario):
        print(" O usuário já existe")
        return
    
    nome = input("Informe o nome: ")
    data_nascimento =  input("Informe a data de nascimento(DD/MM/AAAA): ")
    endereco = input("Informe o endereço: ")

    usuarios.append({"nome":nome, "cpf":cpf, "data_nascimento":data_nascimento, "endereco":endereco})

    print(" ##### Usuario cadastrado com sucesso ##### ")

def pede_cpf() -> str:
    return input("Informe o cpf")

def cria_conta(agencia, contas, usuarios):
    numero_conta = len(contas) + 1

    cpf = pede_cpf()
    usuario = busca_usuario(cpf, usuarios)

    if usuario:
        contas.append({"agencia": agencia, "numero_conta":numero_conta, "usuario":usuario })
        print("Conta criada com sucesso")

def main():
    LIMITE_VALOR_SAQUE = 500
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    extrato = []
    numero_saques = 0
    usuarios = []
    contas = []

    menu = """
    ****** MENU ******

        [d]  Depositar
        [s]  Saque
        [e]  Extrato
        [nc] Nova conta
        [nu] Novo usuário
        [q]  Sair
    ******************
    """

    while True:
        opcao = input(menu)

        if opcao == "d":
            saldo, extrato = deposita(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = saca(saldo=saldo, extrato=extrato, limite=LIMITE_VALOR_SAQUE, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == "e":
            imprime_extrato(saldo, extrato=extrato)

        elif opcao == "nc":
            cria_conta(AGENCIA, contas, usuarios)

        elif opcao == "nu":
            cria_usuario(usuarios)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor slecione novamente a operação desejada.")
            
main()
