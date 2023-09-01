from banco import obterconta, banco

def consultarsaldo(conta: int) -> None:
    cliente = obterconta(conta)
    if cliente:
        print(f'saldo: {cliente["saldo"]}')
    else:
        print('conta não existe')

if __name__ == "__main__":
    consultarsaldo(1)
    print(banco)