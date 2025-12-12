def heap_sort(a: list[int]) -> list[int]:
    if not a:
        return []

    def sift(n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and a[l] > a[largest]:
            largest = l

        if r < n and a[r] > a[largest]:
            largest = r

        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            sift(n, largest)

    n = len(a)

    for i in range(n // 2 - 1, -1, -1):
        sift(n, i)

    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        sift(i, 0)

    return a
