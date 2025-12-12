from insertion_sort import insertion_sort


def bucket_sort(a: list[float], base: int = 10) -> list[float]:
    if not a:
        return []
    mini = min(a)
    maxi = max(a)
    d = maxi - mini

    if d == 0:
        return a

    bins = [[] for _ in range(base)]

    for elem in a:
        norm = (elem - mini) / d
        idx = int(base * norm)
        if idx == base:
            idx -= 1
        bins[idx].append(elem)

    a = []
    for b in bins:
        insertion_sort(b)
        for elem in b:
            a.append(elem)
    return a
