# 4 - mavzu Shart operatoriga oid masalalar

# 1 - masala
# if1. Butun son berilgan. Agar, berilgan son musbat bo lsa, 1 ga oshirilsin, aks holda ozgartirilmasin.
# Hosil bo'lgan sonni ekranga chiqaruvchi programma tuzilsin.
a = int(input('A butun son kiriting: '))
s = 1
if a % 2 == 0:
    s += a
    print('1 ga qoshildi:', s)
else:
    print(a)

# 2 - masala
# if2. Butun son berilgan. Agar, berilgan son musbat bo'lsa, 1 ga oshiring, aks holda 2 ga kamaytiring.
# Hosil bo lgan sonni ekranga chiqaruvchi programma tuzilsin.
a = int(input('A butun son kiriting: '))
s = 0
if a % 2 == 0:
    s = a + 1
    print('1 ga oshirildi', s)
else:
    s = a - 2
    print('2 ga ayirildi', s)

# 3 - masala
# if3. Butun son berilgan. Agar, berilgan son musbat bo'lsa, 1 ga oshiring, agar manfiy bo'lsa 2 ga
# kamaytiring. Agar 0 ga teng bo'lsa, 10 ni ozlashtirsin. Hosil bo'lgan sonni ekranga chiqaruvchi
# programma tuzilsin.
a = int(input('A butun son kiriting: '))
s = 0
if a > 0:
    s = a + 1
    print('1 ga oshirildi', s)
elif a < 0:
    s = a - 2
    print('2 ga kamaytirildi', s)
else:
    s += a + 10
    print('10 ga ozlashtirdi', s)

# 4 - masala
# if4. Uchta butun son berilgan. Shu sonlar orasidan nechta musbat son borligini aniqlovchi programma
# tuzilsin.
a, b, c = int(input('a ni kiriting: ')), int(input('b ni kiritind: ')), int(input('c ni kiriting: '))
count = 0

if a > 0 :
    count += 1
elif b > 0:
    count += 1
elif c > 0:
    count += 1
print('Nechta musbat son bor:', count)

# 5 - masala
# if5. Uchta butun son berilgan. Shu sonlar orasidan nechta musbat va manfiy son borligini aniglovchi
# programma tuzilsin.
a, b, c = int(input('a ni kiriting: ')), int(input('b ni kiritind: ')), int(input('c ni kiriting: '))
musbat = 0
manfiy = 0

if a > 0:
    musbat += 1
elif a < 0:
    manfiy += 1
if b > 0:
    musbat += 1
elif b < 0:
    manfiy += 1
if c > 0:
    musbat += 1
elif c < 0:
    manfiy += 1

print("Manfiy:",manfiy, '\n' "Musbat:", musbat)

# 6 - masala
# if6. Ikkita butun son berilgan. Shu sonlarning kattasini aniqlovchi programma tuzilsin.
a = int(input('a ni kiriting: '))
b = int(input('b ni kiriting: '))
if a > b:
    print('A katta B dan:', a)
else:
    print('B katta A dan:', b)

# 7 - masala
# if7. Ikkita butun son berilgan. Shu sonlarning kichigini tartib ragamini aniqlovchi programma tuzilsin.
a = int(input('a ni kiriting: '))
b = int(input('b ni kiriting: '))

if a < b:
    print('Kichigi:', a)
elif a > b:
    print('Kichigi: ', b)

# 8 - masala
# if8. Ikkita butun son berilgan. Shu sonlarning avval kattasini keyin kichigini ekranga chiqaruvchi
# programma tuzilsin.
a = int(input('a ni kiriting: '))
b = int(input('b ni kiriting: '))

if a > b:
    print('Kattasi', a)
    print('Kichigi', b)
else:
    print('Kattasi', b)
    print('Kichigi', a)

# 9 - masala
# if9. A va B haqiqiy sonlari beringan. Shu sonlari shunday o'zgartirish kerakki, A son kichik B son katta
# bo'lsin. A va B ning qiymati ekranga chiqarilsin.
a = float(input('a ni kiriting: '))
b = float(input('b ni kiriting: '))
if a > b:
    a, b = b, a
print('A', a)
print('B', b)


# 10 - masala
# if10. A va B butun sonlari berilgan. Agar o'zgaruvchilar o'zaro teng bo'lmasa, A va B o'zgaruvchilari
# ularing yegindisini o zlashtirsin. Agar teng bo'lsa, 0 ni o'zlashtirsin. A va B ning qiymati ekranga
# chigarilsin.
a = int(input('a ni kiriting: '))
b = int(input('b ni kiriting: '))

if a != b:
    A = a + b
    B = a - b
else:
    A = 0
    B = 0
print('A', A)
print('B', B)

#11 - masala
# if11. A va B butun sonlari berilgan. Agar o'zgaruvchilar o'zaro teng bo'lmasa, A va B bu sonlarning
# kattasini o zlashtirsin. Agar teng bo'lsa, 0 ni o zlashtirsin. A va B ning qiymati ekranga chiqarilsin.
a = int(input('a ni kiriting: '))
b = int(input('b ni kiriting: '))

if a != b:
    S = max(a,b)
    D = min(a,b)
    if S > D or S < D:
        print('Kattasi', S)
        print('Kichigi', D)
else:
    A = 0
    B = 0
    print('A', A)
    print('B', B)

# 12-masala
# if12. Uchta son berilgan. Shu sonlarni kichigini aniqlovchi programma tuzilsin.
a = int(input('a ni kiriting '))
b = int(input('b ni kiriting '))
c = int(input('c ni kiriting '))
# 1 - usul
if a < b and a < c:
    print('Eng kichigi', a)
elif b < a and b < c:
    print('Eng kichigi', b)
elif c < a and c < b:
    print('Eng kichigi', c)
# 2 - usul
min = min(a, b, c)
print('Eng kichigi', min)

# 13 - masala
# if13. Uchta son berilgan. Shu sonlarni o'ratachasi (ya'ni katta va kichik sonlar orasidagi son) ni
# aniglovchi programma tuzilsin.
a = int(input('a ni kiriting '))
b = int(input('b ni kiriting '))
c = int(input('c ni kiriting '))

max = max(a, b, c)
min = min(a, b, c)

middle = a + b + c - min - max
print('Ortachasi', middle)

# 14 - masala
# if14. Uchta son berilgan. Shu sonlarni avval kichigini keyin kattasini ekranga chiqaruvchi programma
# tuzilsin.
a = int(input('a ni kiriting '))
b = int(input('b ni kiriting '))
c = int(input('c ni kiriting '))

max = max(a, b, c)
min = min(a, b, c)
print('Kichigi', min)
print('Kattasi', max)

# 15 - masala False
# if15. Uchta son berilgan. Shu sonlaring yig 'indisi eng katta bo'ladigan ikkitasini ekranga chiqaruvchi
# programma tuzilsin.
a = int(input('a ni kiriting '))
b = int(input('b ni kiriting '))
c = int(input('c ni kiriting '))
S = 0

if a >= b and a >= c:
    if b >= c:
        S = a + b
    else:
        S = a + c
elif b >= a and b >= c:
    if a >= c:
        S = b + a
    else:
        S = b + c
else:
    if a >= b:
        S = c + a
    else:
        S = c + b

print("Ikki yig'indi eng katta bo'lgan sonlar yig'indisi:", S)


# 16 - masala
# if16. A, B, C haqiqiy sonlari berilgan. Agar berilgan sonlar o'sish tartibida berilgan bo'lsa, sonlarni
# ikkilantiring, aks holda sonlarni ishorasi o'zgartirilsin. A, B, C ning qiymatlari ekranga chiqarilsin.
A = float(input('A ni kiriting: '))
B = float(input('B ni kiriting: '))
C = float(input('C ni kiriting: '))

if A < B < C or C < B < A:
    A *= 2
    B *= 2
    C *= 2
else:
    A = -A
    B = -B
    C = -C

print('A', A)
print('B', B)
print('C', C)

# 17 - masala
# if17. A, B, C hagiqiy sonlari berilgan. Agar berilgan sonlar o'sish yoki kamayish tartibida berilgan
# bo'lsa, sonlarni ikkilantiring, aks holda sonlarni ishorasi o'zgartirilsin. A, B, C ning qiymatlari ekranga
# chigarilsin.
A = float(input('A ni kiriting: '))
B = float(input('B ni kiriting: '))
C = float(input('C ni kiriting: '))

if A < B < C or A > B > C:
    A *= 2
    B *= 2
    C *= 2
else:
    A = -A
    B = -B
    C = -C
print('A', A)
print('B', B)
print('C', C)

# 18 - masala
# if18. Uchta butun son berilgan. Shu sonlarni ikkitasi o'zaro teng, qolgan bittasini tartib гaqami
# aniglansin.
a = int(input('a ni kiriting '))
b = int(input('b ni kiriting '))
c = int(input('c ni kiriting '))
result = 0
if a == b:
    result = c
elif a == c:
    result = b
elif b == c:
    result = a
else:
    print('Tartib raqam yoq')
print('Bitta tartib raqami', result)

# 19 - masala
# If19. To' itta butun son berilgan. Shu sonlari uchtasi o'zaro teng, golgan bittasini tartib raqami
# aniglansin.
a = int(input('a ni kiriting '))
b = int(input('b ni kiriting '))
c = int(input('c ni kiriting '))
d = int(input('d ni kiriting '))
result = 0

if a == b and a == c:
    result = d
elif b == c and b == d:
    result  = a
elif c == d and c == a:
    result = b
elif d == a and  d == b:
    result = c
else:
    print('Tartib raqam yoq')
print('Bitta tartib raqami', result)

# 20 - masala
# if20. Sonlar o' qida uchta A, B, C nugtalar berilgan. A nugtaga eng yagin nugta va ular orasidagi masofa
# topilsin.
x1, y1 = map(float, input('A: ').split()) # map bir nech marta float yoki int foydalanish uchun
x2, y2 = map(float, input('B: ').split())
x3, y3 = map(float, input('C: ').split())

dist_AB = ((x2 - x1)**2 + (y2 - y1)**2)
print(dist_AB)
dist_AC = ((x3 - x1)**2 + (y3 - y1)**2)
print(dist_AC)
dist_BC = ((x3 - x2)**2 + (y3 - y2)**2)
print(dist_BC)

min_dist = min(dist_AB, dist_AC, dist_BC)
print('eng yaqin nuqtani orasidagi masofa: ',min_dist)

# 21 - masala
# if21. Koordinatalar tekisligida butun son berilgan. Agar nuqta koordinata boshida yotsa, 0 chiqarilsin.
# Agar nugta OX yoki OY o'qlarida joylashsa mos holda 1 va 2 chiqarilsin. Agar nugta koordinata o'qida
# joylashmasa 3 chiqarilsin.
x, y = map(int, input('x va y son kiriting: ').split())
if x == 0 and y == 0:
    print(0)
elif x != 0 and y != 0:
    print(3)
elif x == 0 or y == 0:
    print(1, 2)
else:
    print(2)

# 22 - masala
# OX va OY koordinata o'qlarida yotmaydigan nuqta berilgan. Nuqta joylashgan koordinata choragi
# aniglansin.
x, y = map(int, input('x va y sonlar kiriting: ').split())
if x == 0 and y == 0:
    print('OX va OY koordinata oqlariga joylashgan')
else:
    if x > 0 and y > 0:
        choragi = '1 - chi chorak'
    elif x < 0 and y > 0:
        choragi = '2 - chi chorak'
    elif x < 0 and y < 0:
        choragi = '3 - chi chorak'
    else:
        choragi = '4 - chi choral'
    print('Nuqta joylashgan koordinata choragi: ', choragi)

# 23 - masala
# if23. Koordinata o'qlariga parallel ravishda to'g' ri to rtburchakning uchta uchi berilgan, to'rtinchi uchi
# koordinatasini aniglansin.
x1, y1 = map(int, input('x1 va y1 uchini kiriting: ').split())
x2, y2 = map(int, input('x2 va y2 uchini kiriting: ').split())
x3, y3 = map(int, input('x3 va y3 uchini kiriting: ').split())

if x1 == x2:
    x4 = x3
elif x1 == x3:
    x4 = x2
else:
    x4 = x1

if y1 == y2:
    y4 = y3
elif y1 == y3:
    y4 = y2
else:
    y4 = y1

print('Tortinchi uchi koordinatani: ', x4, y4)

# 24 - masala
# if24. X haqiqiy soni berilgan. Quyidagi funksiya hisoblansin.
# f (x) =
# 2 * sin(x), agar x > 0;
# | x -6, agar x <= 0;
from math import sin
x = float(input('Son kiriting: '))

if x > 0:
    f = 2 * sin(x)
elif x <= 0:
    f = x - 6
    print(f"f({x}) = {f}")

# 25 - masala
# if25. X haqigiy soni berilgan. Quyidagi funksiya hisoblansin.
# f(x)=
# [2*x, agar x < -2 yoki x > 2;
# -3*x aks holda ;
x = float(input('Son kiriting: '))
if x < -2 or x > 2:
    f = 2 * x
else:
    f = -3 * x
print(f"f({x}) = {f}")

# 26 - masala
# if26. X hagigiy soni berilgan. Quyidagi funksiya hisoblansin.
# f = x
# - x, agar x <= 0:
# x**2, agar 0<x<2;
# 4, agar x>=2;
x = float(input('Son kiriting: '))
if x <= 0:
    f = -x
elif 0 < x < 2:
    f = pow(x, 2)
elif x >= 2:
    f = 4
print(f"f({x} = {f})")

# 27 - masala
# if27. X haqiqiy soni berilgan. Quyidagi funksiya hisoblansin.
# f(x) =
# 0, agar x < 0;
# 1, agar x € [0,1) (2,3)...
# -1, agar r€ (1,2). 3.4)..
x = float(input('Son kiriting: '))
if x < 0:
    f = 0
elif x % 2 == 0:
    f = 1
else:
    f = -1
    print(f"f({x}) = {f}")

# 28 - masala
# if28. Yil berilgan (musbat butun son). Berilgan yilda nechta kun borligini aniqlovchi programma tuzilsin.
# Kabisa yilida 366 kun bor, kabisa bo'lmagan yilda 365 kun bor. Kabisa yil deb 4 ga karrali villarga
# aytiladi. Lekin 100 ga karrali yillar ichida faqat 400 ga karrali bo'lganlari kabisa yil hisoblanadi.
# Masalan 300, 1300 va 1900 kabisa vili emas. 1200 va 2000 kabisa yili.
n = int(input('Butun son kiriting: '))
if n % 4 == 0:
    if n % 100 == 0:
        if n % 400 == 0:
            kabisa_yil = 366
        else:
            kabisa_yil = 365
    else:
        kabisa_yil = 366
else:
    kabisa_yil = 365

print(f"{n} yil {kabisa_yil} kun bor")


# 29 - masala
# if29. Butun son berilgan. Berilgan sonni "musbat toq son", "manfiy juft son", 'son nolga teng* va x.k.
# ekranga yozadigan programma tuzilsin.
n = int(input('Butun son kiriting: '))
if n > 0 and n < 99:
    if n % 2 != 0:
        print('Musbat toq son')
    else:
        print('Manfiy juft son')
elif n < 0:
    if n % 2 == 0:
        print('Manfiy juft son')
    else:
        print('Musbat juft son')
elif n > 99:
    if n % 2 != 0:
        print('Uch xonali toq son')
    else:
        print('Uch xonali emas')

# 30 - masala
# if30. 1-999 oraliqdagi sonlar berilgan. Berilgan sonni "ikki xonali juft son*, "uch xonali toq son* va x.k.
# ekranga yozadigan programma tuzilsin.
n = int(input('Butun son kiriting: '))
if n >= 10 and n <= 99 and n % 2 == 0:
    print('Ikki honali son juft son')
elif n >= 100 and n <= 999 and n % 2 != 0:
    print('Uch xonali son toq son')
else:
    print('Bunday son mavjud emas')
