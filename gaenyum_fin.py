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
# 파일을 받고 자신이 코딩하는 파일 안에 압축해제 하세요

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

# 정리
'''
접근 방법
• 최상단 계층의 패키지, 모듈은 dot (.) 없이 접근 가능
• 패키지 내부의 모듈은 패키지명.모듈명으로 접근 가능

from 없이 import만 사용한 케이스
• import 뒤에는 모듈명이 있어야함 (패키지명이 올 경우, __init__.py를 실행하고 모듈로 취급됨)
• 올바른 예시
    • (최상단 계층의 모듈) import 모듈명
    • (패키지 내부의 모듈) import 패키지명.모듈명
    • (여러 계층의 패키지 내부의 모듈) import 패키지명.패키지명.모듈명
    
from과 함께 import를 사용한 케이스
• import 뒤에는 모듈명 혹은 모듈 내 선언된 식별자가 dot (.) 없이 단독으로 와야함
• import 뒤에 등장하는 모듈명 혹은 식별자의 접근 경로는 from 뒤에 모두 표시되어야 함
• 올바른 예시
    • (최상단 계층의 모듈) from 모듈명 import 식별자
    • (패키지 내부의 모듈) from 패키지명 import 모듈명
    • (패키지 내부의 모듈) from 패키지명.모듈명 import 식별자
    • (여러 계층의 패키지 내부의 모듈) from 패키지명.패키지명.모듈명 import 식별자
'''
# https://wikidocs.net/1418 참고하면 도움이 될 것이다.