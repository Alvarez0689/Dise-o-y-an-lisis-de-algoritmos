
def Seleccion(a):
    n = len(a)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

a = [15, 20, 9, 18, 0]
Seleccion(a)

print(a)
