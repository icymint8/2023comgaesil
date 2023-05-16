import time
import find_remove_find
import sort_then_find
import walk_through

def time_find_two_smallest(find_func, lst):
    """find_func(lst)를 실행하는 데 몇 초가 걸렸는지 반환한다.
    """

    t1 = time.perf_counter()
    find_func(lst)
    t2 = time.perf_counter()
    return (t2 - t1) * 1000.0

if __name__ == '__main__':
    # 해면 기압을 읽는다.
    sea_levels = []
    sea_levels_file = open('sea_levels.txt', 'r')
    for line in sea_levels_file:
        sea_levels.append(float(line))
    sea_levels_file.close()

    # 각 방법의 시간을 측정한다.
    find_remove_find_time = time_find_two_smallest(
        find_remove_find.find_two_smallest, sea_levels)

    sort_get_minimums_time = time_find_two_smallest(
        sort_then_find.find_two_smallest, sea_levels)

    walk_through_time = time_find_two_smallest(
        walk_through.find_two_smallest, sea_levels)

    print('"찾고 삭제하고 찾기"는 {:.2f}ms가 걸렸습니다.'.format(find_remove_find_time))
    print('"정렬하고 최소값 인덱스 얻기"는 {:.2f}ms가 걸렸습니다.'.format(
        sort_get_minimums_time))
    print('"리스트 전체 스캔하기"는 {:.2f}ms가 걸렸습니다.'.format(walk_through_time))