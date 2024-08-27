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
                    extrato.append({"op": "D", "v": valor})
                    print(
                        f"Depósito de {valor:.2f} adicionado com sucesso a sua conta!")
        case "2":
            pass
        case "3":
            pass
        case "4":
            break
        case _:
            continue
