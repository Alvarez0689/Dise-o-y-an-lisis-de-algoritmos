def QuickSort(a, low, high):
    if low < high:
        pi = partir(a, low, high)
        QuickSort(a, low, pi - 1)
        QuickSort(a, pi + 1, high)

def partir(a, low, high):
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1

a = [6, 3, 1, 12, 0]
QuickSort(a, 0, len(a) - 1)

print(a)
