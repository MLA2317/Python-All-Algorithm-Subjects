# 7 - Mavzu. Shart sikl operatori (While)

# 1 - masala
# While1. A va B butun musbat sonlari berilgan ( A > B). A usunlikdagi kesmada maksimal darajada B
# kesma joylashtirilgan. A kesmaning bo'sh qismini aniqlovchi programma tuzilsin. Ko'paytirish va bo'lish
# amallarini ishlatmang.
a = int(input('A butun sonni kiriting: '))
b = int(input('B butun sonni kiriting: '))

while a >= b:
    a = a - b


print("A kesmaning bo'sh qismi:", a)


# 2 - masala
# While2. A va B butun musbat sonlari berilgan ( A > B). A usunlikdagi kesmada B kesmadan nechta
# joylashtirish mumkinligini aniglovchi programma tuzilsin. Ko'paytirish va bo'lish amallarini ishlatmang.
A = int(input("A ni kiriting: "))
B = int(input("B ni kiriting: "))

count = 0
while A >= B:  # 12 3
    A = A - B  # 9, 6, 3, 0
    count += 1

print("B kesmadan joylashtirish mumkinligi:", count)


# 3 - masala
# While3. N va K butun musbat sonlari berilgan. Faqat ayirish va qo'shish amallarini ishlatib N sonini K
# soniga bo'lgandagi qoldiq va butun qismini aniqlovchi programma tuzilsin.
n = int(input('N butun son kiritining: '))
k = int(input('K butun son kiriting: '))

qoldiq = n
count = 0

while qoldiq >= k:
    qoldiq -= k
    count += 1
print('Qoldigi: ', qoldiq)
print('Butun qismi:', count)


# 4 - masala
# While4. n butun soni berilgan (n > 0). Agar n soni 3 ning darajasi bo'lsa "3 - ning darajasi*, aks xolda "3 -ning darajasi emas"
# degan natija chiqaruvchi programma tuzilsin. Qoldigli bo'lish va bo'lish amallarini ishlatmang.

n = int(input('N butun son berilgan: '))
while n >= 3:
    if n == 3:
        print('3 ning darajasi')
        break
    n -= 3
if n != 3:
    print('3 ning darajasi emas!')


# 5 - masala
# While5. 2 sonining qandaydir darajasini bildiruvchi n butun soni berilgan (n > 0). n = 2 darajasi k.
# k ni aniqlovchi programma tuzilsin.
n = int(input('N butun son kiriting: '))
k = 0
while n % 2 == 0: # 12
    n = n // 2
    print(n)
    k += 1
print('k:', k)


# 6 - masala
# While6. n natural soni berilgan (n > 0). Quyidagi ifodani hisoblovchi programma tuzilsin:
# n!! = n * (n - 2) * (n - 4)...
# Agar n juft bo'lsa oxirgi ko'payuvchi 2, toq bo'lsa 1 bo'ladi.

n = int(input('N butun son kiriting: '))
count = 1
while n > 0:
    if n % 2 == 0:
        print(n)
        count *= 2
        print(count)
    else:
        count *= 1
    n -= 2
    print(n)
print('Result:', count)


# 7 - masala
# While7. n natural soni berilgan (n > 0). Kvadrati n dan katta bo'ladigan eng kichik butun k sonini (k darajasi 2 > n)
# aniqlovchi programma tuzilsin. Ildizdan chiqaruvchi funksiyadan foydalanmang.

n = int(input('Butun son kiriting: '))
k = 1
while k**2 <= n:  # 12,
    # print(k)
    k += 2 # 1 + 2 = 3 + 2 = 5
    print(k)
print('Eng kichik butun son: ', k)


# 8 - masala
# While8. n natural soni berilgan (n > 0). Kvadrati n dan katta bo'lmagan eng katta butun k sonini
# (k darajasi 2 <= n) aniqlovchi programma tuzilsin. Ildizdan chigaruvchi funksiyadan foydalanmang.
n = int(input('N butun son kiriting: '))
k = 1
while k**2 <= n:
    k += 1
k -= 1
print('Eng katta butun son:', k)


# 9 - masala
# While9. n natural soni berilgan (n > 1). 3 darajasi k > n shartni ganoatlantiruvchi eng kichik butun k sonini
# aniqlovchi programma tuzilsin.
n = int(input('N butun son kiriting: '))
k = 1
while 3**k <= n:  # 12, 3**1,3**2
    print(k)
    k += 1 # 1, 2, 3
    # print(k)
print('Eng kichik son', k)


# 10 - masala
# While10. n natural soni berilgan (n > 1). 3 darajasi k <= n shartni qanoatiantiruvchi eng katta butun k sonini
# aniqlovchi programma tuzilsin.
n = int(input('N butun son kiriting: '))
k = 1
while 3 ** k <= n: # 5
    k += 1
k -= 1
print('Eng katta son', k)


# 11 - masala
# While11. n natural soni berilgan (n > 1). (1 + 2 + 3 + ... + k) >= n shart bajariladigan eng kichik k sonini
# aniqlovchi programma tuzilsin. 1 dan k gacha bo'lgan yig'indi ham ekranga chiqarilsin.
n = int(input('N butun son kiriting: '))
k = 1
s = 0
while s < n: # 12, 1,
    s += k # 1,3,
    print(s)
    k += 1 # 1,2,
    print(k)

    # print(k)
print('Eng kichik k soni:', k-1)
print('Yegindisi:', s)


# 12 - masala
# While12. n natural soni berilgan (n > 1). (1 + 2 + 3 + ... + k) <= n shart bajariladigan eng katta k sonini aniqlovchi programma tuzilsin.
# 1 dan k gacha bo'lgan yig'indi ham ekranga chigarilsin.

n = int(input('N butun son kiriting: '))
k = 1
s = 0
while s <= n:
    s += k
    k += 1
k -= 1
print(k)
print('Eng katta son:', k+1)
print('Yegindisi:', s)


# 13 - masala
# While13. a soni berilgan (a > 1). (1 + 1/2 + 1 / 3 + .. + 1 / k) >= a shart bajariladigan eng kichik k
# sonini aniqlovchi programma tuzilsin. Yig'indi ham ekranga chigarilsin
a = int(input('A butun son kiriting: '))
k = 1
s = 0
while s < a:
    s += 1 / k  # 0.5, 0.250
    print('BU s,', s)
    k += 1

print('Eng kichik k son:', k)
print('Yegindisi:', s)


# 14 - masala
# While14. a soni berilgan (a > 1). (1 + 1/2 + 1/3 + ... + 1 / k) <= a shart bajariladigan eng katta k sonini aniqlovchi programma tuzilsin.
# Yig indi ham ekranga chigarilsin.
a = int(input('A butun son kiriting: '))
k = 1
s = 0
while s < a:
    s += 1 / k  # 0.5,
    k += 1  # 2,
    if s > a:
        s -= 1 / k
        k -= 1
        break
print('Eng katta k son:', k)
print('Yegindisi:', s)


# 15 - masala
# While15. Bankka boshlang'ich S so'm qo'yildi. Har oyda bor bo'lgan summa p foizga oshadi (0 < p < 25 ).
# Necha oydan kevin boshlang'ich qiymat 2 martadan ko'p bo'lishini hisoblovchi programma tuzilsin.
# Necha oy k - butun son. Bankda hosil bo'lgan summa haqiqiy son ekranga chigarilsin.

S = float(input("Enter the initial amount (S): "))
p = float(input("Enter the monthly interest rate (p): "))

k = 0  # Counter for the number of months
summa_haqiqiy = S

while summa_haqiqiy <= 2 * S:
    print('haqiqiy:', summa_haqiqiy, '\n', 's-', S)
    summa_haqiqiy += summa_haqiqiy * (p / 100)
    print('summa-', summa_haqiqiy)
    k += 1

print("Necha oydan keyin summa 2 martadan ko'p bo'lgan:", k)
print("Bankda hosil bo'lgan summa:", summa_haqiqiy)


# 16 - masala
# While16. Sportsmen birinchi kuni 10 km yugirib boshladi.
# Keying kunlari bir oldingi kunga nisbatan p foiz ko'p yugurdi (0 < p < 50). Sportsmenning necha kundan keyin
# jami yugurgan masogasi 200 km dan oshadi?
# Jami kunlar soni va masofani (butun son) chigaruvchi programma tuzilsin.

m = 10
p = float(input('Kop yugurgan foizni kiriting (%): '))
jami = 200
kun = 0
while m < jami:
    m += m * (p / 100)
    kun += 1
print('Jami kunlar soni:',kun)
print('Jami masofa:', m)


# 17 - masala
# While17. n va m butun musbat sonlari berilgan (n > m).
# n sonini m soniga bo'lib butun va goldiq qismlarini bo' lish va goldigni olish amallarini ishlatmasdan topuvchi programma tuzilsin.

n = int(input('Butun N son kiriting: '))
m = int(input('Butun M son kiriting: '))
butun = n
qoldiq = 0
while butun >= m:
    butun -= m
    qoldiq += 1
print('Butun sonlar:', butun)
print('Qoldiq sonlar:', qoldiq)


# 18 - masala
# While18. n butun soni berilgan (n > 0).
# Bo'lib butun a qoldiq qismlarini aniqlash orqali, berilgan son raqamlarini teskari tartibda chiqaruvchi programma tuzilsin.

n = int(input('N butun son berilgan: ')) # 12
count = 0
while n > 0:
    s = n % 10 # 2
    # print(s)
    count = count * 10 + s  # 10 + 1.2 =
    print(count)
    n //= 10
print('Teskari tartibdagi sonlar:', n)

# 19 - masala
# While19. n butun soni berilgan (n > 0).
# Bo'lib butun va qoldiq qismlarini aniqlash orqali, berilgan son raqamlari yig'indisini va raqamlari sonini chiqaruvchi programma tuzilsin.

n = int(input('Butun son kiriting: '))
s = 0
while n > 0:
    d = n % 10 # 2
    s += d
    n //= 10
print('Yegindisi:', s)


# 20 - masala
# While20. n butun soni berilgan (n > 0).
# Bo'lib butun va qoldiq qismlarini aniqlash orqali, berilgan son raqamlarining orasida 2 raqami bor - yo'qligini aniqlovchi programma tuzilsin.

n = int(input('N butun son kiriting: '))
count = 0
two = False
while n > 0:
        d = n % 10  # 2
        if d == 2:
            two = True
        count += d
        n //= 10
if two:
    print('Ikki raqami bor')
else:
    print('Ikki raqama yoq')



# 21 - masala
# While21. n butun soni berilgan (n > 0).
# Bo'lib butun va qoldiq qismlarini aniqlash orqali, berilgan son raqamlarining orasida toq raqamlar bor - yo'qligini aniglovchi programma tuzilsin.
n = int(input('N butun son kiriting: '))
count = 0
toq = False
while n > 0:
        d = n % 10  # 2
        print(d)
        if d % 2 != 0:
            toq = True
            print(toq)
            break
        n //= 10
if toq:
    print('Toq')
else:
    print('Juft')



# 22 - masala
# While22. n butun soni berilgan (n > 1). N sonini tub yoki tub emasligini aniqlovchi programma tuzilsin.

n = int(input('N butun son kiriting: '))
tub = True
m = 2
while m <= n // 2:
    if n % m == 0:
        tub = False
        break
    m += 1
if tub:
    print('Tub son', n)
else:
    print('Tub son emas', n)



# 23 - masala
# While23. a va b butun musbat sonari berilgan.
# Berilgan sonlarning eng katta umumiy bo'luvchisini aniqlovchi programma tuzilsin.

a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

max_boluvchisi = 0

while a > 0 and b > 0:
    if a > b:
        a = a % b
        print('bu a', a)
    else:
        b = b % a
        print('bu b', b)

max_boluvchisi = a + b
print(max_boluvchisi)

print("Eng katta umumiy bo'luvchi:", max_boluvchisi)


# 24 - masala
# While24. n butun soni berilgan (n > 1). n sonini Fibonachchi sonlari orasida bor - yo'qligini aniqlovchi
# programma tuzilsin. Fibonachchi sonlari quyidagi qonuniyat asosida topiladi.
# F1 = 1; F2 = 1; Fk = F.k-1 + F.k-2; k = 3,4;

n = int(input('N butun son: '))
F1 = 1
F2 = 1
k = 0
while F1 <= n:
    if F1 == n:
        print(F1, 'F1 n ga teng boldi')
        print('n soni Fibonachi orasida mavjud! ')
        break
    f_next = F2 + F1
    print(f_next, 'f_next')
    F1, F2 = F2, f_next
    print(F1, 'F1')
    print(F2, 'F2')
else:
    print("n soni Fibonachi orasida mavjud emas!")



# 25 - masala
# While25. n butun soni berilgan (n > 1). n sonidan katta bo'lgan birinchi Fibonachchi sonini aniqlovchi
# programma tuzilsin. Fibonachchi sonlari while24 masalasida berilgan
n = int(input('N butun son: '))
F1 = 1
F2 = 1
F_x = F1 + F2
print('F_x 1,', F_x)
while F_x <= n:
    F1 = F2
    print('F1', F1)
    F2 = F_x
    print('F2', F2)
    F_x = F1 + F2
    print('F_X 2,', F_x)
print('Eng kattasi fibonachini:', F_x)


# 26 - masala
# While26. Fibonachchi soni bo'lgan n butun soni berilgan (n > 1). (Fibonachchi sonlari while24
# masalasida berilgan.) n sonidan bir oldingi va bir keyingi Fibonachchi sonlarini chiqaruvchi programma
# tuzilsin.

n = int(input('N butun son kiriting: '))
F1, F2 = 1, 1
while F2 <= n:
    if F2 == n:
        print("n soni Fibonachchi sonlari orasida mavjud.")
        previous_F1 = F1
        print('Previous_F1', F1)
        next_F = F1 + F2
        print('next_F', next_F)
        print("Bir oldingi Fibonachchi son:", previous_F1)
        print("Bir keyingi Fibonachchi son:", next_F)
        break
    fibonacci_next = F1 + F2
    print('fibonachi_next', fibonacci_next)
    F1, F2 = F2, fibonacci_next
    print('F1', F1)
    print('F2', F2)
else:
    print("n soni Fibonachchi sonlari orasida yo'q.")



# 27 - masala
# While27. Fibonachchi soni bo'lgan n butun soni berilgan (n > 1). ( Fibonachchi sonlari while24
# masalasida berilgan.) n soni Fibonachchi ketma - ketligining nechanchi xadi ekanini chiqaruvchi
# programma tuzilsin.

n = int(input("n sonini kiriting: "))

F_1 = 1
F_2 = 1
count = 2  # Ketma-ketlikning xadlar soni

while F_2 < n:
    F_next = F_1 + F_2
    print('F_next', F_next)
    F_1, F_2 = F_2, F_next
    print('F1,', F_1, '\n', 'F2,', F_2)
    count += 1  # Xadlar soni oshirish
    print('Count', count)

if F_2 == n:
    print("n soni Fibonachchi ketma-ketligining", count, "xadi elementi.")
    print('F_2_2', F_2)
else:
    print("Berilgan son Fibonachchi ketma-ketligida yo'q.")


# 28 - masala
# While28. e haqiqiy musbat soni berilgan. Ketma - ketlik xadlari quyidagicha aniqlanadi:
# a1=2, ak= 2+1/a.k-1; k = 2,3, ;
# |a.k - a.k-1| < e shartni qanoatlantiruvchi eng kichik k sonini aniqlovchi programma tuzilsin.
# a.k va a.k - 1 ham ekranga chiqarilsin.

e = float(input("e ni kiriting: "))

a_1 = 2
a_k_1 = 2 + 1 / a_1

k = 2

while abs(a_1 - a_k_1) >= e:
    print("a_k:", a_1)
    print("a_k_minus_1:", a_k_1)

    a_k_1 = a_1
    a_k = 2 + 1 / a_k_1

    k += 1

print("Eng kichik k:", k)
print("ak:", a_1)
print("a.k-1:", a_k_1)


# 29 - masala
# While29. e haqiqiv musbat soni berilgan. Ketma - ketlik xadlari quyidagicha aniqlanadi:
# a1=1; a2=2; ak = (a.k -2 + 2 * a.k-1)/3; k = 3,4,...
# |a1 - a.k-1| < e shartni qanoatlantiruvchi eng kichik k sonini aniqlovchi programma tuzilsin.
# a.k va a.k - 1 ham ekranga chiqarilsin.

e = float(input('E haqiqiy son kiriting: '))
a1, a2 = 1, 2
# ak = (a2 + 2 * a1) / 3
k = 3

while abs(a2 - a1) >= e:
    a_next = (a1 - 2 * a2) / 3

    a1 = a2
    a2 = a_next

    k += 1

print(f"a{k-1} = {a1}, a{k} = {a2}")
print(f"Eng kichik k soni: {k-1}")


# 30 - masala
# While30. A, B, C musbat butun sonlari berilgan. A x B to'rtburchak ichida tomoni C bo'lgan kvadratdan
# nechtasi sig'ishini aniqlovchi programma tuzilsin. Ko'paytirish va bo'lish amallarini ishlatmang.

A, B, C = int(input('A musbat son kiriting: ')), int(input('B musbat son kiriting: ')), int(input('C musbat son kiriting: '))
count = 0
while A >= C and B >= C:
    A -= C
    print('A', A)
    B -= C
    print('B', B)
    count += 1
    print('Count', count)
print('C ni sigishini kvadrati:', count)