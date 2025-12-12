def quick_sort(a: list[int]) -> list[int]:
    if len(a) <= 1:
        return a

    left = []
    mid = []
    right = []
    pivot = a[len(a) // 2]

    for elem in a:
        if elem < pivot:
            left.append(elem)
        elif elem > pivot:
            right.append(elem)
        else:
            mid.append(elem)
    return quick_sort(left) + mid + quick_sort(right)