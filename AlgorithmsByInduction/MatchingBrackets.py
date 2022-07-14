''' MATCHING BRACKETS
Dada uma expressão contendo parênteses, literais e operadores aritméticos, elabore um
algoritmo para determinar se a expressão está com os parênteses balanceados, ou seja,
se para cada parêntese aberto há um parêntese fechando e se os pares de parênteses
estão adequadamente aninhados. Você pode supor que a expressão será fornecida como
uma string e que a reposta de seu algoritmo será um booleano, onde True significa que a
expressão é correta e False, incorreta.
    Ex: ((a + b) + (c * d)) é uma expressão correta
    (( a + b) + 1 é uma expressão incorreta
    ) (a + b)) + (c * d) é uma expressão incorreta '''

from Stack import Stack

def testaExpressao(expressao):
    stack = Stack()
    for e in expressao:
        if e == '(':
            stack.append(e)
        elif e == ')' and stack.isEmpty():
            return False
        elif e == ')':
            stack.pop()

    return stack.isEmpty()


if __name__ == '__main__':
    e1 = "((a + b) + (c * d))"
    e2 = "(( a + b) + 1"
    e3 = ")(a + b)) + (c * d)"
    e4 = "( ( ( ) ) ) ) ( "

    print(testaExpressao(e1))
    print(testaExpressao(e2))
    print(testaExpressao(e3))
    print(testaExpressao(e4))