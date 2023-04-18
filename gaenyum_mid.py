# prompt string
x = input("Prompt")
print(x)

# sep, end
print(1, 2, sep='*', end='//')

# variable swap
x = 1
y = 2
x, y = y, x
print(x, y)

# //
print(13 // 4)

# formatting
print("%5d %07d %-10s %10.6f %10s" % (123, 456, "Python", 123.456789, "Python"))
print("{0:5d} {1:7d} {2:10s} {3:7.3f} {4:^10s}".format(123, 456, "Python", 123.456789, "Python"))
print("{:5d} {:07d} {:10s} {:7.3f} {:>10s}".format(123, 456, "Python", 123.456789, "Python"))

# complex numbers
c = 5j
print(c, type(c), c**2)

# int n round
print(int(2.7), int(-2.7), round(2.7), round(-2.7), int(0.5), round(0.5), round(0.15, 1))

# '"
print("'apostrophie'")
print('"ireum kkameokeum"')

# escape code
print('a\nb\tc\td\\e\'f\"')

# string math
print('abc' + 'def')
print('abc' * 4)

# string functions
tmp = 'abcdefg a '
print(tmp.count('a'))
print(tmp.find('c'))
print(tmp.find('z'))  # -1
print(tmp.index('b'))
# print(tmp.index('x'))  # error
print(' ,'.join(tmp))
print(tmp.upper())
print(tmp.rstrip())
print(tmp.strip())
print(tmp.replace('a', 'z'))
print(tmp.split('d'))

# functions for iterables
# len, min, max, sum, sorted (built-in function)

# modifying via slicing
tmp = list(range(10))
tmp[2:3] = [10] * 4
print(tmp)
# tmp[2:4] = 10  # error

# list functions
tmp = [i for i in range(5)]
tmp.insert(2, 3)
print(tmp)
tmp.extend([5, 6])
print(tmp)
print(tmp.pop())
tmp.pop(6)  # index 기준
print(tmp)
tmp.reverse()
print(tmp)

# immutable은 일반적으로 연산시 다른 대상을 참조하게 됨
# mutable은 반대
# 예외
a = [1, 2, 3, 4]
b = a
a = a[:] + [-1]
print(a, b, id(a), id(b))
# immutable도 프로그램 실행 중 이미 똑같은 결과가 저장된 곳이 있으면 그곳을 참조
# immutable 안에 mutable이 있으면 직접 수정
# 여기 많이 강조하시는거 같은데 왠지는 몰겠네

# bool
print(list(map(bool, [0, 0.0, "", '', [], {}, (), None])))
# 외에는 전부 True

# string compare
print('link' > 'language')

# python식 삼항 연산자
b = input()
print('True' if b == 'T' else 'False')

# iter & next
L = [1, 3, 5, 7, 9]
n = len(L)
it = iter(L)
for i in range(n):
    d = next(it)
    print(f'L[{i:2d}] = {d:2d}')

# how to make a tuple +
fruits = 'apple', 'mango', 'pear'
print(fruits)

# zip
A = ['Kim', 'Lee', 'Park']
B = [20, 30, 40]
C = ['Male', 'Female', 'Female']
Persons = list(zip(A, B, C))
print(Persons)

# aware
print((38,))
print((38))

# set
# for loop에 사용은 가능하나, 순서가 일정하지 않음
# 인덱싱, 슬라이싱 등을 사용할 수 없음
# immutable만 원소로 가짐

# id & hash
a = ('kim', 'lee', 'park')
b = ('kim', 'lee', 'park')
# 둘을 각각 interpretor에 입력하면 id가 달라짐
print(id(a), id(b))
print(hash(a), hash(b))

# set functions
# add(item) 메서드를 통해 새로운 아이템을 추가할 수 있음
# remove(item) 메서드 사용, 아이템이 존재하지 않을 시 에러 발생
# discard(item) 메서드 사용, 아이템 존재하지 않아도 에러 발생하지 않음
# update(items) 메서드를 통해 새로운 아이템을 추가할 수 있음
# clear(): 모두 삭제

# set calculations
a = {1, 2, 3, 4, 5, 6}
b = {7, 1, 3, 5}
print(a.issubset(b))
print(b.issubset(a))
print(a.issuperset(b))
print(b.issuperset(a))
# ==, !=, >=, <=, >, < 연산자 활용
# >, <, >=, <= : subset, superset 체크
print(a & b)
print(a | b)
print(a - b)
print(a ^ b)
for i in b:
    print(i)

# dict func
print(dict(k1='value1', key2='value2', keyN='valueN'))
print(dict([('one', 1), ('two', 2), ('three', 3)]))
# all into str
# hashable objects만이 key로 사용 가능
# 딕셔너리 객체 생성 시, 유니크한 key만 남게됨
# dict.keys(): 앞, dict.values(): 뒤, dict.items(): 둘 다
d = {
    1: 2,
    2: 4,
    3: 6
}
# print(d[4])  # 에러
print(d.get(4))
print(d.get(4, 'not found'))
print(d.pop(3))
print(d)

# 전역변수와 함수
x = 1


def f():
    # print(x) # 전역변수를 바로 쓸 수 없음
    x = 2  # 동일한 이름의 다른 지역변수 생성
    print(x)


f()
print(x)


# call by object reference(immutable)
def func(para1):
    print('address of para1:', id(para1))
    print(para1)


arg1 = 100
print('address of arg1:', id(arg1))
func(arg1)  # 그러니까 함수 내에서 실행하는 parameter는 처음에는 argument의 값을 참조하지만 추가 연산시 다른 값을 참조(immutable)


# call by object reference(mutable)
def func(x):
    x += [6, 7, 8]  # x = x[:]로 쓰면 다른 객체가 할당
    print(x, id(x))


c = [3, 4, 5]  # c[:]로 주면 다른 객체가 할당
print(c, id(c))
func(c)
print(c, id(c))


# mutable in mutable
def func(x):
    x[2][0] = 100
    x += [6, 7, 8]
    print(x, id(x))


c = [3, 4, [-5, -10]]
print(c, id(c))
func(c[:])  # 이걸 복사해 갔는데 내부의 list는 동일한 주소를 이어받아서 값이 바뀌게 됨
print(c, id(c))


# _ and __
# private att/method
class Bank:
    def __init__(self):
        self.__test_var1 = 4
        self._test_var2 = 3
        print('__init__ called')

    # __는 외부에서 사용 불가능
    def __test_func1(self):
        print('test function 1')

    def _test_func2(self):
        print('test function 2')


bank_exp = Bank()
print(dir(bank_exp))
# _(Classname)__(funcname)이 되기 때문
print([attr for attr in dir(bank_exp) if 'test' in attr])


# 상속
class Shape(object):
    def __init__(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color


class Rectangle(Shape):
    def __init__(self, color, width, length):
        super().__init__(color)  # 부모 클래스의 __init__ 받아오기
        self._width = width
        self._length = length

    def get_area(self):
        return self._width * self._length

    def set_color(self, color='red'):  # 메서드 오버라이딩
        self._color = color


rct = Rectangle('red', 10, 8)
print(rct.get_color())
print(rct.get_area())


# 동적 바인딩
class Student(object):
    def __str__(self):
        return 'Student'

    def print_itself(self):
        print(self.__str__())


class GraduateStudent(Student):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'Graduate Student'


# 두줄씩 위치 바꾸면 출력 순서가 바뀜
super_obj = Student()
super_obj.print_itself()

sub_obj = GraduateStudent()
sub_obj.print_itself()

# 연산자 오버로딩
# + * - / % -> add, mul, sub, truediv, mod
# < <= == != > >= -> lt le eq ne gt ge
# [index] -> getitem
# in -> contains
# len -> len
# str -> str
# ex) __getitem__ 로 오버로딩

# map function +
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]
print('x^y', list(map(pow, x, y)))
print(pow(2, 10))

# zip(*)
x = [1, 2, 3, 4]
y = [4, 5, 6]
z = [7, 8, 9, 10, 11]
zip_xyz = list(zip(x, y, z))
print(zip_xyz)
a, b, c = zip(*zip_xyz)
print(*zip_xyz)
print(a, b, c)

# reverse sort
x = [4, 2, 7, 3, 8, 10]
print(sorted(x, reverse=True))

# isinstance
print(isinstance([1, 2, 3], list))


# *args, **kwargs
# *args: positional arguments
# **kwargs: keyword arguments
def test_args_and_kwargs(var1, var2, *args, **kwargs):
    print(var1, var2, args, kwargs, sep='\n')


test_args_and_kwargs('hello', 10, [1, 2, 3], a='bbb', b=123, c=[1, 4, 6])
args = (1, 2, 3, 4, 5)
kwargs = {'a': 10, 'b': 20}
test_args_and_kwargs(*args, **kwargs)


# nested function
def my_func(text):
    # text 바로 사용 가능
    def dot_split():
        return text.split('. ')

    def comma_split(input_text):
        return input_text.split(', ')

    result1 = dot_split()
    result2 = comma_split(text)

    print(result1)
    print(result2)


my_func('apple, banana. 1, 2, 3. 4')


# closure 예시
# 함수를 둘러싼 환경(변수, 위치 등)을 유지하고 있다가 함수를 호출할 때 다시 꺼내서 사용하는 것을 closure라고 함
def printer(tag):
    def print_with_tag(message):
        print(f'[{tag}]', message)

    return print_with_tag

print_warning = printer('warning')
print_warning('virus!!')