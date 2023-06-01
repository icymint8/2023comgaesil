# sys module
import sys

print(sys.builtin_module_names)
print(dir(sys))
print(sys.version)
print(sys.prefix)
'''
('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_codecs_cn', '_codecs_hk', '_codecs_iso2022', '_codecs_jp', '_codecs_kr', '_codecs_tw', '_collections', '_contextvars', '_csv', '_datetime', '_functools', '_heapq', '_imp', '_io', '_json', '_locale', '_lsprof', '_md5', '_multibytecodec', '_opcode', '_operator', '_peg_parser', '_pickle', '_random', '_sha1', '_sha256', '_sha3', '_sha512', '_signal', '_sre', '_stat', '_statistics', '_string', '_struct', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', '_winapi', '_xxsubinterpreters', 'array', 'atexit', 'audioop', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'math', 'mmap', 'msvcrt', 'nt', 'parser', 'sys', 'time', 'winreg', 'xxsubtype', 'zlib')
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_git', '_home', '_xoptions', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'getallocatedblocks', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']
3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
C:\Python\Python39
'''

# os module
import os

print(os.getcwd())
print(os.listdir())
"""
C:\컴개실(004) 김량현\2023comgaesil
['.git', '.idea', 'boj.py', 'debug.py', 'example.txt', 'gaenyum_fin.py', 'gaenyum_mid.py', 'practice_fin.py', 'practice_mid.py', 'README.md']
"""

# random module
import random

for x in range(5):
    numbers = list(range(1, 50))
    gen_numbers = random.sample(numbers, 6)
    print(f'{x + 1}: {gen_numbers}')
'''
1: [36, 43, 15, 38, 12, 34]
2: [36, 46, 45, 20, 5, 27]
3: [3, 8, 4, 12, 49, 1]
4: [8, 41, 17, 38, 12, 47]
5: [30, 13, 17, 46, 20, 45]
'''

# datetime module
from datetime import *

today = date.today()
print(today, today + timedelta(days=300))
'''
2023-05-02 2024-02-26
'''

# 식별자 중복
from random import *
print(randint(1, 5))
def randint():
    pass

class randint():
    pass

randint = 10
print(randint)
'''
3
10
'''

# 잡것
import this
'''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

# __name__
print(__name__)
'''
__main__
'''
# import한 모듈 내에서 위 구문이 실행될 경우 그 함수의 파일명으로 나오게 됨

# etl에서 my_program 파일을 받았다고 가정 후 진행
# 파일을 받고 자신이 코딩하는 디렉토리 안에 압축해제 하세요

# __init__.py
# 패키지 import시 자동으로 실행
import simulation
'''
simulation package is initialized!
imported some modules in simulation package~
'''
# simulation 패키지 안 __init__ 확인해 보기

# __init__을 통해 패키지 안의 프로그램들을 바로 사용 가능
import simulation

if __name__ == '__main__':
    simulation.simulator.preprocess()
    simulation.result_handler.result_parsing('data')
# https://wikidocs.net/1418 참고하면 도움이 될 것이다.

# 파일 입출력(w)
f = open('writing_test.txt', 'w')
# or f = open('C:\\컴개실(004) 김량현\\2023comgaesil\\new_file.txt', w)
# or f = open(r'C:\컴개실(004) 김량현\2023comgaesil\new_file.txt', w)
# r string은 문자를 문자 그대로(escape code가 아닌) 인식하게 만들어준다.
f.write('First line\n')
f.write('Second line\n')
f.write('Third line\n')
f.close()
# writing_test.txt에서
'''
First line
Second line
Third line

'''

# 파일 입출력(a)
f = open('writing_test.txt', 'a')
for i in range(10):
    f.write(f'newly added line ({i})\n')
f.close()
# writing_test.txt에서
'''
newly added line (0)
...
newly added line (9)
'''

# 파일 입출력(r)
f = open(r'C:\컴개실(004) 김량현\2023comgaesil\writing_test.txt', 'r')
for i in range(3):
    line = f.readline()
    print(line.rstrip())  # \n 지우기
f.close()
'''
First line
Second line
Third line
'''

# 파일 읽는 방법들
f = open('writing_test.txt')
while True:
    line = f.readline()
    if not line:  # 끝에 도달하면 line == ''가 됨
        break
    print(line.rstrip())

f = open('writing_test.txt')
for line in f:
    print(line.rstrip())

f = open('writing_test.txt')
for line in f.readlines():
    print(line.rstrip())

f = open('writing_test.txt')
print(f.read())
f.close()
'''
First line
...
newly added line(9)
x3
'''

# 파일 존재여부 확인
import os.path
path = 'writing_test.txt'
print(os.path.isfile(path))
'''
True
'''

# 에러의 종류
print(100)
# print('d) <- syntax error(구문오류). 프로그램 실행 자체가 불가
# print(dsf) < exception(예외). 윗줄까지 실행된 이후 뻗음.
'''
그냥 에러
(1, 2줄)

100
에러
(1, 3줄)
'''

# 예외 처리 예시 - if문
n = input('정수 입력')
if n.isdigit():
    n = int(n)
    print(n, type(n))
else:
    print('정수 아님')
'''
입력: 10
출력: 10 <class 'int'>

입력: ㅎ
출력: 정수 아님
'''

# 예외 처리 예시 - try-except 구문
try:
    n = int(input())
    print(10 / n)
except ZeroDivisionError:
    print('cannot divide by 0')
except:
    print('something wrong')
else:
    print('no exceptions')
finally:
    print('program finished')
'''
입력: 4
출력:
2.5
no exceptions
program finished

입력: 0
출력: cannot divide by 0
program finished

입력: ㅇㅇ
출력: write integer
program finished
'''

# exception 만들기
num = int(input('integer smaller than 5:'))
if num >= 5:
    raise Exception('not smaller than 5')
print(5 / num)
'''
in: 4
out: 1.25

in: 6
out: error
Traceback (most recent call last):
  File "C:\Program Files\JetBrains\PyCharm Community Edition 2022.3.2\plugins\python-ce\helpers\pydev\pydevconsole.py", line 364, in runcode
    coro = func()
  File "<input>", line 4, in <module>
Exception: not smaller than 5
'''

# raising에 대한 자세한 설명은 자료 참고
# tracking raising
def f1():  # line 1
    print('f1 called')
    try:
        f2()
    except Exception:
        print('exception handled at f1')

def f2():  # line 8
    print('f2 called')
    f3()

def f3():  # line 12
    print('f3 called')
    try:
        raise Exception('throw an Exception object at f3')
    except Exception:
        print('exception handled at f3')
    finally:
        raise Exception('throw new exception at f3')

f1()  # line 21
'''
f1 called
f2 called
f3 called
exception handled at f3
exception handled at f1
'''

def rraaiissee():
    try:
        raise Exception('1')
    except Exception as e:
        print(f'{e} exception made')
    finally:
        raise Exception('2')

try:
    rraaiissee()
except Exception as e:
    print(f'{e} exception made in rraaiissee')
'''
1 exception made
2 exception made in rraaiissee
'''

def rraaiissee():
    try:
        raise Exception('1')
    except Exception as e:
        print(f'{e} exception made')
    finally:
        print('done')

try:
    rraaiissee()
except Exception as e:
    print(f'{e} exception made in rraaiissee')
'''
1 exception made
done
'''
# 이건 진짜 헷갈린다
# 나도 잘 모름 ㅅㄱ

# 바람직한 예외처리 방법
def division(a, b):  # line 1
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('not number')

    if b == 0:
        raise ZeroDivisionError('cannot divide by 0')  # 에러 던지고

    return a / b

def with_user_input(num_trial):  # line 10
    if not isinstance(num_trial, int):
        raise TypeError('not int')

    for i in range(num_trial):
        try:
            n1 = eval(input('n1:'))
            n2 = eval(input('n2:'))
            result = division(n1, n2)
            print(result)
            break
        except Exception as ex:  # 그 함수를 호출하는 곳에서 받기
            print(ex)
            print('try again')

try:
    with_user_input(3)
    with_user_input('1')
except Exception as ex:
    print(ex)
    print('wrong input')
'''
n1:>? 4  # 입력
n2:>? 0  # 얘도
cannot divide by 0
try again
n1:>? 'apple'
n2:>? 2
not number
try again
n1:>? 3
n2:>? 2
1.5
not int
wrong input
'''

# custom exception
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
'''
area(r1) = 20
length -1 is invalid
'''

# linear search
# 과거에 len 많이 썼다가 시간초과 난 경험이 있어서...
def seq_search1(a, key):
    for i in a:
        if i == key:
            return a.index(i)
    return -1

# 오리지날
def seq_search2(a, key):
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

# copy 안해도 되지 않을까?
def senti_seq_search1(a, key):
    a.append(key)
    i = 0
    while True:
        if a[i] == key:
            break
        i += 1
    a.pop(-1)

    return -1 if i == len(a) else i

# 오리지날
import copy
def senti_seq_search2(seq, key):
    a = copy.deepcopy(seq)
    a.append(key)
    i = 0
    while True:
        if a[i] == key:
            break
        i += 1

    return -1 if i == len(seq) else i

def binary_search(a, key):
    left = 0
    right = len(a) - 1
    while True:
        middle = (left + right) // 2
        if a[middle] == key:
            return middle
        elif key < a[middle]:
            right = middle - 1
        elif a[middle] < key:
            left = middle + 1
        if left > right:
            break

    return -1

import time
def count_time(search, L, v):
    t1 = time.perf_counter()
    search(L, v)
    t2 = time.perf_counter()
    return (t2 - t1) * 1000

def print_time(v, L):
    t1 = time.perf_counter()
    L.index(v)
    t2 = time.perf_counter()
    index_time = (t2 - t1) * 1000
    seq1_time = count_time(seq_search1, L, v)
    seq2_time = count_time(seq_search2, L, v)
    senti1_time = count_time(senti_seq_search1, L, v)
    senti2_time = count_time(senti_seq_search2, L, v)
    bin_time = count_time(binary_search, L, v)
    print(
        f'{v:<10d} {bin_time:5.4f} {index_time:5.4f} {seq1_time:5.4f} {seq2_time:5.4f} {senti1_time:5.4f} {senti2_time:5.4f}'
    )

L = list(range(10000000))
print_time(10, L)
print_time(5000000, L)
print_time(9999999, L)
# senti2 왤케 오래걸리지? deepcopy 때문인가
'''
        10 0.0180 0.0115 0.0065 0.0222 17.5222 2943.9079
   5000000 0.0119 43.9525 130.1141 165.9049 219.1126 3187.7449
   9999999 0.0185 87.3036 262.6453 328.5049 436.8288 3392.0284
'''

# 정렬 알고리즘들
# 선택 정렬
def selection_sort(a):
    l = len(a)
    for i in range(l - 1):
        ind_m = i
        for j in range(i + 1, l):
            if a[ind_m] > a[j]:
                ind_m = j
        a[i], a[ind_m] = a[ind_m], a[i]

# 삽입 정렬
def insertion_sort(a):
    l = len(a)
    for i in range(1, l):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

# 퀵 정렬
def qsort(a, left, right):
    pl = left
    pr = right
    x = a[(left + right) // 2]
    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    if left < pr: qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)

def quick_sort(a):
    qsort(a, 0, len(a) - 1)

# 병합 정렬
def merge_sort(a):
    def _merge_sort(a, left, right):
        if left < right:
            center = (left + right) // 2
            _merge_sort(a, left, center)
            _merge_sort(a, center + 1, right)

            p = j = 0
            i = k = left
            while i <= center:
                buff[p] = a[i]
                p += 1
                i += 1

            while i < right and j < p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1

            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1
    n = len(a)
    buff = [None] * n
    _merge_sort(a, 0, n - 1)
    del buff

# 시간 재는 함수
import time
def sort_time(sort, a):
    t1 = time.perf_counter()
    sort(a)
    t2 = time.perf_counter()
    return (t2 - t1) * 1000

import random
n = int(input('배열의 원소 수'))
a = random.sample(range(n), n)
print(f't = {sort_time(sorted, a):.6f} milliseconds')
print(a)
'''
# selection sort
input: 10000
t = 2041.051500 milliseconds

# insertion sort
input: 10000
t = 3162.341600 milliseconds

# quick sort
input: 10000
t = 12.714700 milliseconds

# merge sort
input: 10000
t = 21.838400 milliseconds

# built-in sort(sorted)
input: 10000
t = 0.999400 milliseconds
'''

# stack
class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print('stack is empty')

    def peek(self):
        try:
            return self.items[-1]
        except IndexError:
            print('stack is empty')

    def empty(self):
        return not bool(self.items)

    def size(self):
        return len(self.items)

    def __repr__(self):
        return repr(self.items)

stack = Stack()
stack.push(1)
print(stack.pop())
print(stack.pop())
print(stack.size())
for i in range(0, 10, 2):
    stack.push(i)
print(stack)
'''
1
stack is empty
None
0
[0, 2, 4, 6, 8]
'''

# queue
class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        try:
            return self.items.pop(0)
        except IndexError:
            print('queue is empty')

    def empty(self):
        return not bool(self.items)

    def size(self):
        return len(self.items)

    def peek(self):
        try:
            return self.items[0]
        except IndexError:
            print('queue is empty')

    def __repr__(self):
        return repr(self.items)

# 실습은 알아서
# collections.deque와 사용법이 동일(이름은 좀 다름)

# dfs
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9
dfs(graph, 1, visited)
'''
1 2 7 6 8 3 4 5 
'''

# bfs
from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9
bfs(graph, 1, visited)
'''
1 2 3 8 7 4 5 6 
'''

# numpy 기초
# 사실 파이썬 라이브러리 다룰 때는 인터넷 창 켜놓고 설명서 읽으면서 하는 것을 추천합니다
import numpy as np

a = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
print(a)
print(a.dtype)
a = a.astype('float64')
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
'''
[[1 2]
 [3 4]
 [5 6]]
int32
[[1. 2.]
 [3. 4.]
 [5. 6.]]
2
(3, 2)
6
'''

# ndarray 생성
import numpy as np
print(np.zeros((2, 3)))
print(np.ones_like(np.ones((4, 4))))
print(np.identity(3))
print(np.arange(0, 1, 0.1))
print(np.linspace(1.4, 20, 5))
'''
[[0. 0. 0.]
 [0. 0. 0.]]
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
[0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]
[ 1.4   6.05 10.7  15.35 20.  ]
'''

# ndarray 연산
import numpy as np
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(a * a)
print(1 + a)
print(a ** 2)
b = np.array([
    [0, 1],
    [1, 0]
])
print(np.dot(b, a))
print(b.dot(a))
print(b @ a)
c = a
a = a ** 2
print(c)
d = a
a += 1
print(d)
'''
[[ 1  4  9]
 [16 25 36]]
[[2 3 4]
 [5 6 7]]
[[ 1  4  9]
 [16 25 36]]
[[4 5 6]
 [1 2 3]]
[[4 5 6]
 [1 2 3]]
[[4 5 6]
 [1 2 3]]
[[1 2 3]
 [4 5 6]]
[[ 2  5 10]
 [17 26 37]]
'''

# indexing, slicing
import numpy as np
a = np.arange(5)
a[2:] = -1
print(a)
b = np.array([
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [3, 6, 9, 12]
])
print(b[0])
print(b[1:, 3:])
'''
[ 0  1 -1 -1 -1]
[1 3 5 7]
[[ 8]
 [12]]
'''


# copy
import numpy as np
a = np.array([
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [3, 6, 9, 12]
])
b = a
print(id(a))
print(id(b))
c = a[::2, 1]
c[0] = -100
print(a)
d = a[0]
d[1] = -200
print(a)
e = a.copy()
e[2, 2] = -300
print(a)
'''
2072674170320
2072674170320
[[   1 -100    5    7]
 [   2    4    6    8]
 [   3    6    9   12]]
[[   1 -200    5    7]
 [   2    4    6    8]
 [   3    6    9   12]]
[[   1 -200    5    7]
 [   2    4    6    8]
 [   3    6    9   12]]
'''

# boolean indexing
import numpy as np
c = np.arange(1, 7).reshape((2, 3))
print(c)
print(c > 2)
print(c[c > 2])
print(np.logical_or(c == 1, c > 3))
'''
[[1 2 3]
 [4 5 6]]
[[False False  True]
 [ True  True  True]]
[3 4 5 6]
[[ True False False]
 [ True  True  True]]
'''

# counting entries
import numpy as np
x = np.arange(1, 13).reshape((3, 4))
print(np.count_nonzero(x < 6))
print(np.sum(x < 6))
print(x[(x > 2) & (x < 6)]) # and
print(x[(x < 2) | (x > 6)]) # or
print(np.sum(x < 6, axis=0)) # column-wise
print(np.sum(x < 6, axis=1)) # row-wise
# 행 렬이라서 0이 행이고 1이 열일것 같은데 그렇지 않음.
print(np.all(x < 6, axis=1))
'''
5
5
[3 4 5]
[ 1  7  8  9 10 11 12]
[2 1 1 1]
[4 1 0]
[ True False False]
'''

# indexing with arrays
import numpy as np
a = np.arange(5) ** 2
i = np.array([2, 2, 0, 3])
print(a[i])
j = np.array([
    [1, 0],
    [0, 4]
])
print(a[j])
'''
[4 4 0 9]
[[ 1  0]
 [ 0 16]]
'''

# shape manipulation
import numpy as np
a = np.array((1, 2))
b = np.array((3, 4))
print(np.concatenate((a, b)))
a2 = a.reshape([1, 2])
b2 = b.reshape([1, 2])
print(np.concatenate((a2, b2), axis=0))
print(np.concatenate((a2, b2), axis=1))
c = np.arange(12).reshape((3, 4)).flatten()
print(c)
'''
[1 2 3 4]
[[1 2]
 [3 4]]
[[1 2 3 4]]
[ 0  1  2  3  4  5  6  7  8  9 10 11]
'''
