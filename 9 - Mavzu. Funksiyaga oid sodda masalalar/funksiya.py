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


A1 = 10
B1 = 5
C1 = 8

A2 = 3
B2 = 6
C2 = 1

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


A1 = 5
B1 = 8
C1 = 10

A2 = 1
B2 = 3
C2 = 6

A1, B1, C1 = Sortinc3(A1, B1, C1)
A2, B2, C2 = Sortinc3(A2, B2, C2)

print("Sorted (A1, B1, C1):", A1, B1, C1)
print("Sorted (A2, B2, C2):", A2, B2, C2)





