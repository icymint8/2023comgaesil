def find_two_smallest(L):
    # 리스트 L에서 가장 작은 두 값의 인덱스를 튜플로 반환한다.
    # counts = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    # find_two_smallest(counts)
    # (6, 7)

    # 가장 작은 항목의 인덱스를 구해서 그 항목을 삭제한다.
    fir_min = min(L)
    fir_min_ind = L.index(fir_min)
    L.remove(fir_min)

    # 다음으로 가장 작은 항목의 인덱스를 구한다.
    sec_min_ind = L.index(min(L))

    # 가장 작은 항목을 L에 다시 넣는다.
    L.insert(fir_min_ind, fir_min)

    # 삭제와 재삽입으로 인덱스가 바뀌었다면 min2를 수정한다.
    if fir_min_ind <= sec_min_ind:
        sec_min_ind += 1

    return fir_min_ind, sec_min_ind
