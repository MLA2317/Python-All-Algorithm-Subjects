# 6 - Mavzu for sikl operatoriga oid masalalar

# 1 - masala
#For1. k va n butun sonlar berilgan(n > 0). k sonini n marta chiqaruvchi programma tuzilsin
n = int(input('Butun n son kiriting: '))
k = int(input('Butun k son kiriting: '))
if n > 0:
    for i in range(n):
        print(k)

# 2 - masala
#For2. a va b butun sonlar berilgan (a < b). a va b sonlar orasida barcha butun sonlar (a va b ni ham)  chiqaruvchi va
# chiqarolgan sonlar sonini chiqaruvchi programma tuzilsin ( a va b ni ham chiqarilsin)
a = int(input('a butun son kiriting: '))
b = int(input('b butun son kiriting: '))

if a < b:
    for i in range(a, b + 1):
        print('a and b among numbers', i)

# 3 - masala
#For3.  a va b butun sonlar berilgan (a < b). a va b sonlar orasida barcha butun sonlar (a va b dan tashqari)
# kamiyishi tartibida chiqaruvchi va chiqarilgan sonlar sonini chiqaruvchi progma tuzilsin.
a = int(input('a butun son kiriting: '))
b = int(input('b butun son kiriting: '))

count = 0

if a < b:
    for i in range(b-1, a, -1):
        print(i)
        count += 1
print("Chiqarilgan sonlar soni: ", count)

# 4 - masala
#For4. Bir kg konfetning narxi berilgan (haqiqiy son). 1,2, ...., 10 kg konfetni narxini chiqaruvchi programma tuzilsin
narxi = float(input('1 kg konfetni narxini kiriting: '))

for kg in range(1, 11):
    total_price = narxi * kg
    print(f"{kg} - kg, konfetni narxi - {total_price}")

# 5 - masala
#For5. Bir kg konfetning narxi berilgan (haqiqiy son). 0.1,0.2, ...., 0.9, 1 kg konfetni narxini chiqaruvchi programma tuzilsin
narxi = float(input('1 kg konfetni narxini kiriting: '))
for kg in range(1, 11):
    total_price = kg * narxi / 10
    print(f"{kg / 10} - kg, konfetni narxi - {total_price}")

# 6 - masala
#For6. Bir kg konfetning narxi berilgan (haqiqiy son). 1.2,1.4, ...., 2 kg konfetni narxini chiqaruvchi programma tuzilsin
narxi = float(input('1 kg konfetni narxini kiriting: '))
for kg in range(12, 21, 1):
    total_price = kg / 10 * narxi
    print(f"{(kg / 10)} - kg, konfetni narxi - {total_price}")

# 7 - masala
#For7. a va b butun sonlar berilgan (a < b). a dan b gacha bolgan barcha butun sonlar yegindisi chiqaruvchi programma tuzilsin
a = int(input('a butun son kiriting: '))
b = int(input('b butun son kiriting: '))
S = 0
if a < b:
    for i in range(a, b+1):
        print(i)
        S += i
print("Yegindisi: ", S)

# 8 - masala
#For8. a va b butun sonlar berilgan (a < b). a dan b gacha bolgan barcha butun sonlar kopaytmasi chiqaruvchi programma tuzilsin
a = int(input('a butun son kiriting: '))
b = int(input('b butun son kiriting: '))
S = 1
if a < b:
    for i in range(a, b+1):
        print(i)
        S *= i
print("Yegindisi: ", S)

# 9 - masala
#For9. a va b butun sonlar berilgan (a < b). a dan b gacha bolgan barcha butun sonlar kvadratlarining chiqaruvchi programma tuzilsin
a = int(input('a butun son kiriting: '))
b = int(input('b butun son kiriting: '))
S = 0
if a < b:
    for i in range(a, b+1):
        S += pow(i, 2)
        print(S)
print("Yegindisi: ", S)


# 10 - masala
#For10. n butun soni berilgan (n > 0). Quyidagi yigindini hisoblovchi programma tuzilsin
# S = 1 + 1/1 + 1/2 + 1/3 + ... + 1/n
n = int(input("Enter number n: "))
sum = 0

for i in range(1, n+1):
    sum += 1 / i
    print(sum)

sum += i

print(f"The sum S = {sum}")


# 11 - masala
#For11. n butun son berilgan (n > 0).  Quyidagi yigindini hisoblovchi programma tuzilsin
# # S = n kvadrat2 + (n + 1)kvadrat2 + (n + 2)kvadrat2 + ... + (2*n)kvadrat2
n = int(input("Enter number n: "))
sum = 0


for i in range(0, n + 1):
    sum += pow(n + i, 2)

print(f"The sum S = {sum}")


# 12 - masala
#For12. n butun son berilgan (n > 0).  Quyidagi kopaytmani hisoblovchi programma tuzilsin
# S = 1.1 * 1.2 * 1.3 * ... (n ta kopayuvchi)
n = int(input('n butun son kiriting: '))
s = 1
for i in range(1, n+1):
    s *= i
    print(s)

# 13 - masala
#For13. n butun son berilgan (n > 0).  Quyidagi yegindi hisoblovchi programma tuzilsin
# S = 1.1 + 1.2 - 1.3 + ... (n ta qoshiluvchi, ishorala al,ashib keladi. Shart operatoridan foydalanmang! )
n = int(input('n butun son kiriting: '))
s = 0
ishora = 1.1
for i in range(n):
    s += ishora
    ishora = (abs(ishora) + 0.1) * (-1) ** (i + 1)


print("Yig'indiz:", s)


# 14 - masala
#For14. n butun son berilgan (n > 0). Shu sonning kvadratini quyidagi formula asosida hisoblovchi programma tuzilsin
# n kvadrat2 = 1 + 3 + 5 + .. + (2*n - 1). har bir qoshiluvchidan keyingi natijadan chiqarib borin.
# Natijada ekranda 1 dan n gacha bolgan sonlar kvadrati chiqariladi
n = int(input('N butun son kiriting: '))
S = 0
for i in range(1, n+1):
    S += (2*i - 1)
    print(S)


# 15 - masala
#For15. n butun son berilgan va a haqiqiy son berilgan (n > 0). a ning n chi darajasini aniqlovchi programma tuzilsin!
# a ni n darajasi = a*a*a..a;
n = int(input('N butun son: '))
a = float(input('A haqiqiy son: '))
S = 1
for i in range(1, n+1):
    S *= a
print(f"{a} ning {n} darajasi = {S}")


# 16 - masala
#For16. n butun son berilgan va a haqiqiy son berilgan (n > 0). Bir sikldan foydalanib a ning 1 dan n gacha
# bolgan barcha darjalarini chiqaruvchi programma tuzilsin!
n = int(input('N butun son: '))
a = float(input('A haqiqiy son: '))
S = 1
for i in range(1, n+1):
    S = pow(a, i)
    print(S)

# 17 - masala
#For17. n butun soni va a hagigiy soni berilgan (n > 0). Bir sikldan foydalanib quyidagi a ning 1 dan n
# gacha bo'lgan barcha darajalarini chiqaruvchi va yig'indini hisoblovchi programma tuzilsin.
# 1 + a + a kvadrat2 + a kub3 + ... a"
n = int(input('N butun son: '))
a = float(input('A haqiqiy son: '))
sum = 0
for i in range(1, n+1):
    sum += a **i
    print(f"{a} ning, {i} darajasi", a**i)
print('Darajani yegindisi:', sum)


# 18 - masala
#For18. n butun soni va a hagiqiy soni berilgan (n > 0). Bir sikidan foydalanib quyidagi a ning 1 dan n
# gacha bo'lgan barcha darajalarini chiqaruchi va yig'indini hisoblovchi programma tuzilsin.
# 1 - a + a kvadrat2 + a kub3 + ... (-1)n chi darjasi a n darajasi.  Shart operatoridan foydalanilmasin.
n = int(input('N butun son: '))
a = float(input('A haqiqiy son: '))
sum = 0
for i in range(1, n+1):
    sum += (-1)**i * a **i
    print(f"{a} ning, {i} darajasi", a**i)
print('Darajani yegindisi:', sum)


# 19 - masala
#For19. n butun soni berilgan (n > 0). Birdan n gacha bo'lgan sonlar ko'paytmasini chiqaruvchi
# programma tuzilsin. n! = 1 * 2 *... n
# Birdan n gacha bo'igan sonlar ko' paytmasi n faktorial deyiladi.
n = int(input('N nutun son kiriting: '))
s = 1
for i in range(1, n + 1):
    s *= i
    print(f"{s}")


# 20 - masala
#For20. n butun soni berilgan (n > 0). Bir sikidan foydalangan holda quyidagi yig'indini hisoblovchi
# programma tuzilsin. 1! + 2!+ 3! + ... +n!
n = int(input('N nutun son kiriting: '))
s = 0
for i in range(1, n + 1):
    s += i
    print(f"{s}")


# 21 - masala
#For21. n butun soni berilgan (n > 0). Bir sikidan foydalangan holda quyidagi yig'indini hisoblovchi
# programma tuzilsin. (Olingan natija taxminan e = exp(1) ga yaqinlashadi)
# 1 + 1/(1!) + 1/(2!) + 1/(3!) + .. + 1/(n!)
from math import factorial
n = int(input("n sonini kiriting: "))
result = 0

for i in range(n+1):
    result += 1 / factorial(i)

print("Natija:", f"{result}!")


# 22 - masala
#For22. n butun soni va x haqiqiy soni berilgan (n > 0). Quyidagi yig'indini hisoblovchi programma
# tuzilsin. (Olingan natija taxminan e× ga yaqinlashadi)
# 1 + x + x kvadrat2 / (2!) + x kub3 / (3!) + ... + x n darjasi / (n!)
from math import factorial

n = int(input("n butun sonni kiriting: "))
x = float(input("x haqiqiy sonni kiriting: "))

result = 0

for i in range(n+1):
    result += x ** i / factorial(i)

print("Natija:", f"{result}!")


# 23 - masala
#For23. n butun soni va x haqiqiy soni berilgan (n > 0). Quyidagi yig'indini hisoblovchi programma
# tuzilsin. (Olingan natija taxminan sin(x) ga yaqinlashadi) x - x kub3 / (3!) + × darjasi5 / (5!) - ... + (-1) n darajasi x ni 2n+1 darajasi / ((2*n+1)!)
from math import factorial

n = int(input("n butun sonni kiriting: "))
x = float(input("x haqiqiy sonni kiriting: "))

result = 0

for i in range(n+1):
    s = (-1) ** i
    print(s)
    t = (s * x ** (2 * i + 1)) / factorial(2 * i + 1)
    print(t)
    result += t

print("Natija:", f"{result}!")


# 24 - masala
#For24. n butun soni va x haqiqiy soni berilgan (n > 0). Quyidagi yig'indini hisoblovchi programma
# tuzilsin. (Olingan natija taxminan cos(x) ga yaqinlashadi)
# 1 - x kvadrat2 / (2!) + × darajasi4 / (4!) - ... + (-1) n darajasi x ni 2n darajasi / ((2*n)!)
from math import factorial

n = int(input("n butun sonni kiriting: "))
x = float(input("x haqiqiy sonni kiriting: "))

result = 0

for i in range(n+1):
    s = (-1) ** i
    print(s)
    t = (s * x ** (2 * i + 1)) / factorial(2 * i)
    print(t)
    result += t

print("Natija:", f"{result}!")


# 25 - masala
#For25. n butun soni va x haqiqiy soni berilgan (n > 0, |x < 1). Quyidagi yig'indini hisoblovchi programma tuzilsin.
# x - x kvadrat2 / 2 + x kub3 / 3 - ....+ (-1) n - 1 darajasi x ni n darajasi / n
n = int(input("n butun sonni kiriting: "))
x = float(input("x haqiqiy sonni kiriting: "))

result = 0

for i in range(1, n + 1):
    result += ((-1) * (i - 1)) * (x * i) / i

print("Natija:", result)


# 26 - masala
#For26. n butun soni va x haqiqiy soni berilgan (n > 0, (x| < 1). Quyidagi yig'indini hisoblovchi programmatuzilsin
# x - x kub3 / 3 + x darajasi 5 / 5 - ... + (-1) n darajasi x ni 2n + 1 darajasi / (2n + 1)
n = int(input("n butun sonni kiriting: "))
x = float(input("x haqiqiy sonni kiriting: "))
result = 0
for i in range(n+1):
    result += ((-1) ** i) * (x ** (2 * i + 1)) / (2 * i + 1)
print("Result:", result)


# 27 - masala
#For27. n butun soni va x haqiqiy soni berilgan (n > 0, |×| < 1). Quyidagi yig'indini hisoblovchi programma tuziisin
# X + 1 * × kub3 / (2 * 3) + 1 * 3 * x darajasi5 / (2 * 4 * 5) + ... + 1 * 3 * ... * (2*n-1) * x darajasi2n+1 /(2 * 4 * ... * (2 * n)*(2*n+1))



# 28 - masala
#For28. n butun soni va x haqiqiy soni berilgan (n > 0, |×| < 1). Quyidagi yig'indini hisoblovchi programma tuzilsin
# 1 + X / 2 - 1 * X kvadrat2 / (2 * 4) + 1 * 3 * x kub3 / (2 * 4 * 6) - ... + (-1) darjasi n-1 * 1 * 3 ... *(2 * n - 3) * x darjasi n /(2*4*...*(2*n))


# 29 - masala
#For29. n butun soni va sonlar o'gida 2 ta A, B nuqta berilgan. (A, B haqiqiy son). [A, B] kesmani teng nta kesmaga bo'ling.
# [A, B] kesmada ajratilgan barcha nuqtalarni chiqaring

n = int(input('N butun son kiriting: '))
A = float(input('A haqiqiy son kiriting: '))
B = float(input('B haqiqiy son kiriting: '))

d = (B - A) / n
# print(d)
points = []
for i in range(n+1):
    x = A + i * d
    print(x)
    points.append(x)

print("Alohida points:")
for point in points:
    print(point)


# 30 - masala
#For30. n butun soni va sonlar o'gida 2 ta A, B nuqta berilgan. (A, B hagiqiy son). [A, B] kesmani teng n ta kesmaga bo'ling.
# [A, B] kesmada ajratilgan barcha nuqtalar uchun F(X) = 1 - sin(X) funksiya qiymatini hisoblang.
from math import *
n = int(input('N butun son kiriting: '))
A = float(input('A haqiqiy son kiriting: '))
B = float(input('B haqiqiy son kiriting: '))

d = (B - A) / n
points = []
f = []
for i in range(n+1):
    x = A + i * d
    points.append(x)
    f.append(1 - sin(x))
print("Ajratilgan nuqtalar va funksiya qiymatlari:")
for point, value in zip(points, f): # zip - bu int va str yoki int va int ha hakozo ni birlashtitib beradi
    print(f"X = {point:.2f}, F(X) = {value:.2f}") # .2f - bu sonlarni yaxlitlab beradi


# 31 - masala
#For31. n butun soni berilgan (n > 0). Quyidagi ketma - ketlikning dastlabki n ta hadini chiqaruvchi programma tuzilsin.
# A0 = 2;
# Ak = 2 + 1 / A.k-1
# K= 1,2, ...

n = int(input('N butun son kiriting: '))
A = 2
for k in range(1, n+1):
    print(f"A{k - 1} = {A}")
    A = 2 + 1 / A
print(f"A{n} = {A}")



# 32 - masala
# For32. n butun soni berilgan (n > 0). Quyidagi ketma - ketlikning dastlabki n ta hadini chiqaruvchi programma tuzilsin.
# A0 = 1;
# AK = (A.k-1 + 1) / K; K = 1,2, ...

n = int(input('N butun son kiriting: '))
A = 1
for k in range(1, n+1):
    print(f"A{k - 1} = {A}")
    A = (A + 1) / k

print(f"A{n} = {A}")


# 33 - masala
#For33. n butun soni berilgan (n > 1). Fibonachchi ketma - ketlikning dastlabki n ta hadini chigaruvchi programma tuzilsin.
# F1 = 1; F2 = 1;
# F.K = F.K-2 + F.k-1; K=3,4,...

n = int(input('N butun son kiriting: '))
F = [1, 2]

if n > 1:
    for k in range(2, n):
        print(k)
        F.append(F[k-1] + F[k-2])
        print('Nmf',F)

print(f"Fibonachi {n} ta hadi")
for i in range(n):
    print(F[i])


# 34 - masala
#For34. n butun soni berilgan (n > 1). Quyidagi ketma - ketlikning dastlabki n ta hadini chiqaruvchi programma tuzilsin.
# A1 = 1; A2 = 2;
# A.k = (A.k-2 + 2 * A.k-1) / 3;
# K=3,4,
n = int(input('N butun son kiritilgan: '))
A = [1, 2]
if n > 1:
    for k in range(1, n):
        A.append(A[k-2] + 2 * A[k-1])
        print(A)
print(f'Quyidagi {n} ta hadi')
for i in range(n):
    print(A[i])


# 35 - masala
#For35. n butun soni berilgan (n > 2). Quyidagi ketma - ketlikning dastlabki n ta hadini chiqaruvchi programma tuzilsin.
# A1 = 1; A2 = 2; A3 = 3; A.k = (A.k-1 + A.k-2 - 2 * A.k-3);
# K= 4,5,
n = int(input('N butun son kiritilgan: '))
A = [1, 2, 3]

for k in range(3, n):
    A.append(A[k-1] + A[k-2] - 2 * A[k-3])
print(f'Quyidagi {A} ta hadi')


# Ichma - ich ochilgan sikllar

# 36 - masala
#For36. N va K butun sonlari berilgan. Quyidagi yig'indini chiqaruvchi programma tuzilsin.
# 1 darajasi K + 2 darajasi K+ ... + N darajasi K
n = int(input('n butun son berilgan: '))
k = int(input('k butun son berilgan: '))
s = 0
for i in range(1, n+1):
    s = s + k**i
print('Yegindisi: ', s)


# 37 - masala
#For37. N butun soni berilgan. Quyidagi yig'indini chiqaruvchi programma tuzilsin.
# 1 darajasi 1 ÷ 2 darjasi 2 + ... + N darajasi N

n = int(input('N butun son kiriting: '))
s = 0
for i in range(1, n + 1):
    s += i ** i
print('Yegindisi:', s)


# 38 - masala
#For38. N butun soni berilgan. Quyidagi yig 'indini chigaruvchi programma tuzilsin.
# 1 darjasi N + 2 darajasi N-1 + ... + N darajasi 1

n = int(input('N butun son kiriting: '))
s = 0
for i in range(1, n+1):
    print(i)
    s += i ** n-1

    print('Yegindisi: ', s)


# 39 - masala
#For39. A va B butun soni berilgan (A < B). A va B sonlari orasidagi barcha butun sonlari chiqaruvchi
# programma tuzilsin. Bunda har bir son o zining qiymaticha chiqarilsin. Ya'ni 3 soni 3 marta chigariladi.

a = int(input('A butun son kiriting: '))
b = int(input('B butun son kiriting: '))
if a < b:
    for i in range(a, b+1):
        for j in range(1, i+1):
            print(i)


# 40 - masala
#For40. A va B butun soni berilgan (A < B). A va B sonlari orasidagi barcha butun sonlarni chiqaruvchi
# programma tuzilsin. Bunda A soni 1 marta, (A + 1) soni 2 marta chigariladi va xakazo.

A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))

for i in range(A, B + 1):
    for j in range(A, i + 1):
        print(i, end=" ")