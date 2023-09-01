from banco import obterconta, banco

def transferir(contaOri: int, contaDes: int, valor: float) ->None:
    contaOrigem = obterconta(contaOri)
    contaDestino = obterconta(contaDes)
    if contaOrigem and contaDestino:
        if contaOrigem['saldo'] >= valor:
            contaOrigem['saldo'] -= valor
            contaDestino['saldo'] += valor
            print('transferencia realizada!')
        else:
            print('saldo insuficiente!')
    else:
        print('uma ou mais contas não existem!')

if __name__ == '__main__':
    transferir(1, 2, 159.99)
    print(banco)