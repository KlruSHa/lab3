from src.errors import NonIntegerError


def counting_sort(a: list[int]) -> list[int]:
    if not a:
        return []
    for elem in a:
        if not isinstance(elem, int):
            raise NonIntegerError("Counting Sort", type(elem))

    maxi = max(a)
    mini = min(a)
    k = maxi - mini + 1
    c = [0] * k
    res = []

    for elem in a:
        c[elem - mini] += 1
    for i in range(len(c)):
        count = c[i]
        for j in range(count):
            res.append(i + mini)
    return res
