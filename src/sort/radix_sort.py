from src.errors import NonIntegerError


def radix_sort(a: list[int], base: int = 10) -> list[int]:
    if not a:
        return []
    for elem in a:
        if not isinstance(elem, int):
            raise NonIntegerError("Radix Sort", type(elem))

    bins = [[] for _ in range(base)]
    maxi = len(str(max(a)))

    for i in range(0, maxi):
        for elem in a:
            digit = (elem // (base ** i)) % base
            bins[digit].append(elem)
        a = []
        for i in bins:
            for j in i:
                a.append(j)

        bins = [[] for _ in range(base)]
    return a