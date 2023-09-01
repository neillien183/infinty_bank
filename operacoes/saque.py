from banco import obterconta, banco

def sacar(conta: int, valor: float) -> None:
    cliente = obterconta(conta)
    if cliente:
        if cliente['saldo'] >= valor:
           cliente['saldo'] = cliente['saldo'] - valor
           print('saque realizado com sucesso')
        else:
           print('saldo insuficiente!')
    else:
        print('cliente não existe!')
if __name__ == '__main__':
    sacar(1, 100)
    print(banco)