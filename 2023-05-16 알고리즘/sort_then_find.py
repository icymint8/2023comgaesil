def find_two_smallest(L):
    """리스트 L에서 가장 작은 두 값의 인덱스를 튜플로 반환한다.

    >>> counts = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(counts)
    (6, 7)
    """

    # 리스트 맨 앞에 가장 작은 두 수가 오도록 리스트를 정렬한 복사본을 구한다.
    sorted_L = sorted(L)

    # 원래 리스트 L에서 두 수의 인덱스를 구한다.
    fir_min_ind = L.index(sorted_L[0])
    sec_min_ind = L.index(sorted_L[1])

    return fir_min_ind, sec_min_ind

