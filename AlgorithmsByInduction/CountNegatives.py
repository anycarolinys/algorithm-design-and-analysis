''' Dado um vetor de inteiros de n elementos, elabore um algoritmo para determinar
quantos destes números são negativos '''

def countNegatives(v, n):
    neg = 0
    if n < 0: # Caso base
        return neg

    neg = countNegatives(v, n - 1) # HI

    if v[n] < 0: # Caso geral
        neg += 1

    return neg

if __name__ == '__main__':
    array0 = [1,2,3,4,5,6,7,8,9,10] 
    array1 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
    array2 = [1,2,3,4,5,6,7,8,9,-10]
    array3 = [-1,2,3,4,5,6,7,8,9,10]
    array4 = [1,2,3,4,-5,6,7,-8,9,10]
    
    negatives = countNegatives(array0, len(array0)-1)
    print(f'{negatives} NEGATIVE VALUE(S)')
    
    negatives = countNegatives(array1, len(array1)-1)
    print(f'{negatives} NEGATIVE VALUE(S)')
    
    negatives = countNegatives(array2, len(array2)-1)
    print(f'{negatives} NEGATIVE VALUE(S)')
    
    negatives = countNegatives(array3, len(array3)-1)
    print(f'{negatives} NEGATIVE VALUE(S)')
    
    negatives = countNegatives(array4, len(array4)-1)
    print(f'{negatives} NEGATIVE VALUE(S)')