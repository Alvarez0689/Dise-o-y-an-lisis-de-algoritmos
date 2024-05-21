def MergeSort(a):
    if len(a) > 1:
        mid = len(a) // 2
        left_half = a[:mid]
        right_half = a[mid:]

        MergeSort(left_half)
        MergeSort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a[k] = left_half[i]
                i += 1
            else:
                a[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            a[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            a[k] = right_half[j]
            j += 1
            k += 1

a = [6, 3, 1, 12, 0]
MergeSort(a)

print(a)
