# 9 - Mavzu. Funksiyaga oid sodda masalalar


# 1 - masala
def PowerA3(A, B, C, D, E):
    result = pow(A, 3) + pow(B, 3) + pow(C, 3) + pow(D, 3) + pow(E, 3)
    return result


A = int(input('A butun son kiriting: '))
B = int(input('B butun son kiriting: '))
C = int(input('C butun son kiriting: '))
D = float(input('D haqiqiy son kiriting: '))
E = float(input('E butun son kiriting: '))

result = PowerA3(A, B, C, D, E)
print(result)


# 2 - masala
def PowerA234(A, B, C):
    result = pow(A, 2) + pow(B, 3) + pow(C, 4)
    return result


A = float(input('A haqiqiy son kiriting: '))
B = float(input('B haqiqiy son kiriting: '))
C = float(input('C haqiqiy son kiriting: '))

result = PowerA234(A, B, C)
print(result)



# 3 - masala
import math

def MEAN(A, B, C, D):
    arifmetik_orta = (A + B + C + D) / 4
    geometrik_orta = math.sqrt(A * B * C * D)
    return arifmetik_orta, geometrik_orta


A = float(input('A haqiqiy son kiriting: '))
B = float(input('A haqiqiy son kiriting: '))
C = float(input('A haqiqiy son kiriting: '))
D = float(input('A haqiqiy son kiriting: '))

arifmetik_orta, geometrik_orta = MEAN(A, B, C, D)

print("Orta Arifmetika:", arifmetik_orta)
print("Orta Geometriya:", geometrik_orta)


# 4 - masala
import math

def Triangle(teng_tomon):
    perimeter = 3 * teng_tomon

    # Calculate area
    area = (math.sqrt(3) / 4) * teng_tomon ** 2

    return perimeter, area


side_length = float(input('haqiqiy son kiriting: '))

perimeter, area = Triangle(side_length)

print("Perimeter:", perimeter)
print("Area:", area)


# 5 - masala
def RectPS(x1, y1, x2, y2):
    length = abs(x2 - x1)
    width = abs(y2 - y1)

    # Calculate perimeter
    perimeter = 2 * (length + width)

    # Calculate area
    area = length * width

    return perimeter, area


x1 = int(input('x1 butun son kiriting: '))
y1 = int(input('y1 butun son kiriting: '))
x2 = int(input('x2 butun son kiriting: '))
y2 = int(input('y2 butun son kiriting: '))

perimeter, area = RectPS(x1, y1, x2, y2)

print("Perimeter:", perimeter)
print("Area:", area)


# 6 - masala
def DigitCountSum(num):
    yegindi = 0
    count = 0

    while num != 0:
        digit = num % 10
        print('dig', digit)
        count += 1
        print('c', count)
        yegindi += digit
        print('ye', yegindi)
        num //= 10
        print('num', num)
    return yegindi, count

a = int(input())
b = int(input())
c = int(input())

count_a, yegindi_a = DigitCountSum(a)
count_b, yegindi_b = DigitCountSum(b)
count_c, yegindi_c = DigitCountSum(c)

print('a number yegindi', yegindi_a, 'a count', count_a)
print('b number yegindi', yegindi_b, 'b count', count_b)
print('c number yegindi', yegindi_c, 'c count', count_c)


# 7 - masala
def InvertDigit(num):
    teskari = 0
    while num > 0:
        digit = num % 10
        print('di', digit)
        teskari = (teskari * 10) + digit
        print('tes', teskari)
        num //= 10
        print('num', num)

    return teskari


a = int(input())
b = int(input())
c = int(input())

teskari_a = InvertDigit(a)
teskari_b = InvertDigit(b)
teskari_c = InvertDigit(c)

print('Number a', teskari_a)
print('Number b', teskari_b)
print('Number c', teskari_c)


# 8 - masala
def AddRightDigit(number, digit):
    new_number = (number * 10) + digit

    return new_number

K = int(input())
R = int(input())

new_number = AddRightDigit(K, R)

print('New add number on the rigth: ', new_number)


# 9 - masala
def AddLeftDigit(number, digit):
    digits = len(str(number))
    print('d', digits)
    new_number = (digit * (10 ** digits)) + number

    return new_number

K = int(input())
R = int(input())

new_number = AddLeftDigit(K, R)

print('New add number on the left: ', new_number)


# 10 - masala
def Swap(a, b):
    a[0], b[0] = b[0], a[0]

A = [int(input())]
B = [int(input())]
C = [int(input())]
D = [int(input())]
print('A:', A[0], 'B:', B[0], 'C:', C[0], 'D:', D[0])

Swap(A, B)
Swap(D, C)
print('A:', A[0], 'B:', B[0], 'C:', C[0], 'D:', D[0])


# 11 - masala
def Minmax(X, Y):
    if X > Y:
        X, Y = Y, X

    return X, Y

a = int(input())
b = int(input())
c = int(input())
d = int(input())

a, b = Minmax(a, b)
c, d = Minmax(c, d)

print('a', a, 'b', b)
print('c', c, 'd', d)


# 12 - masala
def Sortinc3(A, B, C):
    if A > B:
        A, B = B, A
    if B > C:
        B, C = C, B
    if A > B:
        A, B = B, A

    return A, B, C


A1 = int(input('A1: '))
B1 = int(input('B1: '))
C1 = int(input('C1: '))

A2 = int(input('A2: '))
B2 = int(input('B2: '))
C2 = int(input('C2: '))

A1, B1, C1 = Sortinc3(A1, B1, C1)
A2, B2, C2 = Sortinc3(A2, B2, C2)

print("Sorted (A1, B1, C1):", A1, B1, C1)
print("Sorted (A2, B2, C2):", A2, B2, C2)


# 13 - masala
def Sortinc3(A, B, C):
    if A < B:
        A, B = B, A
    if B < C:
        B, C = C, B
    if A < B:
        A, B = B, A

    return A, B, C


A1 = int(input('A1: '))
B1 = int(input('B1: '))
C1 = int(input('C1: '))

A2 = int(input('A2: '))
B2 = int(input('B2: '))
C2 = int(input('C2: '))

A1, B1, C1 = Sortinc3(A1, B1, C1)
A2, B2, C2 = Sortinc3(A2, B2, C2)

print("Sorted (A1, B1, C1):", A1, B1, C1)
print("Sorted (A2, B2, C2):", A2, B2, C2)



# 14 - masala
def ShiftRight(A, B, C):
    A1 = B
    B1 = C
    C1 = A
    A2 = B1
    B2 = C1
    C2 = A1
    return (A1, B1, C1), (A2, B2, C2)

A = int(input('A ni kiritng:'))
B = int(input('B ni kiritng:'))
C = int(input('C ni kiritng:'))

result1, result2 = ShiftRight(A, B, C)
print(f"(A1, B1, C1): {result1}")
print(f"(A2, B2, C2): {result2}")


# 15 - masala
def ShiftRight(A, B, C):
    A1 = C
    B1 = A
    C1 = B
    A2 = C1
    B2 = A1
    C2 = B1
    return (A1, B1, C1), (A2, B2, C2)

A = int(input('A ni kiritng:'))
B = int(input('B ni kiritng:'))
C = int(input('C ni kiritng:'))

result1, result2 = ShiftRight(A, B, C)
print(f"(A1, B1, C1): {result1}")
print(f"(A2, B2, C2): {result2}")


# 16 - masala
def Ishora(number):
    if number < 0:
        return -1
    elif number > 0:
        return 1
    else:
        return 0

a = int(input())
b = int(input())

result = Ishora(a) + Ishora(b)

print(f"ishora(a) + ishora(b) = {result}")


# 17 - masala
import math
def find_roots(A, B, C):

    discriminant = (B ** 2) - (4 * A * C)

    if discriminant > 0:
        root1 = (-B + math.sqrt(discriminant)) / (2 * A)
        root2 = (-B - math.sqrt(discriminant)) / (2 * A)
        return root1, root2
    elif discriminant == 0:
        root = -B / (2 * A)
        return root, root
    else:

        real_part = -B / (2 * A)
        imaginary_part = math.sqrt(-discriminant) / (2 * A)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2


A = int(input())
B = int(input())
C = int(input())


root1, root2 = find_roots(A, B, C)


print(f"Root 1: {root1}")
print(f"Root 2: {root2}")


# 18 - masala
def Doira(radius):
    pi = 3.1415
    area = pi * radius**2
    return area

radius1 = int(input())
radius2 = int(input())
radius3 = int(input())

area1 = Doira(radius1)
area2 = Doira(radius2)
area3 = Doira(radius3)

print(f"Doira 1 area -", area1)
print(f"Doira 2 area -", area2)
print(f"Doira 3 area -", area3)


# 19 - masala
def RingS(R1, R2):
    pi = 3.1415
    area1 = pi * R1 ** 2
    area2 = pi * R2 ** 2
    ring_area = abs(area1 - area2)
    return ring_area


R1 = float(input())
R2 = float(input())

ring_area = RingS(R1, R2)

print(f"Ring area: {ring_area}")


# 20 - masala
from math import sqrt
def TrieangleP(A, B):
    perimetr = A + B + sqrt(A**2 + B**2)
    return perimetr

A = int(input())
B = int(input())
perimetr = TrieangleP(A, B)
print('Perimetr:', perimetr)


# 21 - masala
def SumRange(A, B, C):
    if A > B:
        return 0

    sum_a_to_b = sum(range(A, B+1))
    print('a b', sum_a_to_b)
    sum_b_to_c = sum(range(B, C+1))
    print('b c', sum_b_to_c)
    print(sum(range(B, C+1)))

    return sum_a_to_b + sum_b_to_c

A = int(input())
B = int(input())
C = int(input())

result = SumRange(A, B, C)
print('Sum', result)


# 22 - masala
def Calc(A, B, Op):
    if Op == 1:
        return A - B
    elif Op == 2:
        return A * B
    elif Op == 3:
        if B != 0:
            return A / B
        else:
            return 'Xato nolga bolinish'
    elif Op == 4:
        return A + B
    else:
        print('Bunday raqam mavjud emas!')

A = float(input())
B = float(input())

N1 = Calc(A, B, 1)
N2 = Calc(A, B, 2)
N3 = Calc(A, B, 3)
N4 = Calc(A, B, 4)

print('Ayirish', N1)
print('Kopaytirish', N2)
print('Bolish', N3)
print('Qoshish', N4)


# 23 - masala
def Quarter(X, Y):
    if X > 0 and Y > 0:
        return '1-chorak'
    elif X < 0 and Y > 0:
        return '2-chorak'
    elif X < 0 and Y < 0:
        return '3-chorak'
    elif X > 0 and Y < 0:
        return '4-chorak'
    else:
        print('Hech qanday chorakga yotmaydi')

X = int(input())
Y = int(input())
result = Quarter(X, Y)
print(result)


# 24 - masala
def Even(K):
    if K % 2 == 0:
        return 'Juft'
    else:
        return 'Toq'

num1 = int(input())
num2 = int(input())
num3 = int(input())
result1 = Even(num1)
result2 = Even(num2)
result3 = Even(num3)

print(result1)
print(result2)
print(result3)


# 25 - masala
def IsQuare(K):
    if K <= 0:
        return False

    kvadrat = int(K ** 0.5) # 4**0.5 = 2
    print('kv', kvadrat)

    return kvadrat * kvadrat == K

number = int(input('A: ')), int(input('B: ')), int(input('C: ')) # 4,7,16

for num in number:
    result = IsQuare(num)
    print(f"{number}: {result}")


# 26 - masala
def IsPower5(K):
    if K <= 0:
        return False

    while K > 1:
        if K % 5 != 0:
            return False
        K /= 5
    return True


numbers = int(input('1: ')), int(input('2: ')), int(input('3: ')), int(input('4: ')),int(input('5: '))

for number in numbers:
    result = IsPower5(number)
    print(f"{number}: {result}")


# 27 - masala
def IsPowerN(K, N):
    if K <= 0 or N <= 0:
        return False

    while K > 1:
        if K % N != 0:
            return False
        K //= N

    return True

numbers = [(125, 5), (24, 3), (3125, 5), (100, 2), (625, 5)]

for number, power in numbers:
    result = IsPowerN(number, power)
    print(f"{number} ning darajasi {power}: {result}")


# 28 - masala
def IsPrime(N):
    if N <= 1:
        return False

    for i in range(2, N):
        if N % i == 0:
            return False

    return True


K = int(input("K: "))

count = 0
for num in range(2, K+1):
    if IsPrime(num):
        count += 1

print(f"{K}: tub sonlar {count} ta")


# 29 - masala
def DigitCount(K):
    if K <= 0:
        return 0

    count = 0
    while K > 0:
        count += 1
        K //= 10


    return count

N = 5
for i in range(N):
    enter = f"{i+1}-chi soni kiriting: "
    num = int(input(enter))
    result = DigitCount(num)
    print(f"Kiritilgan raqam {num}: {result}")


# 30 - masala
def DigitN(K, N):
    if K <= 0:
        return -1
    K = str(K)
    print('K', K)

    if N > len(K):
        return -1
    else:
        print(int(K[N-1])) # 123,2 = [1,2,3] = 2 indexni oladi
        return int(K[N-1])


K1 = int(input())
N = int(input())
result1 = DigitN(K1, N)
print(f'K1 ning {N} raqami', result1)

K2 = int(input())
N = int(input())
result2 = DigitN(K2, N)
print(f"K2 ning {N} raqami", result2)

K3 = int(input())
N = int(input())
result3 = DigitN(K3, N)
print(f"K3 ning {N} raqami", result3)



# 31 - masala
def IsPalindrom(N):
    N = str(N)
    print('N', N)
    length = len(N)
    print('lenth', length)
    for i in range(length // 2):
        if N[i] != N[length - i - 1]:
            print('N[i]', N[i], 'va', 'N[lenth-i]', N[length - i - 1])
            return False
    return True

def CountPalindromes(start, end):
    count = 0
    for number in range(start, end + 1):
        print('number', number)
        if IsPalindrom(number):
            count += 1
            print('count', count)
    return count

start = int(input())
end = int(input())
result = CountPalindromes(start, end)
print(f"{start} dan {end} gacha {result} ta palindrom son mavjud.")



# 32 - masala
from math import radians

def DegToRad(D):
    return radians(D)

D = 3
for i in range(D):
    enter = f"{i+1}-chi burchakni kiriting: "
    burchak = int(input(enter))
    result = DegToRad(burchak)
    print(f"Kiritilgan burchak {burchak} ni radiani {result}")



# 33 - masala
from math import degrees

def RadToDeg(R):
    return degrees(R)

R = 3
for i in range(R):
    enter = f"{i+1}-chi radianni kiriting: "
    radian = float(input(enter))
    result = RadToDeg(radian)
    print(f"Kiritilgan radian {radian} ni gradus {result}")



# 34 - masala
def Fact(N):
    if N == 0 or N == 1:
        return 1
    else:
        print('n', N * Fact(N-1))
        return N * Fact(N - 1)

number = 3
for num in range(number):
    enter = f"{num+1}-chi factorialni kiriting: "
    factor = int(input(enter))
    result = Fact(factor)
    print(f"{factor} ni faktoriali: {result}")


# 35 - masala
def Fact(N):
    if N == 0 or N == 1:
        return 1
    else:
        print('n', N * Fact(N-2))
        return N * Fact(N - 2)

number = 3
for num in range(number):
    enter = f"{num+1}-chi factorialni kiriting: "
    factor = int(input(enter))
    result = Fact(factor)
    print(f"{factor} ni faktoriali: {result}")


# 36 - masala
def Fib(N):
    if N <= 0:
        return []
    elif N == 1:
        return [0]
    elif N == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        while len(fib) < N:
            next_number = fib[-1] + fib[-2]
            fib.append(next_number)
        return fib

numbers = 3
for num in range(numbers):
    number = f"{num+1}-chi fibonachini kiritng: "
    n = int(input(number))
    result = Fib(n)
    print(f"Fibonachchi {n}-elementlari: {result}")


# 37 - masala
def Power1(A, B):
    return A**B

A1 = int(input('A1: '))
A2 = int(input('A2: '))
A3 = int(input('A3: '))
B = int(input('B: '))

result1 = Power1(A1, B)
result2 = Power1(A2, B)
result3 = Power1(A3, B)

print(f"{A1} ning {B} darajasi: {result1}")
print(f"{A2} ning {B} darajasi: {result2}")
print(f"{A3} ning {B} darajasi: {result3}")



# 38 - masala
def Power2(A, N):
    if N == 0:
        return 1
    elif N > 0:
        result = 1
        for i in range(N):
            print('i', i)
            result *= A
            print('result1', result)
        return result
    else:
        result = 1
        for j in range(abs(N)):
            print('j', j)
            result *= A
            print('result2', result)
        print('1/result', 1 / result)
        return 1 / result


A = float(input('A: '))
N = int(input("N: "))
M = int(input("M: "))
K = int(input("K: "))

result1 = Power2(A, N)
result2 = Power2(A, M)
result3 = Power2(A, K)

print('A ni N darajasi', result1)
print('A ni M darajasi', result2)
print('A ni K darajasi', result3)


# 39 - masala

def Power1(A, B):
    return A ** B


def Power2(A, N):
    if N == 0:
        return 1
    elif N > 0:
        result = 1
        for i in range(N):
            result *= A
        return result
    else:
        result = 1
        for j in range(abs(N)):
            result *= A
        return 1 / result


def Power3(A, N):
    if N % 1 != 0:  # Kasr qismi 0 dan farqli bo'lsa
        print('BU power2', Power2(A, int(N)))
        return Power2(A, int(N))
    else:
        print('BU power1', Power1(A, int(N)))
        return Power1(A, int(N))


A = float(input('A: ')) # 2.5
N = float(input('N: ')) # 3.2
M = float(input('M: ')) # 4.7
K = float(input('K: ')) # -2.9

result1 = Power3(A, N)
result2 = Power3(A, M)
result3 = Power3(A, K)

print(f"{A} ning {N} chi darajasi: {result1}")
print(f"{A} ning {M} chi darajasi: {result2}")
print(f"{A} ning {K} chi darajasi: {result3}")


# 40 - masala
def factorial(n):
    if n == 0:
        return 1
    else:
        print('n*factorial', n * factorial(n - 1))
        return n * factorial(n - 1)


def Exp1(x, e):
    result = 1
    s = 1
    n = 1

    while s >= e:
        s = x**n / factorial(n)
        print('s', s)
        result += s
        print('res', result)
        n += 1
        print('n', n)

    return result

x = float(input('x: '))  # 2.5
e1 = float(input('e1: '))  # 0.1
e2 = float(input('e2: ')) # 0.01
e3 = float(input('e3: '))  # 0.001

result1 = Exp1(x, e1)
result2 = Exp1(x, e2)
result3 = Exp1(x, e3)

print(f"Exp1({x}, {e1}) = {result1}")
print(f"Exp1({x}, {e2}) = {result2}")
print(f"Exp1({x}, {e3}) = {result3}")


# 41 - masala
def factorial(n):
    if n == 0:
        return 1
    else:
        # print('n*factorial', n * factorial(n - 1))
        return n * factorial(n - 1)

def sin1(x, e):
    result = 0
    s = x
    n = 1

    while abs(s) >= e:
        print('abs', abs(s))
        result += s
        print('result', result)
        s = (-1) ** n * x ** (2 * n + 1) / factorial(2 * n + 1)
        print('nnn',  (-1) ** n * x ** (2 * n + 1) / factorial(2 * n + 1))
        print('s', s)
        n += 1
        print('n', n)
    print('res', result)
    return result

x = float(input('x: ')) # 1.5
e1 = float(input('e1: '))  # 0.1
e2 = float(input('e2: '))   # 0.01
e3 = float(input('e3: '))   # 0.001

result1 = sin1(x, e1)
result2 = sin1(x, e2)
result3 = sin1(x, e3)

print(f"sin1({x}, {e1}) = {result1}")
print(f"sin1({x}, {e2}) = {result2}")
print(f"sin1({x}, {e3}) = {result3}")


# 42 - masala
import math
def cos1(x, e):
    result = 1
    s = 1
    n = 1

    while math.fabs(s) > e:
        print('math', math.fabs(s))
        s *= -x * x / ((2 * n) * (2 * n - 1))
        print('s', s)
        result += s
        print('result', result)
        n += 1

    return result


x = float(input('x: '))  # 1.0
e1 = float(input('e1: '))  # 0.1
e2 = float(input('e2: '))  # 0.01
e3 = float(input('e3: '))  # 0.001

result1 = cos1(x, e1)
result2 = cos1(x, e2)
result3 = cos1(x, e3)

print(f"{x} ni {e1} - {result1}")
print(f"{x} ni {e2} - {result2}")
print(f"{x} ni {e3} - {result3}")


# 43 - masala
import math

def ln1(x, e):
    result = 0
    s = x
    n = 1

    while math.fabs(s) > e:
        result += s
        s *= -x * n / (n + 1)
        n += 1

    return result
x = float(input('x: '))  # 0.5
e1 = float(input('e1: '))  # 0.1
e2 = float(input('e2: '))  # 0.01
e3 = float(input('e3: '))  # 0.001

print(ln1(x, e1))
print(ln1(x, e2))
print(ln1(x, e3))


# 44 - masala
import math

def Arctg1(x, e):
    result = 0
    s = x
    n = 1

    while math.fabs(s) > e:
        result += s
        s *= -x * n / (2 * n + 1)
        n += 1

    return result
x = float(input('x: '))
e1 = float(input('e1: '))
e2 = float(input('e2: '))
e3 = float(input('e3: '))

print(Arctg1(x, e1))
print(Arctg1(x, e2))
print(Arctg1(x, e3))


# 45 - masala
import math

def power4(x, a, e):
    result = 1
    s = 1
    n = 1

    while math.fabs(s) > e:
        s *= a * (a - 1 - n) * x / (n * (n + 1))
        print('s', s)
        result += s
        print('result', result)
        n += 1

    return result

x = float(input('x: '))  # 0.5
a = int(input('a: '))  # 2
e1 = float(input('e1: '))   # 0.1
e2 = float(input('e2: '))  # 0.01
e3 = float(input('e3: '))   # 0.001

result1 = power4(x, a, e1)
result2 = power4(x, a, e2)
result3 = power4(x, a, e3)

print(f"{x} - {a} - {e1} = {result1}")
print(f"{x} - {a} - {e2} = {result2}")
print(f"{x} - {a} - {e3} = {result3}")


# 46 - masala
def Ekub(A, B):
    while B != 0:
        A, B = B, A % B
        print('A, B', A, B, 'AND', 'B,', B)
    return A

A = int(input('A: '))
B = int(input('B: '))
C = int(input('C: '))
D = int(input('D: '))


print(Ekub(A, B))
print(Ekub(A, C))
print(Ekub(A, D))


# 47 - masala
def Frac1(a, b, p, q):
    num = a * q + p * b
    print('a,q,p,b', a,q,p,b)
    print('num', num)
    d = b * q
    print('d', d)
    s = Ekub(num, d)
    print('s',s)
    sn = num // s
    print('sn', sn)
    sd = d // s
    print('sd', sd)
    return sn, sd


def Ekub(A , B):
    while B != 0:
        A, B = B, A % B
    return A


a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))
d = int(input('D: '))
p = int(input('p: '))
q = int(input('q: '))

p1, q1 = Frac1(a, b, p, q)
p2, q2 = Frac1(a, c, p, q)
p3, q3 = Frac1(a, d, p, q)


print(f"({a}/{b}) = ({p1}/{q1})")
print(f"({a}/{c}) = ({p2}/{q2})")
print(f"({a}/{d}) = ({p3}/{q3})")


# 48 - masala
def Ekub(A, B):
    while B != 0:
        A, B = B, A % B
        print('A,B', A, B, 'va', B)
    return A


def Ekuk(A, B):
    ekub = Ekub(A, B)
    print('ekub', ekub)
    return (A * B) // ekub


A = int(input('A: '))
B = int(input('B: '))
C = int(input('C: '))
D = int(input('D: '))

ekuk1 = Ekuk(A, B)
ekuk2 = Ekuk(A, C)
ekuk3 = Ekuk(A, D)

print(f"EKUK{A},{B} = {ekuk1}")
print(f"EKUK{A},{C} = {ekuk2}")
print(f"EKUK{A},{D} = {ekuk3}")


# 49 - masala
def Ekub(A, B):
    while B != 0:
        A, B = B, A % B
    return A

def EKUB3(A, B, C):
    ekub_ab = Ekub(A, B)
    print('ekub_b', ekub_ab)
    ekub_abc = Ekub(ekub_ab, C)
    print('ekub_abc', ekub_abc)
    return ekub_abc


a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))
d = int(input('D: '))

ekub1 = EKUB3(a, b, c)
ekub2 = EKUB3(a, c, d)
ekub3 = EKUB3(a, b, d)


print(f"EKUB3 {a} - {b} - {c} = {ekub1}")
print(f"EKUB3 {a} - {c} - {d} = {ekub2}")
print(f"EKUB3 {a} - {b} - {d} = {ekub3}")


# 50 - masala
def TimeToHMS(T):
    H = T // 3600 # soat
    print(H)
    M = (T % 3600) // 60 # minut
    print(M)
    S = (T % 3600) % 60 # sekund
    print(S)
    return H, M, S

T = int(input('Sekund kiriting: '))

H, M, S = TimeToHMS(T)


print(f"{H}H : {M}M : {S}S")



# 51 - masala

def IncTime(H, M, S, T):
    total_seconds = H * 3600 + M * 60 + S
    print('total_sec', total_seconds)
    total_seconds += T
    print('TT', total_seconds)


    H = total_seconds // 3600
    M = (total_seconds % 3600) // 60
    S = (total_seconds % 3600) % 60

    return H, M, S

H = int(input('H soatni kiritng: '))
M = int(input('M minutni kiriting: '))
S = int(input('S sekundi kiritng: '))
T = int(input('T sekundga oshirish: '))

H, M, S = IncTime(H, M, S, T)

print(f"{H}H : {M}M : {S}S")


# 52 - masala
def IsLeap(Y):
    if Y % 4 == 0:
        if Y % 100 == 0:
            if Y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


y = int(input('Yilni kiriting -> '))
a = int(input('Yilni kiriting -> '))
b = int(input('Yilni kiriting -> '))
c = int(input('Yilni kiriting -> '))
d = int(input('Yilni kiriting -> '))
result1 = IsLeap(y)
result2 = IsLeap(a)
result3 = IsLeap(b)
result4 = IsLeap(c)
result5 = IsLeap(d)
print(f"{y} - Kabisa yili - {result1}")
print(f"{a} - Kabisa yili - {result2}")
print(f"{b} - Kabisa yili - {result3}")
print(f"{c} - Kabisa yili - {result4}")
print(f"{d} - Kabisa yili - {result5}")


# 53 - masala
def IsLeapYear(Y):
    if Y % 400 == 0 or (Y % 100 != 0 and Y % 4 == 0):
        return True
    else:
        return False


def MonthDays(M, Y):
    if M == 2:
        if IsLeapYear(Y):
            return 29
        else:
            return 28
    elif M in [4, 6, 9, 11]:
        return 30
    else:
        return 31



Y = int(input('Yilni kiriting: '))
M1 = int(input('M1 oyni kiritng: '))
M2 = int(input('M2 oyni kiritng: '))
M3 = int(input('M3 oyni kiritng: '))

days_M1 = MonthDays(M1, Y)
days_M2 = MonthDays(M2, Y)
days_M3 = MonthDays(M3, Y)

print(f"{Y} yilining {M1}-oyida {days_M1} kun, {M2}-oyida {days_M2} kun, {M3}-oyida {days_M3} kun bor.")


# 54 - masala

def IsLeapYear(Y):
    if Y % 400 == 0 or (Y % 100 != 0 and Y % 4 == 0):
        return True
    else:
        return False


def MonthDays(M, Y):
    if M == 2:
        if IsLeapYear(Y):
            return 29
        else:
            return 28
    elif M in [4, 6, 9, 11]:
        return 30
    else:
        return 31


def PrevDate(D, M, Y):
    if D > 1:
        return D - 1, M, Y
    if M > 1:
        prev_month = M - 1
        prev_year = Y
        prev_day = MonthDays(prev_month, prev_year)
        return prev_day, prev_month, prev_year
    else:
        prev_day = 31
        prev_month = 12
        prev_year = Y - 1
        return prev_day, prev_month, prev_year


D = int(input('Kun kiriting: '))
M = int(input('Oyni kiriting: '))
Y = int(input('Yilni kiriting: '))

prev_day, prev_month, prev_year = PrevDate(D, M, Y)

print(f"{D}Day-{M}Month-{Y}Year dan oldingi sana {prev_day}Day-{prev_month}Month-{prev_year}Year")


# 55 - masala
def IsLeapYear(Y):
    if Y % 400 == 0 or (Y % 100 != 0 and Y % 4 == 0):
        return True
    else:
        return False


def MonthDays(M, Y):
    if M == 2:
        if IsLeapYear(Y):
            return 29
        else:
            return 28
    elif M in [4, 6, 9, 11]:
        return 30
    else:
        return 31


def NextDate(D, M, Y):
    days_in_month = MonthDays(M, Y)
    if D < days_in_month:
        return D + 1, M, Y
    elif M < 12:
        next_month = M + 1
        next_year = Y
        next_day = 1
        return next_day, next_month, next_year
    else:
        next_day = 1
        next_month = 1
        next_year = Y + 1
        return next_day, next_month, next_year

D = int(input('Kun kiriting: '))
M = int(input('Oyni kiriting: '))
Y = int(input('Yilni kiriting:'))

next_day, next_month, next_year = NextDate(D, M, Y)

print(f"{D}day-{M}month-{Y}year dan keyingi sana: {next_day}day-{next_month}month-{next_year}year")


# 56 - masala
import math
def Length(X1, Y1, X2, Y2):
    distance = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)
    print('dist', distance)
    return distance

XA = int(input('XA: '))
YA = int(input('YA: '))
XB = int(input('XB: '))
YB = int(input('YB: '))
XC = int(input('XC: '))
YC = int(input('YC: '))
XD = int(input('XD: '))
YD = int(input('YD: '))

AB_distance = Length(XA, YA, XB, YB)
AC_distance = Length(XA, YA, XC, YC)
AD_distance = Length(XA, YA, XD, YD)

print(f"|AB| = {AB_distance}")
print(f"|AC| = {AC_distance}")
print(f"|AD| = {AD_distance}")


# 57 - masala
import math

def Length(X1, Y1, X2, Y2):
    distance = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)
    return distance


def Perim(Xa, Ya, Xb, Yb, Xc, Yc):
    AB = Length(Xa, Ya, Xb, Yb)
    BC = Length(Xb, Yb, Xc, Yc)
    CA = Length(Xc, Yc, Xa, Ya)
    perimetr = AB + BC + CA
    print('perimetr', perimetr)
    return perimetr

XA = int(input('XA: '))
YA = int(input('YA: '))
XB = int(input('XB: '))
YB = int(input('YB: '))
XC = int(input('XC: '))
YC = int(input('YC: '))
XD = int(input('XD: '))
YD = int(input('YD: '))

ABC_perimetr = Perim(XA, YA, XB, YB, XC, YC)
ABD_perimetr = Perim(XA, YA, XB, YB, XD, YD)
ACD_perimetr = Perim(XA, YA, XC, YC, XD, YD)


print(f"ABC ni perimetri - {ABC_perimetr}")
print(f"ABD ni perimetri - {ABD_perimetr}")
print(f"ACD ni perimetri - {ACD_perimetr}")


# 58 - masala
import math


def Length(X1, Y1, X2, Y2):
    distance = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)
    # print('dis', distance)
    return distance


def Area(Xa, Ya, Xb, Yb, Xc, Yc):
    AB = Length(Xa, Ya, Xb, Yb)
    BC = Length(Xb, Yb, Xc, Yc)
    CA = Length(Xc, Yc, Xa, Ya)
    s = (AB + BC + CA) / 2
    # print('s', s)
    area = math.sqrt(s * (s - AB) * (s - BC) * (s - CA))
    # print('area', area)
    return area


def Perimeter(Xa, Ya, Xb, Yb, Xc, Yc):
    AB = Length(Xa, Ya, Xb, Yb)
    BC = Length(Xb, Yb, Xc, Yc)
    CA = Length(Xa, Ya, Xc, Yc)

    perimeter = AB + BC + CA
    # print('perimetr: ', perimeter)
    return perimeter


XA, YA = int(input('XA: ')), int(input('YA: '))
XB, YB = int(input('XB: ')), int(input('YB: '))
XC, YC = int(input('XC: ')), int(input('YC: '))
XD, YD = int(input('XD: ')), int(input('YD: '))

area_abc = Area(XA, YA, XB, YB, XC, YC)
perimeter_abc = Perimeter(XA, YA, XB, YB, XC, YC)

area_abd = Area(XA, YA, XB, YB, XD, YD)
perimeter_abd = Perimeter(XA, YA, XB, YB, XD, YD)

area_acd = Area(XA, YA, XC, YC, XD, YD)
perimeter_acd = Perimeter(XA, YA, XC, YC, XD, YD)

print("ABC uchburchak yuzi:", area_abc)
print("ABC uchburchak perimetri:", perimeter_abc)

print("ABD uchburchak yuzi:", area_abd)
print("ABD uchburchak perimetri:", perimeter_abd)


print("ACD uchburchak yuzi:", area_acd)
print("ACD uchburchak perimetri:", perimeter_acd)


# 59 - masala
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def heron_formula(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def Area(Xa, Ya, Xb, Yb, Xc, Yc):
    AB = distance(Xa, Ya, Xb, Yb)
    BC = distance(Xb, Yb, Xc, Yc)
    AC = distance(Xa, Ya, Xc, Yc)
    area_ABC = heron_formula(AB, BC, AC)
    return area_ABC


def Dist(Xa, Ya, Xb, Yb, Xp, Yp):
    area_ABC = Area(Xa, Ya, Xb, Yb, Xp, Yp)

    AB = distance(Xa, Ya, Xb, Yb)
    print('AB: ',AB)
    dist_P_AB = (2 * area_ABC) / AB
    print('dist_P_AB', dist_P_AB)
    return dist_P_AB



Xa, Ya = int(input('Xa: ')), int(input('Ya: '))
Xb, Yb = int(input('Xb: ')), int(input('Yb: '))
Xp, Yp = int(input('Xp: ')), int(input('Yp: '))

result = Dist(Xa, Ya, Xb, Yb, Xp, Yp)
print("P nuqtadan AB kesmaga tushurilgan balandlik:", result)


# 60 - masala 50/50

import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def heron_formula(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def Area(Xa, Ya, Xb, Yb, Xc, Yc):
    AB = distance(Xa, Ya, Xb, Yb)
    BC = distance(Xb, Yb, Xc, Yc)
    AC = distance(Xa, Ya, Xc, Yc)

    area_ABC = heron_formula(AB, BC, AC)

    return area_ABC


def Dist(Xa, Ya, Xb, Yb, Xp, Yp):
    area_ABC = Area(Xa, Ya, Xb, Yb, Xp, Yp)

    AB = distance(Xa, Ya, Xb, Yb)
    dist_P_AB = (2 * area_ABC) / AB

    return dist_P_AB


def Heights(Xa, Ya, Xb, Yb, Xc, Yc, Ha, Hb, Hc):
    dist_AB = Dist(Xa, Ya, Xb, Yb, Xc, Yc)
    dist_BC = Dist(Xb, Yb, Xc, Yc, Xa, Ya)
    dist_AC = Dist(Xa, Ya, Xc, Yc, Xb, Yb)

    return dist_AB, dist_BC, dist_AC



Xa, Ya = int(input('Xa: ')), int(input('Ya: '))
Xb, Yb = int(input('Xb: ')), int(input('Yb: '))
Xc, Yc = int(input('Xc: ')), int(input('Yc: '))
Ha, Hb, Hc = int(input('Ha: ')), int(input('Hb: ')), int(input('Hc: '))


resultA = Heights(Xa, Ya, Xb, Yb, Xc, Yc, Ha, Hb, Hc)
resultB = Heights(Xa, Ya, Xb, Yb, Xc, Yc, Ha, Hb, Hc)
resultC = Heights(Xa, Ya, Xb, Yb, Xc, Yc, Ha, Hb, Hc)
print("A tomoniga tushurilgan balandlik:", resultA)
print("B tomoniga tushurilgan balandlik:", resultB)
print("C tomoniga tushurilgan balandlik:", resultC)




