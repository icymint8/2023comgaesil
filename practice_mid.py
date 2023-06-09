# 파이썬 기본 2/실습1
import time

year = [2011 + i for i in range(8)]
population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]
print(year[-3:])
print(population[-3:])
print([i for i in year if i % 2])
print([population[year.index(i)] for i in year if i % 2])

# 파이썬 기본 2/실습2
at = ['이가연', '이승희', '이지은']
print(f'현재 학생은 {at}')
at.append(input('새로 들어온 학생의 이름은 무엇입니까? '))
print("번호 재정렬...")
at.sort()
for i, j in enumerate(at):
    print(i+1, j)

# 제어구조/실습1
goal_dict = {
    '국어': 90,
    '영어': 81,
    '수학': 86,
    '과학': 80
}
name = input('이름을 입력하세요: ')
score_sum = 0
passed = 'PASS'
for i in goal_dict:
    tmp = int(input(f'{i} 성적을 입력하세요: '))
    if tmp < goal_dict[i]:
        passed = 'FAIL'
    score_sum += tmp
print(f'{name} 님의 성적은')
print(f'총합 {score_sum}점, 평균 {score_sum / 4}점입니다.')
print(passed)

# 제어구조/실습2
import random
answer = random.randint(1, 100)
while True:
    tmp = int(input('Enter a guess: '))
    if tmp != answer:
        print(f'{tmp} is too {"low" if tmp < answer else "high"}; try again')
    else: break
print('You got it right!')

# 제어구조/실습3
bev_list = [
    ['사이다', 700],
    ['콜라', 800],
    ['물', 1200]
]
money = int(input('얼마를 입력하시겠습니까: '))
choice = int(input('선택) 1-사이다 2-콜라 3-물: ')) - 1
if money >= bev_list[choice][1]:
    print(f'{bev_list[choice][0]}가 나왔습니다. 덜컹')
    print(f'잔돈 {money - bev_list[choice][1]}원 반환합니다.')
else:
    print('음료수를 사먹을 수 없습니다.')

# 데이터타입/튜플의 활용/문제1
members = (('choi', 93), ('han', 50), ('jung', 92), ('kang', 68), ('kim', 80), ('lee', 90), ('moon', 65), ('na', 100), ('park', 75), ('song', 75))
print(input() in [mem[0] for mem in members])

# 데이터타입/튜플의 활용/문제2
members = (('choi', 93), ('han', 50), ('jung', 92), ('kang', 68), ('kim', 80), ('lee', 90), ('moon', 65), ('na', 100), ('park', 75), ('song', 75))
print(max(members, key=lambda x: x[1]))

# 데이터타입/튜플의 활용/문제3
members = (('choi', 93), ('han', 50), ('jung', 92), ('kang', 68), ('kim', 80), ('lee', 90), ('moon', 65), ('na', 100), ('park', 75), ('song', 75))
try:
    print(members[[i[0] for i in members].index(input())])
except:
    print('not included')

# 데이터타입/set의 활용/문제1
a, b = map(int, input().split())
s_a = {i for i in range(1, a + 1) if a % i == 0}
s_b = {i for i in range(1, b + 1) if b % i == 0}
print(s_a, s_b, s_a & s_b, max(s_a & s_b), sep='\n')

# 데이터타입/set의 활용/문제2
s1 = {10, 20, 30, 40, 30, 20, 10}
s2 = {i for i in range(100 + 1) if i % 2 == 0}
print(sorted(list(s1 | s2)), sorted(list(s1 & s2)), sep=' ')

# 데이터타입/dict의 활용/문제1
books = {'여행의 이유':13500, '소년이로':13000, '희랍인 조르바':9000, '세 여자':14000, '아픔이 길이 되려면':18000}
while True:
    tmp = input()
    if tmp == '0': break
    else:
        print(books.get(tmp, 'not available'))

# 데이터타입/dict의 활용/문제2
code = {'A': '.-', 'B': '-....', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}
input_string = input()
for c in input_string:
    print(code.get(c, 'None'), end=' ')

# 데이터타입/dict의 활용/문제3
lines = open('example.txt', 'r').readlines()
lines = [line.strip() for line in lines]
word_dict = {}
for line in lines:
    for word in line.split():
        tmp = word.strip(".,").lower()
        if tmp not in word_dict: word_dict[tmp] = 1
        else: word_dict[tmp] += 1
print([(i, word_dict[i]) for i in sorted(word_dict) if word_dict[i] >= 10])


# 함수/실습 문제1
def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b


def calc(a, b, c='+'):
    if c == '+': return addition(a, b)
    elif c == '-': return subtraction(a, b)
    elif c == '*': return multiplication(a, b)
    elif c == '/': return division(a, b)
    else: return None


def operate_calculator():
    a = int(input())
    b = int(input())
    c = input()
    result = calc(a, b, c)
    if result or result == 0:
        print(f'{a} {c} {b} = {result}')
    else:
        print('wrong operator type')


operate_calculator()

# 함수/실습 문제2
import random
def draw_a_card(cards):
    return cards.pop(random.randrange(1, 12))


def get_score(card_list, owner):
    print(card_list)
    print(f'{owner}: {sum(card_list)}')
    return sum(card_list)


def print_result(my_score, dealer_score):
    print('Win' if my_score > dealer_score else 'Lose')


cards = list(range(1, 12)) * 4
my_cards, dealer_cards = [], []
for i in range(2):
    my_cards.append(draw_a_card(cards))
    dealer_cards.append(draw_a_card(cards))
my_sum = get_score(my_cards, 'me')
dealer_sum = get_score(dealer_cards, 'dealer')
print_result(my_sum, dealer_sum)


# 함수/실습 문제3
import random
def draw_a_card(cards):
    return cards.pop(random.randrange(1, 12))


def get_score(card_list, owner):
    print(card_list)
    print(f'{owner}: {sum(card_list)}')
    return sum(card_list)


def print_result(my_score, dealer_score):
    who = 'Win' if my_score > dealer_score else 'Lose'
    print(who)
    return who


def play_a_round():
    cards = list(range(1, 12)) * 4
    my_cards, dealer_cards = [], []
    for i in range(2):
        my_cards.append(draw_a_card(cards))
        dealer_cards.append(draw_a_card(cards))
    my_sum = get_score(my_cards, 'me')
    dealer_sum = get_score(dealer_cards, 'dealer')
    return print_result(my_sum, dealer_sum)


def play_with_betting(my_chips, dealer_chips):
    if my_chips and dealer_chips:
        max_bet = min([my_chips, dealer_chips])
        bet = int(input(f'bet = ? (<={max_bet})'))
        while bet > max_bet:
            bet = int(input(f'bet = (<={max_bet})'))
        if play_a_round() == 'Win':
            return play_with_betting(my_chips + bet, dealer_chips - bet)
        else:
            return play_with_betting(my_chips - bet, dealer_chips + bet)
    else:
        return my_chips, dealer_chips


my_init, dealer_init = 100, 100
my_fin, dealer_fin = play_with_betting(my_init, dealer_init)
if my_fin:
    print('I win')
else:
    print('dealer wins')


# 클래스/실습문제 1
class SimpleClass:
    def __init__(self):
        self.attr1 = 3.14
        self.attr2 = 2.72

    def met1(self):
        print(self.attr1)

    def met2(self):
        print(self.attr2)


new_class = SimpleClass()
new_class.met1()
new_class.met2()


# 클래스/실습문제 2
class SimpleCalc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def subtraction(self):
        print(self.a - self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)


a, b = map(int, input().split())
new_calc = SimpleCalc(a, b)
new_calc.addition()
new_calc.subtraction()
new_calc.multiplication()
new_calc.division()


# 클래스/실습문제 3
import random
class Player:
    def __init__(self):
        self.num_wins = 0
        self.hand = ''

    def play(self):
        self.hand = ['rock', 'paper', 'scissors'][random.randrange(0, 3)]

    def feedback(self, opponent):
        tmp = ['rock', 'paper', 'scissors']
        if self.hand == opponent.hand:
            return 'draw'
        else:
            if tmp.index(opponent.hand) == (tmp.index(self.hand) + 1) % 3:
                return 'lose'
            else:
                return 'win'


n = int(input())
p1 = Player()
p2 = Player()
for i in range(n):
    p1.play()
    p2.play()
    print(p1.hand, p2.hand, end=' ')
    tmp = p1.feedback(p2)
    if tmp == 'win':
        print('p1 won')
    elif tmp == 'draw':
        print('draw')
    else:
        print('p2 won')


# 상속과 다형성/실습 1
class Person(object):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f'Person {self.age}'

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return self.age != other.age


hj = Person(52)
sy = Person(48)
rh = Person(19)
mj = Person(13)
l = [hj, sy, rh, mj]
l.sort()
for p in l:
    print(p)


# 상속과 다형성/실습 2
class ReverseIndexingList(list):
    def __init__(self, list_obj):
        super().__init__(list_obj)

    def __getitem__(self, item):
        return super().__getitem__(-item - 1)

ril = ReverseIndexingList([1, 2, 3, 4, 5])
print(ril[4])


# 함수 2/재귀함수/실습 1
def jisu(a, n):
    if n == 0: return 1
    else:
        return a * jisu(a, n - 1)

print(jisu(2, 10))


# 함수 2/재귀함수/실습 2
def symmetry_check(s):
    l = len(s)
    if l == 1:
        return True
    elif l == 2:
        return s[0] == s[1]

    if symmetry_check(s[1:l-1]):
        return True
    else:
        return False

print(symmetry_check('aabbaa'))
print(symmetry_check([1, 2, 3, 2, 1]))
print(symmetry_check((2, 4, 3, 2)))


# 함수 2/재귀함수(tail recursion)/실습
import time
def fib(ind):
    if ind == 0:
        return 0
    elif ind == 1:
        return 1
    else:
        return fib(ind - 1) + fib(ind - 2)

def fib_tail(ind):
    return fib_helper(ind, 0, 1)

def fib_helper(ind, bef, aft):
    if ind == 0:
        return bef
    else:
        return fib_helper(ind - 1, aft, bef + aft)


n = 60
t0 = time.time()
print(fib(n))
t1 = time.time()
print(fib_tail(n))
t2 = time.time()
print(t1 - t0)
print(t2 - t1)


# 함수 2/함수를 parameter로 활용하기/실습
def return_last(text):
    return text.split(' ')[-1]


def return_first(text):
    return text.split(' ')[0]


def new_dict(func, p_dict):
    ndict = {}
    for k, v in p_dict.items():
        ndict[func(k)] = v
    return ndict


data = {
    'John Legend': 'singer',
    'Taylor Swift': 'singer',
    'Ashton Kutcher': 'actor',
    'Ryan Gosling': 'actor'
}
print(new_dict(return_first, data))
print(new_dict(return_last, data))


# 함수 2/customizing function with closure/실습
def make_multiplier(arg1):
    def multiply(arg2):
        return arg1 * arg2

    return multiply


mul_4 = make_multiplier(4)
print(mul_4(5))
