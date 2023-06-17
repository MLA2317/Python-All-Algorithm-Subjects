
# 1 masala c++
# Begin1. Kvadratning tomoni a berilgan. Uning perimetri aniqlansin. P=4*a
# length = float(input('Kvadratning tomon uzunligini kiriting --> '))
# if length > 0:
#     perimetr = length * 4
#     print('Perimetri:', perimetr)
# else:
#     print("Tomon uzunligi musbat bo'lishi kerak")

# 2 masala c++
# Begin2. Kvadratning tomoni a berilgan. Uning yuzasini aniqlansin
# a = int(input('Kvadratning tomon yuzasi kiriting >> '))
# if a > 0:
#     area = a ** 2
#     print('Yuzasi:', area)
# else:
#     print('Tomon uzunligi musbat bolishi kerak')

# 3 masala c++
# Begin3. To'g'ri to'rtburchakning tomonlari a va b berilgan. Uning yuzasi S = a * b va  P = 2 * (a + b) perimetri aniqlansin.
# a = int(input())
# b = int(input())
# if a > 0 and b > 0:
#     s = a * b
#     p = 2 * (a + b)
#     print('Yuzasi:', s)
#     print('Perimetri:', p)
# else:
#     print('Musbat bolishi kerak')
#

# 4 masala c++
# Begin 4. Aylananing diametri d berilgan. Uning uzunligi aniqlansin L = p * d, p = 3.14
# d = int(input('Aylananing diametrni kiriting >> '))
# if d > 0:
#     p = 3.14
#     L = d * p
#     print('Uzunligi:', L)
# else:
#     print('Diametr musbat bolishi kerak')

# 5 masala c++
# Begin 5. Kubning  yon tomoni a berilgan. Uning hajmini V = a ni kubi va to'la sirti S=6 * a ni kvadrati aniqlansin
# k = int(input('Kubning yon tomonini kiriting >> '))
# if k > 0:
#     V = k ** 3
#     S = 6 * k ** 2
#     print('Hajmi:', V)
#     print('Tola Sirti:', S)
# else:
#     print('Kub musbat son bolishi kerak')

# 6 masala c++
# Begin 6. Parallelepedning tomonlari a, b ,c  berilgan. Uning hajmi V = a * b *c va tola  sirti s = 2 * (a * b + b * c + a * c) aniqlansin
# a = int(input('Parralelepedning tomonini 1 chisi kiriting >> '))
# b = int(input('Parralelepedning tomonini 2 chisi kiriting >> '))
# c = int(input('Parralelepedning tomonini 3 chisi kiriting >> '))
# if a > 0 and b > 0 and c > 0:
#     V = a * b * c
#     S = 2 * (a * b + b * c + a * c)
#     print('Hajmi:', V)
#     print('Tola sirti:', S)
# else:
#     print('Parraleleped musbat bolishi kerak')


# 7 masala c++
# Begin7. Doiraning radiuse R berilgan. Uning uzunligi L va yuzasi S aniqlansin  L = 2 * p * r, s = p * r**2
# r = int(input('Doirani rasiusini kiriting >> '))
# if r > 0:
#     p = 3.14
#     L = 2 * p * r
#     S = p * r**2
#     print('Uzunligi:', L)
#     print('Yuzasi:', S)
# else:
#     print("Doira musbat bolish kerak")

# 8 masala c++
# Begin8. Ikkita son a va b berilgan. Ularning orta arifmetikasi aniqlansin (a+b) / 2
# a = int(input('son kiriting >> '))
# b = int(input('son kiriting >> '))
# if a > 0 and b > 0:
#     c = (a + b) / 2
#     print('Orta arifmetika:', c)
# else:
#     print('Musbat bolish kerak')

# 9 masala c ++
# Begin9. Ikkita manfiy bolmagan son a va b berilgan. Ularning o'rta geometriyasi aniqlansin  ildizda a*b
# import math
#
# a = float(input("a ni kiriting: "))
# b = float(input("b ni kiriting: "))
#
# if a >= 0 and b >= 0:
#     agm = math.sqrt(a * b)
#     print("O'rta geometriya:", agm)
# else:
#     print("Xato: Sonlar manfiy bo'lishi kerak emas.")

# 10 masala c ++
# Begin10. Nolga teng bolmagan ikkita son berilgan. Ularning yigindisi, kopaytmasi va far birini kvadrati aniqlansin
# a = int(input('a ni kiritng:'))
# b = int(input('b ni kiritng:'))
# if a > 0 and b > 0:
#     c = a + b
#     v = a * b
#     k = a**2, b**2
#     print('Yegindisi:', c)
#     print('Kopaytmasi:', v)
#     print('Kvadrati:', k)
# else:
#     print('Nolga teng son kiritingiz')

# 11 masala c ++
# Begin11. Nolga teng bo'lmagan ikkita son berilgan. Ularning yeg'indisi ko'paytmasini va har biriniing moduli aniqlansin
# a = int(input('a ni kiriting >> '))
# b = int(input('b ni kiriting >> '))
# if a > 0 and b > 0:
#     sum = a + b
#     k = a * b
#     modul_a = abs(a) # modul
#     modul_b = abs(b)
#     print('Yegindisi:', sum)
#     print('Kopaytmasi:', k)
#     print('Mudul A:', modul_a)
#     print('Modul B:', modul_b)
# else:
#     print('Manfiy son bolish kerak')

# 12 masala c++
# Begin12. Tog'ri uchburchakning katetlari a va b berilgan. Uning gipotenuzasi c va perimetri P aniqlansin c = ildizni ichida a kvadrat + b kvadrat, P = a + b + c
# import math
# a = int(input('a ni kiritng >> '))
# b = int(input('b ni kiriting >> '))
# if a > 0 and b > 0:
#     c = math.sqrt(a**2 * b**2)
#     P = a + b + c
#     print('Gipotenuzasi:', c)
#     print('Perimetri:', P)
# else:
#     print('Musbat bolishi kerak')

# 13 masala c++
# Begin13. Umumiy markazda bo'lgan ikkita aylana radiusi berilgan R1=R2=(R1>R2) Ularning yuzalari S1 va S2 ularning ayirmasi S3 aniqlansin
# S1 = p  * R1, S2 = p * R2, S3 = p * (R1 - R2)

# r1 = int(input('r1 ni kiriting >> '))
# r2 = int(input('r2 ni kiriting >> '))
# if r1 > 0 and r2 > 0:
#     p = 3.14
#     # r1 = r2 = (r1 > r2)
#     S1 = p * r1
#     S2 = p * r2
#     S3 = p * (r1 - r2)
#     print('Yuzasi S1:', S1)
#     print('Yuzasi S2:', S2)
#     print('Ayirmasi S3:', S3)
# else:
#     print('Musbat bolishi kerak')

# 14 masala c++
# Begin14. Aylananing uzunligi L berilgan. Uning radiusi R va Yuzasi S aniqlansin  L = 2 * p * R, S = p * R kvadrat, p = 3.14
# r = int(input('r sonni kiriitng >> '))
# if r > 0:
#     p = 3.14
#     L = 2 * p * r
#     S = p * r**2
#     print('Uzunligi L:', L)
#     print('Yuzasi S:', S)
# else:
#     print('Musbat bolish kerak')
#
# 15 masala c ++
# begin15. Aylananing yuzasi S berilgan. Uning diametrini d va R aniqlansin L = 2 * p * R, S = p * R kvadrati, p=3.14
# s = int(input('Aylaning uzunligini kiriting >> '))
# p = 3.14
# R = p * s**2
# d = 2 * R
# L = 2 * p * R
# print('Radiusi:', R)
# print('Diametr:', d)
# print('Aylananing uzunligi:', L)

# 16 masala c ++ True
# Begin16. Sonlar oqida ikkita nuqta orasidagi masofa aniqlansin |x2 - x1|
# x1 = float(input('x1 ni kiriting >> '))
# x2 = float(input('x2 ni kiriting >> '))
#
# distance = abs(x2 - x1)
# print('Nuqta orasidagi masofa:', distance)

# 17 masala c ++ True
# Begin17. Sonlar o’qida A, B, C nuqtalar berilgan. AC va BC kesmalarning uzunligini va kesmalar uzunligining yeg’indisini topuvchi programma tuzilsin
# A = int(input('A ni kiriting >> '))
# B = int(input('B ni kiriting >> '))
# C = int(input('C ni kiriitng >> '))
#
# AC = abs(A - C) # abs musbat qiymatga aylantiradi
# BC = abs(B - C)
# D = AC + BC
# print('Kesmani uzunligi AC:', AC)
# print('Kesmani uzunligi BC:', BC)
# print('Kesmaning Yegindisi D:', D)

# # 18 masala c ++ True
# Begin18. Sonlar oqida A, B, C nuqtalar berilgan. C nuqta A va B nuqtalar orasida joylashgan. AC va BC kesmalarning uzunligini toping
# A = int(input('A ni kiriting >> '))
# B = int(input('B ni kiriting >> '))
# C = int(input('C ni kiriting >> '))
# print('AC * BC =', abs(A - C) * abs(B - C))

# 19 masala c++ 50/50
# Begin19. Togri tortburchakning qarama-qarchi uchlari koordinatalari berilgan. Uning tomonlari koordinata oqiga parallel. Togri tortburchakning perimtri va yuzaasi aniqlansin
#
# x1 = int(input("x1 koordinatasini kiriting: "))
# y1 = int(input("y1 koordinatasini kiriting: "))
# x2 = int(input("x2 koordinatasini kiriting: "))
# y2 = int(input("y2 koordinatasini kiriting: "))
#
# a = abs(x1 - x2)
# b = abs(y1 - y2)
# print("Perimetr:", (a + b) * 2)
# print("Yuzasi:", a * b)


# 20 masala c ++ True
# Begin20. Tekislikdagi berilgan 2ta nuqta (x1,y1) va (x2,y2) orasidagi masofa topilsin, ildizni ichida (x2 - x1)kvadrati + (y1 - y2)kvadrati
# import math
# x1 = int(input('x1 >> '))
# x2 = int(input('x2 >> '))
# y1 = int(input('y1 >> '))
# y2 = int(input('y2 >> '))
# c = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
# print('Masofasi:', c)

# 21 masala c ++ True
# Begin21. Uchburchakning uchta tomoni uchlari koordinatalari berilgan (x1,y1)(x2,y2)(x3,y3). Ikki nuqta orasida masofa topish Begin20 da berilgan. Uchburchakning yuzasini va perimtrini toping. S = ildizni ichida p(p-a)(p-b)(p-c), p=(a+b+c)/2
# import math
# x1 = int(input('x1 >> '))
# x2 = int(input('x2 >> '))
# x3 = int(input('x3 >> '))
# y1 = int(input('y1 >> '))
# y2 = int(input('y2 >> '))
# y3 = int(input('y3 >> '))
#
# a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
# b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
# c = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
#
# p = (a + b + c)/2
# S = math.sqrt(p * (p - a) * (p - b) * (p - c))
# print("Perimetr:", p)
# print('Yuzasi:', S)

# 22 masala c++ True
# Begin22. Berilgan A va B sonlarning qiymatlarini almashtiring. A va B yangi qiymatlarda chiqarilsin
# A = int(input('A ni kiriting: '))
# B = int(input('B ni kiriiting: '))
#
# a = B
# b = A
#
# print('A ni qiymati:', a)
# print('B ni qiymati:', b)

# 23 masala c++ True
# Begin23. A,B  va C sonlar berilgan. A ni qiymati B ga, B ni qiymati C ga, va C ni qiymati A ga almashtirsin. A,B va C yangi qiymatlarda ekranga chiqarilsin
# A = int(input('A ni kiriting: '))
# B = int(input('B ni kiriting: '))
# C = int(input('C ni kiriting: '))
#
# a = B
# b = C
# c = A
#
# print('A ni qiymati:', a)
# print('B ni qiymati:', b)
# print('C ni qiymati:', c)

# 24 masala c++ True
# Begin24. A,B  va C sonlar berilgan. A ni qiymati C ga, C ni qiymati B ga, va B ni qiymati A ga almashtirsin. A,B va C yangi qiymatlarda ekranga chiqarilsin
# A = int(input('A ni kiriting: '))
# B = int(input('B ni kiriting: '))
# C = int(input('C ni kiriting: '))
#
# a = C
# b = A
# c = B
#
# print('A ni qiymati:', a)
# print('B ni qiymati:', b)
# print('C ni qiymati:', c)

# 25 masala c++ True
# Begin25. x ni qiymati berilganda y = 3x oltinchi darajasi - 6x kvadrati - 7 funksiyani qiymati aniqlansin
# x = int(input('X ni kiriting: '))
#
# y = 3 * x**6 - 6 * x**2 - 7
# print('Funksiya qiymati:', y)

# 26 masala c++ True
# Begin26.  x ni qiymati berilganda y = 4(x-3)6chi darajasi -7(x-3)kubi + 2 funksiyaning qiymati aniqlansin
# x = int(input('X ni kiriting: '))
# y = 4 * (x - 3)**6 - 7 * (x - 3)**3 + 2
# print('Funksiyani qiymati:', y)

# 27 masala c++ True
# Begin27. A soni berilgan. A ning A2,A4,A8 darajalarini aniqlovchi programma tuzilsin
# a = int(input('A ni kiriting:' ))
# a2 = a**2
# a4 = a**4
# a8 = a**8
# print('A ni 2 darajasi:', a2)
# print('A ni 4 darajasi:', a4)
# print('A ni 8 darajasi:', a8)

# 28 masala c++ True
# Begin28. A soni berilgan. A ning A2,A3,A5,A10,A15 darajani aniqlovchi programma tuzilsin
# a = int(input('A ni kiriting: '))
# a2 = a**2
# a3 = a**3
# a5 = a**5
# a10 = a**10
# a15 = a**15
# print('A ni 2 darajasi:', a2)
# print('A ni 3 darajasi:', a3)
# print('A ni 5 darajasi:', a5)
# print('A ni 10 darajasi:', a10)
# print('A ni 15 darajasi:', a15)

# 29 masala c++ True
# Begin29. a burchak gradusga berilgan (0gradus < a < 360gradus). Berilgan burchakning qiymati  radianga otkazuvchi programma tuzilsin
# import math
# a = int(input('A gradusni kiriting: '))
# radian = math.radians(a)
# print('Radian qiymati:', radian)

# 30 masala c ++ True
# Begin30. a burchak radianga berilgan (0 < a < 2p). Berilgan burchakning qiymati  gradusga otkazuvchi programma tuzilsin
#import math
# a = float(input('A radianni kiriting: '))
# degree = math.degrees(a)
# print('Gradus qiymati:', degree)

# 31 masala c ++ True
# Begin31. Temperatura Tf Farengeytda berilgan. Temperatura qiymati Tc gradus  selsiyga otkazuvchi programma tuzilsin Tc = (Tf - 32) *  5/9
# T = int(input('Son kiriting: '))
# T_c = (T - 32) * 5/9
# print('Temperaturada qiymati selsda:', T_c, 'C`')

# 32 masala c++ True
# Begin32. Temperatura Tf gradusga berilgan. Temperatura qiymati Tc farengeytga otkazuvchi programma tuzilsin Tc = (Tf - 32) *  5/9
# T_f = (int(input()))
# T_c = (T_f * 9/5) + 32
# print('Temperaturada qiymati Farengeytga:', T_c, 'F`')

# 33 masala c ++ True
# x = int(input(' kg ni kiriting:' ))
# a = int(input(' som ni kiriting:' ))
# y = x * a
# print('Y ning KG konfeti:', y)

# 34 masala c ++ True
# x = float(input('Shokolad kg ni kiriting: '))
# a = float(input('som ni kiriting: '))
# y = float(input('Konfet kg ni kiriting:' ))
# b = float(input('som ni kiriting: '))
#
# shokolad_qiymati = x * a
# konfet_qiymati = y * a
#
# qancha_farqi_narxi = shokolad_qiymati - konfet_qiymati
#
# print('Shokoladni narxi:', shokolad_qiymati)
# print('Konfetni narxi:', konfet_qiymati)
# print('Konfetdan qancha qimat turishi:', qancha_farqi_narxi)

# 35 masala c ++ True
# V = int(input('Qayiqni tezligi kiriting: '))
# U = int(input('Oqimni tezligini kiriting: '))
# T1 = int(input('Harakatlanish vaqtini kiriting: '))
# T2 = int(input('Oqimga qarshi kiriting:' ))
#
# S = ((V * T1) + (U * T2))
# print('Qayiqni yurgan yoli:', S)

# 36 masala c++ True
# V1 = int(input('Brinchi avtomobilni tezligi: '))
# V2 = int(input('Ikkinchi avtomobil tezligi: '))
# T = int(input('Uzoqlashgan vaqti (soat):' ))
# S = abs((V1 - V2) * T)
# print('Orasidagi masofa km: ', S)

# 37 masala c++ True
# V1 = int(input('Birinchi avtomobilni tezligi: '))
# V2 = int(input('Ikkinchi avtomobilni tezligi: '))
# T = int(input('Vaqt oraligidagi masofa(soat): '))
# S = abs((V1 - V2) * T)
# print('Orasidagi masofa km: ', S)

# 38 masala c++ True
# A = int(input('A sonni kiriting: '))
# B = int(input('B sonni kiriting: '))
# if A != 0:
#     x = -B / A
#     print('Tenlama x ni yechimi: ', x )
# else:
#     print('Tenglama notogri')

# 39 masala c++ False
# from math import sqrt
# A = int(input('A sonni kiriting: '))
# B = int(input('B sonni kiriting: '))
# C = int(input('C sonni kiriting: '))
#
# D = pow(B, 2) - 4 * A * C
# print(D)
# if D > 0:
#     x1 = (-B + sqrt(D)) / 2 * A
#     x2 = (-B - sqrt(D)) / 2 * A
#     print('X1 - ', x1)
#     print('x2 - ', x2)
# else:
#     print('Noldan katta emas')



# 40 masala c++
#
# A1, B1, C1, A2, B2, C2 = int(input('A1: ')), int(input('B1: ')), int(input('C1: ')), int(input('A2: ')), int(input('B2: ')), int(input('C2: '))
# D = (A1 * B2 - A2 * B1)
# x = (C1 * B2 - C2 * B1) / D
# y = (A1 * C2 - A2 * C1) / D
# print("x:", x)
# print("y:", y)