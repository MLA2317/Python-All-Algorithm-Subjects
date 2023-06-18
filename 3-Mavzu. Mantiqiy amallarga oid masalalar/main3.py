# 1 - masala
# Boolean1. A butun soni berilgan. Jumlani rostlikka tekshiring: "A soni musbat'.

A = int(input('A sonni kiriting >> '))
if A > 0:
    print('A soni musbat')
else:
    print('A soni manfiy')

#  2 - masala
# Boolean2. A butun soni berilgan. Jumlani rostlikka tekshiring: "A soni toq son*

A = int(input('A sonni kiriting >> '))
if A % 2 != 0:
    print('A toq son', A)
else:
    print('A juft son', A)


# 3 - masala
# Boolean3, A butun soni berilgan. Jumlani rostlikka tekshiring: "A soni juft son*.

A = int(input('A sonni kiriting >> '))
if A % 2 == 0:
    print('A juft son', A)
else:
    print('A toq son', A)

# Boolean4. Ikkita butun A va B sonlari berilgan. Jumlani rostlikka tekshiring: 'A>2 va B<=3*.
# 4 - masala
A = int(input('A sonni kiriting >> '))
B = int(input('B sonni kiriting >> '))
if A > 2 and B <= 3:
    print('Rost')
else:
    print('Yolgon')


# Boolean5, Ikkita butun A va B sonlari berilgan. Jumlani rostlikka tekshiring:
# "A >= 0 voki B < -2
# 5 - masala
A = int(input('A sonni kiriting >> '))
B = int(input('B sonni kiriting >> '))
if A >= 0 and B < -2:
    print('Rost')
else:
    print('Yolgon')

# Booalean6. Uchta A, B, C butun sonlar berilgan. Jumlani rostlikka tekshiring:
# "A<= B <= C"
# 6 - masala
A = int(input('A sonni kiriting >> '))
B = int(input('B sonni kiriting >> '))
C = int(input('C sonni kiriting >> '))
if A <= B <= C:
    print('Rost')
else:
    print('Yolgon')

# Booalean7. Uchta A, B, C butun sonlar berilgan. Jumlani rostlikka tekshiring: "B soni A va C sonlari
# orasida yotadi.
# 7 - masala
A = int(input('A sonni kiriting >> '))
B = int(input('B sonni kiriting >> '))
C = int(input('C sonni kiriting >> '))
if B > A and B < C or B < A and C < B:
    print('Orasida yotadi')
else:
    print('Orasida yotmaydi')

# Boolean8. Ikkita butun A va B sonlari berilgan. Jumlani rostikka tekshiring: "A va B sonlari toq sonlar".
# 8 - masala
A = int(input('A sonni kiriting >> '))
B = int(input('B sonni kiriting >> '))
if A % 2 != 0 and B % 2 != 0:
    print('A va B sonlar Toq son')
else:
    print('Juft son')


# Boolean9. Ikkita butun A va B sonlari berilgan. Jumlani rostlikka tekshiring: "A va B sonlaring hech
# bo 'imaganda bittasi toq son'.
# 9 - masala
A = int(input('A sonni kiriting >> '))
B = int(input('B sonni kiriting >> '))
if A % 2 != 0 or B % 2 != 0 and A % 2 == 0 or B % 2 == 0:
    print('A va B sonlar orasida hech bolmagandan bittasi toq son')
else:
    print('Juft son')

# Boolean10. Ikkita butun A va B sonlari berilgan. Jumlani rostikka tekshiring: "A va B sonlarning faqat
# bittasi toq son".
# 10 - masala
A = int(input('A sonni kiriting >> '))
B = int(input('B sonni kiriting >> '))
if (A % 2 != 0 or B % 2 != 0) and (A % 2 == 0 or B % 2 == 0):
    print('A va B sonlarning faqat bittasi toq son')
else:
    print('Juft son')

# Boolean11. Ikkita butun A va B sonlari berilgan. Jumlani rostlikka tekshiring: "A va B sonlarining har
# ikkalasi ham yoki toq son yoki juft son'.
# 11 - masala
A = int(input('A sonni kiriting >> '))
B = int(input('B sonni kiriting >> '))
if A % 2 != 0 and B % 2 != 0 or A % 2 == 0 and B % 2 == 0:
    print('A va B sonlarning har ikkilasi ham yoki toq son yoki juft son')
else:
    print('Bilmadim')

# Boolean12. Uchta A, B, C butun sonlar berilgan. Jumlani rostlikka tekshiring: "A, B, C sonlarning har
# biri musbat".
# 12 - masala
A = int(input('A sonni kiriting: '))
B = int(input('B sonni kiritnig: '))
C = int(input('C sonni kiriting: '))
if  A > 0 and B > 0 and C > 0:
    print('A B C ni har biri musbat')
else:
    print('manfiy')


# Boolean13.Uchta A. B. C butun sonlar berilgan. Jumlani rostikka tekshiring: "A, B, C sonlaming hech
# bo'lmaganda bittasi musbat".
# 13 - masala
A = int(input('A sonni kiriting: '))
B = int(input('B sonni kiritnig: '))
C = int(input('C sonni kiriting: '))
if A > 0 or B > 0 or C > 0:
    print('A B C ni sonlarning hech bolmaganda bittasi musbat')
else:
    print('Manfiy')

# Boolean14.Uchta A, B, C butun sonlar berilgan. Jumlani rostlikka tekshiring: "A, B, C sonlaridan faqat
# bittasi musbat son*.
# 14 - masala
A = int(input('A sonni kiriting: '))
B = int(input('B sonni kiritnig: '))
C = int(input('C sonni kiriting: '))
if (A > 0 and B <= 0 and C <= 0) or (A <= 0 and B > 0 and C <= 0) or (A <= 0 and B <=0 and C > 0):
    print('A B C ni sonlarning faqat bittasi musbat son')
else:
    print('Manfiy')

# Boolean15. Uchta A, B, C butun sonlar berilgan. Jumlani rostlikka tekshiring: "A, B, C sonlardan fagat
# ikkitasi musbat son".
# 15 - masala
A = int(input('A sonni kiriting: '))
B = int(input('B sonni kiritnig: '))
C = int(input('C sonni kiriting: '))
if (A > 0 and B > 0 and C <= 0) or (A > 0 and B <= 0 and C > 0) or (A <= 0 and B > 0 and C > 0):
    print('A B C ni sonlarning faqat ikkita musbat son')
else:
    print('Manfiy')

# Boolean16. Musbat butun son berilgan. Jumlani rostikka tekshiring: "Berilgan son ikki xonali juft son".
# 16 - masala
n = int(input('N sonni kiriting >> '))
if n > 9 and n < 100 and n % 2 == 0:
    print('Berilgan son ikki honali juft son')
else:
    print('Bir honali yoki uch honali son va toq son kiritdingiz')


# Boolean17. Musbat butun son berilgan. Jumlani rostikka tekshiring: "Berilgan son uch xonali tog"
# 17 - masala
n = int(input('N sonni kiriting >> '))
if n > 1 and n > 10 and n < 999 and n % 2 != 0:
    print('Berilgan son uch honali toq son')
else:
    print('Bir honali yoki on honali son va juft son kiritdingiz')

# Boolean18. Jumlani rostikka tekshiring: "Berilgan uchta butun sonlaring hech bo'lmaganda 2 tasi bir
# biriga teng*.
# 18 - masala
A = int(input('A sonni kiriting: '))
B = int(input('B sonni kiritnig: '))
C = int(input('C sonni kiriting: '))

if (A == B and B != C) or (A == C and C != B) or (B == C and B != A and C != A):
    print('A B C hech bolmaganda ikkitasi bir biriga teng')
else:
    print('teng emas')

# Boolean19. Jumlani rostlikka tekshiring: "Berilgan uchta butun sonlarning hech bo'imaganda bir jufti
# o'zaro garama-qarshi".
# 19 - masala
A = int(input('A sonni kiriting: '))
B = int(input('B sonni kiritnig: '))
C = int(input('C sonni kiriting: '))
if (A % 2 == 0 and B % 2 != 0 and C % 2 != 0) or (A % 2 != 0 and B % 2 == 0 and C % 2 != 0) or (A % 2 != 0 and B % 2 != 0 and C % 2 == 0):
    print('Bir jufti ozaro qarama qarshi')
else:
    print('Toqlari')

# Boolean20. Uch xonali son berilgan. Jumlani rostikka tekshiring: "Ushbu sonning barcha ragamlari xar xil
# 20 - masala
# a = int(input('Uch xonali son kiriting: '))
digit1 = a // 100
digit2 = (a // 10) % 10
digit3 = a % 10
print(digit1, digit2, digit3)
if digit1 != digit2 and digit1 != digit3 and digit2 != digit3:
    print('Barcha raqamlar xar xil')
else:
    print('Barchasi bir hil')

# Boolean21. Uch xonali son berilgan. Jumlani rostikka tekshiring: "Ushbu sonning ragamlari ketama-
# ket o'suvchi bo'lib joylashgan"
# 21 - masala
a = int(input('Uch xonali son kiriting: '))
digit1 = a // 100
digit2 = (a // 10) % 10
digit3 = a % 10
print(digit1, digit2, digit3)
if digit1 < digit2 and digit1 < digit3 and digit2 < digit3:
    print('Barcha raqamlar Ketma ket osuvchi bolib joylashgan')
else:
    print('Barchasi bir hil')

# Boolean22. Uch xonali son berilgan. Jumlani rostikka tekshiring: "Ushbu sonning raqamlari ketama-
# ket o'suvchi bo'lib joylashgan yoki kamayuvchi ketma-ketlikka ega*
# 22 - masala
a = int(input('Uch xonali son kiriting: '))
digit1 = a // 100
digit2 = (a // 10) % 10
digit3 = a % 10
if (digit1 < digit2 and digit1 < digit3 and digit2 < digit3) or (digit1 > digit2 and digit1 > digit3 and digit2 > digit3):
    print('Barcha raqamlar Ketma ket osuvchi bolib yoki kamayuvchi bolib joylashgan')
else:
    print('Barchasi bir hil')


# Boolean23. Uch xonali son berilgan. Jumlani rostlikka tekshiring: "Ushbu sonni chapdan o'qiganda
# ham, o'ngdan o'qiganda ham bir xil".
# 23 - masala
a = int(input('Uch xonali son kiriting: '))
digit1 = a // 100
digit2 = (a // 10) % 10
digit3 = a % 10
if digit1 == digit3:
    print('Chapdan oqiganda va ongdan oqiganda ham bir hil')
else:
    print('Birhil emas')

# Boolean24. A. B. C sonlar beilgan (A soni noldan farqli). D=B kvadrat - 4*A*C diskerminantdan foydalanib,
# jumlani rostlikka tekshiring: "Ax kvadrat+ Bx+C=0 kvadrat tenglama haqiqiy ildizga ega".
# 24 - masala
A, B, C = int(input('A ni kiriting:')), int(input('B ni kiriting:')), int(input('C ni kiriting:'))

D = pow(B, 2) - 4 * A * C
if D >= 0:
    print('Kvadrat tenglama ildizi:', D)
else:
    print('Kvadrat tenglama ildizi emas')


# Boolean25. x, y sonlar berilgan. Jumlani rostlikka tekshiring: "Koordinatalari (x,y) bo'lgan nugta,
# koordinata choragining ikkinchisida yotadi".
# 25 - masala
x, y = int(input('X ni kiriting: ')), int(input('Y ni kiriting: '))
if x < 0 and y > 0:
    print('Koordinata x y choragiga ikkinchiga yotadi.', )
else:
    print('Koordinata x y choragiga ikkinchiga yotmaydi.')


# Boolean26. x, y sonlar berilgan. Jumlani rostlikka tekshiring: "Koordinatalri (x,y) bo'lgan nuqta
# koordinata choragining to'rtinchisida yotadi".
# 26 - masala
x, y = float(input('X ni kiriting: ')), float(input('Y ni kiriting: '))
if x > 0 and y < 0:
    print('Koordinata x y choragiga tortinchisiga yotadi.')
else:
    print('Koordinata x y choragiga tortinchisiga yotmaydi: ')


# Boolean27. x, y sonlar berilgan. Jumlani rostlikka tekshiring: "Koordinatalri (x,y) bo'lgan nuqta
# koordinata choragining ikkinchisida yoki uchunchisida yotadi".
# 27 - masala
x, y = int(input('X ni kiriting: ')), int(input('Y ni kiriting: '))
if x < 0 and y > 0  or x < 0 and y < 0:
    print('Koordinata x y choragiga ikkinchi yoki uchinchisiga yotadi.')
else:
    print('Koordinata x y  choragiga ikkinchi yoki uchinsiga yotmaydi.')


# Boolean28. x, y sonlar berilgan. Jumlani rostlikka tekshiring: "Koordinatalri (x,y) bo'lgan nuqta
# koordinata choragining birinchi yoki uchunchisida yotadi"
# 28 - masala
x, y = int(input('X ni kiriting: ')), int(input('Y ni kiriting: '))
if x > 0 and y > 0  or x < 0 and y < 0:
    print('Koordinata x y choragiga birinchi yoki uchinchisiga yotadi.')
else:
    print('Koordinata x y choragiga birinchi yoki uchinsiga yotmaydi.')


# Boolean29. (x, y), (x1, y1), (x2, y2) sonlari berilgan. Jumlani rostikka tekshiring: "Koordinatalari (x,y)
# bo'lgan nuqta, chap yuqori cho'qgisi (x1,y1) koordinatalarga ega bo'lgan va o'ng pastikisi (×2,y2)
# bo'lgan, tomonlari esa koordinata o'qlariga parallel bo'lgan to'rtburchak ichida yotadi'.
# 29 - masala
x = int(input('x ni kiriting: '))
y = int(input('y ni kiriting: '))
x1 = int(input('x1 ni kiriting: '))
y1 = int(input('y1 ni kiriting: '))
x2 = int(input('x2 ni kiriting: '))
y2 = int(input('y2 ni kiriting: '))

parallel = (y2 - y1) * (x - x1) == (x2 - x1) * (y - y1)

if parallel:
    print('Koordinatalar (x,y) bolgan nuqta, chap yuqori choqisi (x1,y1) koordinatalatga ega bolgan\n'
          'ong pastikisi (x2,y2) bolgan')
else:
    print('Koordinatalarga (x,y) ega emas')


# Boolean30. a, b, c butun sonlari berilgan. Jumlani rostikka tekshiring: "a, b, c tomonli uchburchak teng
# tomonli bo'ladi".
# 30 - masala
a, b, c = int(input('a ni kiritng: ')), int(input('b ni kiting: ')), int(input('c ni kiriting: '))
if a == b == c:
    print('a, b, c teng tomonli uchburchak boldi')
else:
    print('a,b,c teng tomonli uchburchak emas')

# Boolean31. a, b, c butun sonlari berilgan. Jumlani rostikka tekshiring: *a, b, c tomonli uchburchak teng
# yonli bo'ladi".
# 31 - masala
a, b, c = int(input('a ni kiritng: ')), int(input('b ni kiting: ')), int(input('c ni kiriting: '))
if a == b == c:
    S = a * b * c
    print('a,b,c teng yonli uchburchak boldi', S)
else:
    print('a,b,c teng yonli uchburchak emas')

# Boolean32. a, b, c butun sonlar berilgan. Jumlani rostlikka tekshiring: "a, b, c tomonli uchburchak to'g'ri burchakli".
# 32 - masala
a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))
c = int(input("c ni kiriting: "))

if a > 0 and b > 0 and c > 0:
    if a + b > c and b + c > a and c + a > b:
        a1 = (pow(b, 2) + pow(c, 2) - pow(a, 2)) / (2 * b * c)
        b1 = (pow(c, 2) + pow(a, 2) - pow(b, 2)) / (2 * c * a)
        c1 = (pow(a, 2) + pow(b, 2) - pow(c, 2)) / (2 * a * b)
        print(a1)
        print(b1)
        print(c1)

        if a1 > 0 and b1 > 0 and c1 > 0:
            print("a, b, c tomonli uchburchak to'g'ri burchakli.")
        else:
            print("a, b, c tomonli uchburchak to'g'ri burchakli emas.")
    else:
        print("a, b, c tomonli uchburchak emas.")
else:
    print("a, b, c musbat emas.")

# Boolean33. a, b, c butun sonlar berilgan. Jumlani rostlikka tekshiring: "a, b, c tomonli uchburchak
# yasash mumkin'
# 33 - masala
a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))
c = int(input("c ni kiriting: "))
if a + b > c and a + c > b and b + c > a:
    S1 = a + b
    S2 = a + c
    S3 = b + c
    print(S1,'> c', S2,'> b', S3,'> a')
    print('Uchburchak yasash mumkin')
else:
    print('Uchburchak yasash mumkin emas')

# Boolean34. Shaxmat doskasining x, y koordinatalari berilgan (1-8 oraliqda yotuvchi butun sonlar).
# Doskaning chap pastki maydoni (1,1) qoraligini hisobga olib, jumlani rostlikka tekshiring: "Berilgan (x,
# y) maydon oq.
# 34 - masala
print('1 - 8 gacha butun son kiriting')
x, y = int(input('X ni kiriting: ')), int(input('Y ni kiriting: '))
if (x + y) % 2 == 0:
    print('Berilgan x,y maydoni oq')
else:
    print('Berilgan x,y maydoni qora')

# Boolean35. Shaxmat doskasining ikkita turli (x1, y1), (x2, y2) koordinalari berilgan (1-8 oraliqda
# yotuvchi butun sonlar). Jumlani rostlikka tekshiring: "Berilgan maydonlar bir xil rangda".
# 35-masala
print('1 - 8 gacha butun son kiriting')
x1 = int(input('X1 ni kiriting: '))
y1 = int(input('Y1 ni kiriting: '))
x2 = int(input('X2 ni kiriting: '))
y2 = int(input('Y2 ni kiriting: '))
if (x1 + y1) % 2 == 0 and (x2 + y2) % 2 == 0:
    print('Berilgan maydonlar bir hil rangda')
else:
    print('Berilgan maydonlar bir hil rangda emas')

# Boolean36. Shamat doskasining ikkita turli (x1, y1), (x2, y2) koordinalari berilgan (1-8 oraliqda
# yotuchi butun sonlar). Jumlani rostlikka tekshiring: "Ruh bir yurishda bir maydondan ikkinchisiga o'ta
# oladi
# 36 - masala
print('1-8 gacha butun son kiriting')
x1 = int(input('X1 ni kiriting: '))
y1 = int(input('Y1 ni kiriting: '))
x2 = int(input('X2 ni kiriting: '))
y2 = int(input('Y2 ni kiriting: '))
if abs(x1 - y1) == abs(x2 - y2):
    print('Ruh bir yurishda bir maydandan ikkinchisiga ota oladi')
else:
    print('Ruh bir yurishda bir maydandan ikkinchisiga ota olmaydi')


# Boolean37. Shaxmat doskasining ikkita turli (x1, y1), (x2, y2) koordinalari berilgan (1-8 oraliqda
# yotuvchi butun sonlar). Jumlani rostlikka tekshiring: "Shoh bir yurishda bir maydondan ikkinchisiga o'ta
# oladi."
# 37 - masala
print('1-8 gacha butun son kiriting')
x1 = int(input('X1 ni kiriting: ')) # 4 - True, 1 - False,
y1 = int(input('Y1 ni kiriting: ')) # 4 - True, 1 - False,
x2 = int(input('X2 ni kiriting: ')) # 3 - True, 1 - False,
y2 = int(input('Y2 ni kiriting: ')) # 3 - True, 8 - False,
if abs(x1 - y1) <= 1 and abs(x2 - y2) <= 1:
    print('Shoh bir yurishda bir maydondan ikkinchisiga ota oladi')
else:
    print('Shoh bir yurishda bir maydondan ikkinchisiga ota olmaydi')


# Boolean38. Shaxmat doskasining ikkita turli (×1, y1), (×2, y2) koordinalan berilgan (1-8 oraliqda
# yotuvchi butun sonlar). Jumlani rostlikka tekshiring: "Fil bir vurishda bir maydondan ikkinchisiga o'ta
# oladi".
# 38 - masala
print('1-8 gacha butun son kiriting')
x1 = int(input('X1 ni kiriting: ')) # 4 - True,  4 - False
y1 = int(input('Y1 ni kiriting: ')) # 4 - True,  4 - False
x2 = int(input('X2 ni kiriting: ')) # 3 - True,  5 - False
y2 = int(input('Y2 ni kiriting: ')) # 3 - True,  4 - False
if abs(x1 - x2) and abs(y1 - y2) or x1 == x2 and y1 == y2:
    print('Fil bir yurishda bir maydondan ikkinchisiga ota oladi')
else:
    print('Fil bir yurishda bir maydondan ikkinchisiga ota olmaydi')


# Boolean39. Shaxmat doskasining ikkita turli (x1, y1), (x2, y2) koordinalari berilgan (1-8 oraliqda
# yotuvchi butun sonlar). Jumlani rostlikka tekshiring: "Farzin bir yurishda bir maydondan ikkinchisiga o'ta
# oladi".
# 39 - masala
print('1-8 gacha butun son kiriting')
x1 = int(input('X1 ni kiriting: ')) # 3 true,  5 False
y1 = int(input('Y1 ni kiriting: ')) # 3 true,  6 False
x2 = int(input('X2 ni kiriting: ')) # 1 true,  3 False
y2 = int(input('Y2 ni kiriting: ')) # 1 true,  3 False

d1 = abs(x2 - x1)
d2 = abs(y2 - y1)

if d1 == 1 or d2 == 2 and d1 == 2 or d2 == 1:
    print('Farzin bir yurishda birinchi maydondan ikkinchiga ota oladi')
else:
    print('Farzin bir yurishda birinchi maydondan ikkinchiga ota olmaydi')


# Boolean40. Shaxmat doskasining ikkita turli (x1, y1), (x2, y2) koordinalari berilgan (1-8 oraliqda
# yotuvchi butun sonlar). Jumlani rostlikka tekshiring: "Ot bir yurishda bir maydondan ikkinchisiga o'ta
# oladi.
# 40 - masala
print("1-8 gacha butun son kiriting")
x1 = int(input('X1 ni kiriting: '))  # 5 true,  2 False
y1 = int(input('Y1 ni kiriting: '))  # 2 true,  8 False
x2 = int(input('X2 ni kiriting: '))  # 4 true,  3 False
y2 = int(input('Y2 ni kiriting: '))  # 4 true,  7 False

h1 = abs(x2 - x1)
h2 = abs(y2 - y1)

if (h1 == 1 and h2 == 2) or (h1 == 2 and h2 == 1):
    print('Ot bir yurishda birinchi maydondan ikkinchiga ota oladi')
else:
    print('Ot bir yurishdan birinchi maydondan ikkinchiga ota olmaydi')