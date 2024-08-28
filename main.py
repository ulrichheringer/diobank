# Constantes
LIMITE_POR_SAQUE = 500.0
LIMITE_SAQUES = 3

# Operacoes permitidas
operacoes = """
[1] - Deposito
[2] - Saque
[3] - Extrato
[4] - Sair
Digite uma opcao: """

saldo = 0
# Array de Dicionarios, para guardar o extrato
extrato = []

while True:
    option = input(operacoes)

    match option:
        case "1":
            while True:
                valor = float(
                    input("Por favor digite um valor para o depósito: "))
                if valor < 0:
                    print("Por favor, digite um valor maior do que R$0")
                    continue
                else:
                    saldo += valor
                    extrato.append({"op": "D", "v": valor})
                    print(
                        f"Depósito de R${valor:.2f} adicionado com sucesso a sua conta!")
                    break
        case "2":
            while True:
                saques_diarios = 0
                if extrato:
                    for i in extrato:
                        if i["op"] == "S":
                            saques_diarios += 1
                        else:
                            continue
                if saques_diarios == 3:
                    print("O limite de saques diarios foi atingido!")
                    break
                valor = float(input("Digite o quanto voce quer sacar: "))
                if valor < 0:
                    print("Por favor, digite um valor maior do que zero")
                    continue
                if valor > LIMITE_POR_SAQUE:
                    print(
                        f"O valor digitado para o saque é maior do que o limite permitido por saque. O valor ultrapassou R${(valor-LIMITE_POR_SAQUE):.2f} do limite!")
                    continue
                elif valor > saldo:
                    print("Voce nao tem saldo suficiente para concluir esta operacao.")
                    break
                else:
                    saldo -= valor
                    extrato.append({"op": "S", "v": valor})
                    print(
                        f"R${valor:.2f} sacados com sucesso da sua conta!")
                    break
        case "3":
            if extrato:
                for i in extrato:
                    if i["op"] == "S":
                        print(f'SAQUE -> -R${i["v"]:.2f}')
                        continue
                    print(f'DEPOSITO -> +R${i["v"]:.2f}')
                print(f"Balanço geral: R${saldo:.2f}")
        case "4":
            print("Saindo...")
            break
        case _:
            print("Opçao invalida, por favor digite novamente.")
            continue
