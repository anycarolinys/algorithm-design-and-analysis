''' Suponha que você tenha um ranking dos x filmes mais populares em uma rede social,
obtido através da votação de todos os membros. Assim, cada filme f tem um código
inteiro único c e um valor p a ele associado, 1 ≤ p ≤ x, que denota sua posição neste
ranking. O arquivo está ordenado pelo ranking. Não existem valores nem de c e nem de
p duplicados. Você também tem acesso a um arquivo de membros da rede social, que
inclui, para cada membro m, a ordem de preferência de m em relação a estes x filmes, na
forma de sequência dos códigos dos filmes, listados do mais preferido por m para o
menos preferido. Você pode supor que este arquivo cabe em memória primária. Por
exemplo, considerando a informação (c, f, p) e apenas três filmes (x = 3),
Seu objetivo é gerar um arquivo em que ordenará os membros da rede social pelo índice
de discrepância do membro em relação ao ranking estipulado por todos, em ordem
crescente do índice de discrepância. O índice de discrepância de uma pessoa é a
quantidade de pares (i, j), tal que i > j, considerando os x dados de ranking da pessoa,
que são na realidade, uma permutação do ranking global. Entretanto, o cálculo do índice
de discrepância de um membro m precisa ser calculado no tempo de O(x log x). '''

from Entities import Member, Movie
from HashTable import HashTable
import math


def mergeSortDiscrepancy(arr, n):
    temp = [0]*n
    return mergeSorting(arr, temp, 0, n-1)


def mergeSorting(arr, temp, left, right):

    discrepancy = 0

    if left < right:

        middle = (left + right)//2

        discrepancy += mergeSorting(arr, temp,
                                    left, middle)
        discrepancy += mergeSorting(arr, temp,
                                    middle + 1, right)

        discrepancy += merge(arr, temp, left, middle, right)
    return discrepancy


def merge(arr, temp, left, middle, right):
    i = left
    j = middle + 1
    k = left
    discrepancy = 0

    while i <= middle and j <= right:

        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            # Contabilizanod inversão
            discrepancy += (middle-i + 1)
            k += 1
            j += 1

    while i <= middle:
        temp[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]

    return discrepancy


def mergeSortMembers(V):

    if len(V) > 1:

        middledle = math.floor(len(V)/2)
        L = []
        R = []

        for i in range(0, middledle):
            L.append(V[i])

        for j in range(middledle, len(V)):
            R.append(V[j])

        mergeSortMembers(L)

        mergeSortMembers(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            # Os membros são ordenados pelo
            # seu atributo de discrepancia
            if L[i].discrepancy <= R[j].discrepancy:
                V[k] = L[i]
                i += 1
            else:
                V[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            V[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            V[k] = R[j]
            j += 1
            k += 1


def hashingCode(ranking, x):
    HT = HashTable(x)

    for i in range(x):
        HT.put(ranking[i].code, ranking[i].rank)

    return HT


def memberRanking(member: Member, HT):

    moviesRanking = []

    for i in range(len(member.ranking)):
        moviesRanking.append(HT.get(member.ranking[i]))

    return moviesRanking


if __name__ == '__main__':

    # Quantidade de filmes
    x = 3

    # Instanciando os filmes
    movie1 = Movie(109, "Cinema Paradiso", 1)
    movie2 = Movie(15, "Tomates Verdes Fritos", 2)
    movie3 = Movie(1180, "O Marido da Cabelereira", 3)

    # Criando um vetor de filmes por ordem
    # de posicao no ranking
    originalRanking = [movie1, movie2, movie3]

    # Relacionando o codigo do filme
    # com sua posicao no ranking
    # usando hashtable
    HT = hashingCode(originalRanking, x)

    y = 4  # members

    # Instanciando os membros
    member1 = Member("Maria", [1180, 109, 15])
    member2 = Member("Joao", [109, 15, 1180])
    member3 = Member("Ana", [1180, 15, 109])
    member4 = Member("Ivo", [109, 1180, 15])

    # Criando um vetor de membros
    members = [member1, member2, member3, member4]

    # Imprimindo nome e ranking de filmes
    # por codigo
    for i in range(y):
        print(f'({members[i].name}, ', end='')
        print(members[i].ranking, end=')')
        print()

    print()
    # Imprimindo nome, ranking dos filmes
    # por posicao no ranking original,
    # e discrepancia do ranking dos membros
    for i in range(y):
        movieRanking = memberRanking(members[i], HT)
        print(f'{members[i].name}')
        print(f'Ranking: {movieRanking}')
        discrepancy = mergeSortDiscrepancy(movieRanking, len(movieRanking))
        members[i].discrepancy = discrepancy
        print(f'Discrepancia: {members[i].discrepancy}')

    # Ordenando membros por discrepancia
    mergeSortMembers(members)

    print()
    # Imprimindo nome, ranking dos filmes
    # por codigo e discrepancia
    # dos membros ordenados
    for i in range(y):
        print(f'({members[i].name}, ', end='')
        print(members[i].ranking, end=', ')
        print(members[i].discrepancy, end=')')
        print()
