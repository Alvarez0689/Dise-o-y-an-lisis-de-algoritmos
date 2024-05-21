def BubbleSort(a):
    n = len(arreglo)

    for i in range(n-1): 
        for j in range(n-1-i): 
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

a = [5, 2, 1, 15, 0]
BubbleSort(arreglo)

print(arreglo)
