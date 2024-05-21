def BubbleSort(a):
    n = len(a)

    for i in range(n-1): 
        for j in range(n-1-i): 
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

a = [5, 2, 1, 15, 0]
BubbleSort(a)

print(a)
