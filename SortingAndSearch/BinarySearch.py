'''  Em uma dada janela de tempo, suponha que os dados
obedeçam ao seguinte padrão: há uma sequência estritamente crescente de número de
infectados, seguida de uma sequência estritamente decrescente. São muitas cidades e
você tem muitos dados, em várias janelas de tempo. Assim, para facilitar a análise dos
dados, você foi solicitado a elaborar um programa que dado os registros diários de
infectados em uma janela de tempo que obedeça ao padrão acima, determina a data em
que ocorreu o maior número de infectados, naquela janela de tempo. Os registros
diários de uma dada janela de tempo estão armazenados em um vetor, em memória
primária. O seu algoritmo deve possuir complexidade O(log n), onde n é a quantidade
de registros diários em uma janela de tempo. '''
import math

def binarySearch(array, left, right):

    middle = math.floor((left + (right-1))/2)

    if array[middle] >= array[middle-1] and (array[middle] >= array[middle+1]):
        return middle

    if (array[middle] >= array[middle-1]) and (array[middle] <= array[middle+1]):
        return binarySearch(array, middle+1, right)
    elif (array[middle] <= array[middle-1]) and (array[middle] >= array[middle+1]):
        return binarySearch(array, left, middle)


if __name__ == '__main__':
    v0 = [1, 2, 8, 32, 64, 128, 122, 50, 30, 12]  # 128
    v1 = [3, 8, 15, 2, 0]  # 15
    v2 = [2, 32, 18, 10, 6]  # 32
    v3 = [2, 5, 8, 25, 10]  # 25

    max = binarySearch(v0, 0, len(v0)-1)
    print(v0[max])

    max = binarySearch(v1, 0, len(v1)-1)
    print(v1[max])

    max = binarySearch(v2, 0, len(v2)-1)
    print(v2[max])

    max = binarySearch(v3, 0, len(v3)-1)
    print(v3[max])
