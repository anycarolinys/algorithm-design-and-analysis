def intersecaoArbitraria(v1, v2):
    intersecao=[]
    i,j = 0,0  
    n1=len(v1)
    n2=len(v2)

    for i in range(n1):
        for j in range(n2):
            if v1[i] == v2[j]:
                intersecao.append(v1[i])

    return intersecao

if __name__ == "__main__":
    v1=[15,10,9,8,3,0,-6]
    v2=[3,2,0,-1]
    v = intersecaoArbitraria(v1, v2)

    print('Array 1:', v1)
    print('Array 2:', v2)
    print('Intersection:', v)
    print()    

    v1 = [158,150,100,81,80,72,24,8]
    v2 = [250,200,150,81,24,0,-5,-10]
    v = intersecaoArbitraria(v1, v2)

    print('Array 1:', v1)
    print('Array 2:', v2)
    print('Intersection:', v)
    print()    

    v1=[15,10,9,8,3,-6]
    v2=[-1,0,2,3]
    v = intersecaoArbitraria(v1, v2)

    print('Array 1:', v1)
    print('Array 2:', v2)
    print('Intersection:', v)
    print()    