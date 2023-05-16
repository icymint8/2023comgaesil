def find_two_smallest(L):
    """리스트 L에서 가장 작은 두 값의 인덱스를 튜플로 반환한다.

    >>> counts = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(counts)
    (6, 7)
    """

    # L의 맨 앞부분에서 가장 작은 값과 두 번째로 작은 값의 인덱스를 
    # min1과 min2에 할당한다.
    min1 = 0 if L[0] < L[1] else 1
    min2 = 0 if min1 else 1
    len_L = len(L)
    if len_L < 3:
        return min1, min2

    # 리스트 내 각 값을 순서대로 확인한다.
    for i in range(2, len(L)):
        # L[i]는 min1과 min2보다 작거나, 둘 사이거나, 둘보다 크다.
        # 가장 작은 값을 새로 찾았을 때
        if L[i] < L[min1]:
            min1, min2 = i, min1

        # 두 번째로 작은 값을 새로 찾았을 때
        elif L[i] < L[min2]:
            min2 = i

    return min1, min2


