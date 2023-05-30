# 파일 입출력/실습문제 1(count_each_letter)
import os.path


def read_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            return [line.rstrip() for line in f.readlines()]


def count_letter(line, str_to_cnt):
    return line.count(str_to_cnt)


def get_statistics(freq_list):
    return sum(freq_list), sum(freq_list) / len(freq_list), max(freq_list), min(freq_list)


def write_result(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)


def main(read_path, write_path, str_to_cnt):
    line_list = read_file(read_path)
    freq_list = [count_letter(line, str_to_cnt) for line in line_list]
    freq_dict = dict(zip(['sum', 'avg', 'max', 'min'], get_statistics(freq_list)))
    print_str = ''
    for k, v in freq_dict.items():
        print_str = print_str + f'{k}: {v}\n'
    print(print_str)
    print_str = f'statics of {str_to_cnt}\n' + print_str
    write_result(write_path, print_str)


letter_to_check = input("which letter? (a-z): ")

file_path_to_read = 'example.txt'
file_path_to_write = 'statistics.txt'

main(file_path_to_read, file_path_to_write, letter_to_check)
print("file is saved at: %s" % file_path_to_write)


# 입출력 및 예외처리/실습 1(개념 파일에 있음)
class InvalidLength(Exception):
    def __init__(self, length):
        super().__init__()
        self.length = length


class Rectangle(object):
    def __init__(self, a, b):
        if a <= 0:
            raise InvalidLength(a)
        elif b <= 0:
            raise InvalidLength(b)
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


try:
    r1 = Rectangle(4, 5)
    print(f'area(r1) = {r1.get_area()}')
    r2 = Rectangle(-1, -3)
    print(f'area(r2) = {r2.get_area()}')
except InvalidLength as e:
    print(f'length {e.length} is invalid')


# 입출력 및 예외처리/실습 2
class ZeroDivideZeroError(ZeroDivisionError):
    def __init__(self):
        super().__init__()


def int_division(n1, n2):
    if not isinstance(n1, int) or not isinstance(n2, int):
        raise TypeError
    elif n1 == 0 and n2 == 0:
        raise ZeroDivideZeroError
    elif n2 == 0:
        raise ZeroDivisionError

    return n1 // n2


try:
    print(int_division(8, 3))
    # print(int_division('a', 1))  # TypeError
    # print(int_division(0, 0))  # ZeroDivideZeroError
    # print(int_division(5, 0))  # ZeroDivisionError
    # print(int_division(1, 2, 3))  # TypeError
except TypeError:
    print('TypeError')
except ZeroDivideZeroError:
    print('cannot divide 0 by 0')
except ZeroDivisionError:
    print('cannot divide by 0')
except:
    print('exception occured')
else:
    print('no exceptions')


# 알고리즘 part1/실습/원하는 정수 찾기
n = int(input())
a = sorted(list(map(int, input().split())))
m = input()
f = list(map(int, input().split()))

# binary search는 안보고 칠 수 있도록 만드는 것이 좋을 것
def binary_search(a, key):
    left = 0
    right = len(a) - 1
    middle = (left + right) // 2
    flag = True

    while a[middle] != key:
        if key < a[middle]:
            right = middle - 1
        elif a[middle] < key:
            left = middle + 1
        if left > right:
            flag = False
            break

    return middle if flag else -1

for i in f:
    print(f'{1 if binary_search(a, i) != -1 else 0}')

# 알고리즘 part 2/실습 1
'''
검증되지 않은 코드
inp_list = input().split(', ')
l_max = max(map(len, inp_list))
to_sort = list(zip(inp_list, map(lambda x: x + x[0] * (l_max - len(x)), inp_list)))
to_sort.sort(key=lambda x: x[1])
print(int(''.join([to_sort[-1 - i][0] for i in range(len(inp_list))])))
'''
# 교수님 풀이
def to_swap(n1, n2):
    return str(n1) + str(n2) < str(n2) + str(n1)

def largest_number(nums):
    i = 1
    while i < len(nums):
        j = i
        while j > 0 and to_swap(nums[j - 1], nums[j]):
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
        i += 1
    return int(''.join(map(str, nums)))

print(largest_number([10, 2]))
print(largest_number([3, 30, 34, 5, 9]))

# 알고리즘 part 2/실습 2
inp_list = eval(input())
inp_list.sort(key=lambda x: x[0])
flag = True
while flag:
    flag = False
    for i in range(len(inp_list) - 1):
        if inp_list[i][1] >= inp_list[i + 1][0]:
            flag = True
            if inp_list[i][1] >= inp_list[i + 1][1]:
                inp_list.pop(i + 1)
            else:
                inp_list[i] = [inp_list[i][0], inp_list[i + 1][1]]
            break
print(inp_list)

# 알고리즘 part 3/실습 1
# 교수님 풀이와 같음
N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            result += 1
print(result)

# 알고리즘 part 3/실습 2
# 교수님 풀이와 같음
from collections import deque

n, m = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    numbers = list(map(int, input()))
    for j in range(m):
        graph[i][j] = numbers[j]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        xx, yy = queue.popleft()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[xx][yy] + 1
                    queue.append((nx, ny))

bfs(0, 0)
print(graph[n - 1][m - 1])
