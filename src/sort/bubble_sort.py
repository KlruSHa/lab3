def bubble_sort(a: list[int]) -> list[int]:
    if not a:
        return []
    for i in range(1, len(a) + 1):
        for j in range(len(a) - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a