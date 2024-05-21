def inserccion(a):
    n = len(a)

    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

a = [10, 5, 1, 20, 0]
inserccion(a)

print(a)
