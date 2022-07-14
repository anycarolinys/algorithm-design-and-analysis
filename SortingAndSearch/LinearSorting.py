import collections

def ordenacaoLinear(V, n):
    # Vetor extra para os valores ordenados
    N = []

    for i in range(n):
        if V[i].chave < 0:
            N.append(V[i])

    for i in range(n):
        if V[i].chave == 0:
            N.append(V[i])

    for i in range(n):
        if V[i].chave > 0:
            N.append(V[i])

    # Retorna o vetor ordenado
    return N


if __name__ == '__main__':

    Registro = collections.namedtuple('Registro', ['chave', 'dados'])
    r1 = Registro(0, 'a')
    r2 = Registro(-1, 'b')
    r3 = Registro(1, 'c')
    r4 = Registro(0, 'd')
    r5 = Registro(0, 'e')
    r6 = Registro(-1, 'f')
    r7 = Registro(1, 'g')
    r8 = Registro(-1, 'h')
    r9 = Registro(-1, 'i')

    r1 = [r1, r2, r3, r4, r5, r6, r7, r8, r9]
    sortedRegisters = ordenacaoLinear(r1, len(r1))

    for i in range(len(sortedRegisters)):
        print(sortedRegisters[i].chave, sortedRegisters[i].dados)
