''' Dados dois vetores de inteiros ordenados em ordem crescente, gere um terceiro vetor
com os dados dos vetores de entrada também ordenados em ordem crescente, mas sem
elementos repetidos '''

def uniaoOrdenada(v1, v2):              
    uniao = []
    n1 = len(v1)
    n2 = len(v2)
    i, j = 0, 0
    
    while i < n1 and j < n2:
        if v1[i] < v2[j]:
            uniao.append(v1[i])    
            i += 1 
        elif v1[i] > v2[j]:    
            uniao.append(v2[j])    
            j += 1 
        else:    
            uniao.append(v1[i])    
            i += 1    
            j += 1

    while i < n1:  
        uniao.append(v1[i])  
        i += 1
    
    while j < n2:  
        uniao.append(v2[j])  
        j += 1
    
    return uniao


if __name__ == "__main__":
    v1 = [-6, 0,3,8,9,10,15]
    v2 = [-1, 0,2,3]
    v = uniaoOrdenada(v1, v2)

    print('Array 1:', v1)
    print('Array 2:', v2)
    print('Union:', v)
    print()

    v1 = [8, 24, 72,80,81,100,150,158]
    v2 = [-10, -5, 0,24,81,150,200,250]
    v = uniaoOrdenada(v1, v2)

    print('Array 1:', v1)
    print('Array 2:', v2)
    print('Union:', v)
    print()

    v1 = [-6, 3,8,9,10,15]
    v2 = [-1, 0,2,3]
    v = uniaoOrdenada(v1, v2)

    print('Array 1:', v1)
    print('Array 2:', v2)
    print('Union:', v)
    print()
