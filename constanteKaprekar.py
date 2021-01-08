import numpy as np
def aplanar(vector):
    a = ''
    for element in vector:
        a = a+str(element) 
    return(int(a))
def agregarCeros(vector):
    if len(vector) < 4:
        vector += '0' * (4 - len(vector))
    return vector
def orde(vector):
    vector = agregarCeros(vector)
    return[aplanar(list(np.sort(vector))),aplanar(list(np.sort(vector))[::-1])]
def restaRecursiva(vector,count):
    count=count+1
    print("A restar: ",vector,count)
    resta = abs(vector[0] - vector[1])
    if abs(resta) == 6174:
        print(count)
    else:
        restaRecursiva(orde([int(x) for x in str(resta)]),count)
def kaprekar(num):
    count = 0
    if str(num) == str(num)[::-1]:
        return 8
    elif num==6174:
        return 0
    else:
        return restaRecursiva(orde([int(x) for x in str(num)]),count)
kaprekar(99)