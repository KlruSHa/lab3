def insertion_sort(b):
    if not b:
        return []
    for i in range(1, len(b)):
        key = b[i]
        j = i - 1
        while j >= 0 and key < b[j]:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = key
