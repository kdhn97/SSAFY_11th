def solution(sizes):
    max_i = 0
    max_j = 0
    for size in sizes:
        i, j = size

        if i < j:
            i, j = j, i

        if max_i < i:
            max_i = i

        if max_j < j:
            max_j = j

    result = max_i * max_j
    return result