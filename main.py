LIMITE_VALOR_SAQUE = 500
LIMITE_SAQUES = 3
saldo = 0
extrato = []
numero_saque = 0

menu = """
****** MENU ******

[d] Depositar
[s] Saque
[e] Extrato
[q] Sair
******************
"""
def solicita_valor():
    valor_inputado = float(input("Digite Valor:"))
    print("\n")
    return valor_inputado

def verifica_valor(valor):
    nao_valido = valor <= 0
    
    if nao_valido:
        print("Digite um valor válido.")
    
    return nao_valido

def deposita():
    global saldo
    valor = solicita_valor()

    if verifica_valor(valor):
       return
    
    saldo += valor
    resgistra_operacao(valor, True)
    
def saca():
    global saldo
    valor = solicita_valor()

    if verifica_valor(valor):
        return
    
    if numero_saque >= LIMITE_SAQUES:
        print("Limite saque atingido.")
        return
    
    if valor > saldo:
        print("Não possui saldo suficiente.")
        return

    if valor > LIMITE_VALOR_SAQUE:
        print("O valor ultrapassou o limete do saque")
        return

    saldo -= valor
    resgistra_operacao(valor, False)

def imprime_extrato():

    if len(extrato) == 0:
        print("Não foram realizadas movimentações.")

    for operacao in extrato:
        print(operacao)

    print(f"Saldo atual R$ {saldo:,.2f}")

def resgistra_operacao(valor, deposito):
    global numero_saque

    if deposito:
        extrato.append(f"R$ {valor:,.2f}")
    else:
        numero_saque += 1
        extrato.append(f"R$ -{valor:,.2f}")

while True:
    opcao = input(menu)

    if opcao == "d":
        deposita()

    elif opcao == "s":
        saca()

    elif opcao == "e":
        imprime_extrato()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor slecione novamente a operação desejada.")
        

