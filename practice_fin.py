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
inp_list = input().split(', ')
l_max = max(map(len, inp_list))
to_sort = list(zip(inp_list, map(lambda x: x + x[0] * (l_max - len(x)), inp_list)))
to_sort.sort(key=lambda x: x[1])
print(int(''.join([inp_list[-1 - i] for i in range(len(inp_list))])))
