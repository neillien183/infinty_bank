banco = [
    {"conta": 1, "nome": "Mariana", "saldo": 159.99},
    {"conta": 2, "nome": "Jonas", "saldo": 205.50}
]
conta_atual = 2
def adicionarConta(nome: str, saldo: float) -> None:
    global conta_atual
    conta_atual += 1
    cliente = {
        "conta": conta_atual,
        "nome": nome,
        "saldo": saldo
    }
    banco.append(cliente)
    print('Cliente cadastrado com sucesso!')

def obterconta(conta: int) -> dict or None:
    for cliente in banco:
        if cliente['conta'] == conta:
            return cliente
    return None
def deletarconta(conta: int) -> None:
    cliente = obterconta(conta)
    if cliente != None:
        banco.remove(cliente)
        print(cliente)
    else:
        print('cliente não existe!')
def editarNome(novoNome: str, conta: int) -> None:
    cliente = obterconta(conta)
    if cliente:
        cliente['nome'] = novoNome
        print('dados alterados com sucesso')
    else:
        print('cliente não existe!')

def consultarcliente(conta: int) -> None:
    cliente = obterconta(conta)
    if cliente:
        print(f"n. conta: {conta}")
        print(f"cliente: {cliente['nome']}")
        print(f"saldo: {cliente['saldo']}")
    else:
        print('cliente não existe')

def listartodasconta() -> None:
    for cliente in banco:
        consultarcliente(cliente['conta'])
        print('________________')







if __name__ == "__main__":
   listartodasconta()
