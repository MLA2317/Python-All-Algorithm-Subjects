# 5 - Mavzu Tanlash operatorga oid masalalar

# 1 - masala
# Case1. 1-7 gacha bo'lgan butun sonlar berilgan. Kiritilgan songa mos ravishda hafta kunlarini so'zda
# ifodalovchi programma tuzilsin. (1-Dushanba,2-Chorshanba,...h.k)
print('1-7 gacha butun son berilgan')
n = int(input('Butun son kiriting: '))
hafta = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba', 'Yakshanba']
kun = (n - 1) % 7
print('Kiritilgan son shu hafta', hafta[kun])

# 2 - masala
# Case2. K butun soni berilgan. Baho natijalarini chiqaruvchi programma tuzing.(1-yomon, 2-goniqarsiz,
# 3-goniqarli, 4-yahshi, 5-a'lo). Agar k soni 1-5 gacha oraliqqa tegishli bo 'Imasa "xato" deb chiqarilsin.
k = int(input('1 - 5 gacha oraligida son kiriting: '))
if k <= 5:
    baho = ['yomon', 'qoniqarsiz', 'qoniqarli', 'yaxhsi', 'alo']
    son = (k - 1) % 5
    print('Sizning bahoyingiz:', baho[son])
else:
    print('xato')

# 3 - masala
# Case3. Oy ragamini berilgan. Kiritilgan oy gaysi faslga tegishli ekanligini chigaruvchi programma
# tuzilsin. (Masalan: 2 chi oy, "qish")
oy = int(input('Oyning kiriting: '))
if 1 <= oy <= 2 and oy == 12:
    print('Sizning tanlagan oy Qish')
elif 3 <= oy <= 5:
    print('Sizning tanlagan oy Bahor')
elif 5 <= oy <= 8:
    print('Sizning tanlagan oy Yoz')
elif 8 <= oy <= 11:
    print('Sizning tanlagan oy Kuz')
else:
    print('Siz togri oyni kiritmadingiz')

# 4 - masala
# Case4. Oy raqami berilgan. Shu oyda nechta kun borligini aniqlovchi programma tuzilsin.
print('1 - 12 gacha oyni kiriting')
n = int(input('Butun son kiriting: '))
if n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12:
    print(f"Bu oyning shuncha 31 kuni bor")
elif n == 4 or n == 6 or n == 9 or n == 11:
    print(f"Bu oyning shuncha 30 kuni bor")
else:
    print(f"Bu oyning shuncha 28 kuni bor")

# 5 - masala
# Case5. A. B hagigiy va amal butun soni berilgan. A va B sonlari ustida arifmetik amallar bajaruvchi
# progaramma tuzilsin. amal quyidagi qiymatlarni qabul qiladi: 1-qo shish, 2-ayirish, 3-bo'lish, 4. ko paytinsh.
a = int(input('Son kiriting 1 - 4 gacha: '))
A = int(input('A ni kiriting: '))
B = int(input('B ni kiriting: '))
if a == 1:
    qiymat = A + B
    print('Qoshishni yegindisi:', qiymat)
elif a == 2:
    qiymat = A - B
    print('Ayirishni yegindisi:', qiymat)
elif a == 3:
    qiymat = A // B
    print('Bolishni yegindisi:', qiymat)
elif a == 4:
    qiymat = A * B
    print('Kopaytmani yegindisi:', qiymat)
else:
    print('Notogri amal kiritildi')

# 6 - masala
# Case6. Uzinlik birliklari quyidagi tartibda berilgan. 1-desimetr, 2-kilometr, 3-metr, 4-millimeter, 5-
# santimetr. Uzunlik birligini bildiruvchi son berilgan (1 - 5 oraligda) va shu birlikdagi kesma uzunligi
# berilgan (haqiqiy son). Kesmaning uzunligini metrlarda ifodalofchi programma tuzilsin.
uzunlik = int(input('1 - 5 gacha son kiriting: '))
kesma = int(input('Butun son kiriiting: '))
if uzunlik == 1:
    kesmaning_metrda = kesma / 10
    print('Kesmaning uzunligi metrda', kesmaning_metrda, 'desimetr')
elif uzunlik == 2:
    kesmaning_metrda = kesma * 1000
    print('Kesmaning uzunligi metrda', kesmaning_metrda, 'km')
elif uzunlik == 3:
    kesmaning_metrda = kesma
    print('Kesmaning uzunligi metrda', kesmaning_metrda, 'metr')
elif uzunlik == 4:
    kesmaning_metrda = kesma / 1000
    print('Kesmaning uzunligi metrda', kesmaning_metrda, 'milimetr')
elif uzunlik == 5:
    kesmaning_metrda = kesma / 100
    print('Kesmaning uzunligi metrda', kesmaning_metrda, 'sanitmetr')
else:
    print('Bunday son mavjud emas')

# 7 - masala
# Case7. Og'irlik birliklari quyidagi tartibda berilgan. 1-kilogramm, 2-milligramm, 3-gramm, 4-tonna, 5.
# sentner. Og'irlik birligini bildiruvchi soni berilgan va shu birlikdagi og irlik qiymati berilgan. Og'irlikni
# kilogramda ifodalofchi programma tuzilsin.
birlik = int(input('1 - 5 gacha son kiriting: '))
ogirlik = int(input('Butun son kiriting: '))

if birlik == 1:
    kilogram_ogirlik = ogirlik
    print('Ogirligi', kilogram_ogirlik, 'killogramm')
elif birlik == 2:
    kilogram_ogirlik = ogirlik / 1000000
    print('Ogirligi', kilogram_ogirlik, 'milligramm')
elif birlik == 3:
    kilogram_ogirlik = ogirlik / 1000
    print('Ogirligi', kilogram_ogirlik, 'gramm')
elif birlik == 4:
    kilogram_ogirlik = ogirlik * 1000
    print('Ogirligi', kilogram_ogirlik, 'tonna')
elif birlik == 5:
    kilogram_ogirlik = ogirlik * 100
    print('Ogirligi', kilogram_ogirlik, 'sentner')


# 8 - masala False
# Case8. Sanani bildiruvchi ikkita butun son berilgan D (kun) va M (oy). (Kabisa bo'lmagan yil sanasi
# kiritiladi). Berilgan sanani ifodalovchi programma tuzilsin. Kabisa ilida 366 kun, kabisa bo'lmagan
# yilda 365 kun bor bo'ladi.
d = int(input('kunni kiriting: '))
m = int(input('oyni kiriting: '))
y = int(input('yilni kiriting: '))

if m % 4 == 0:
    if m % 100 == 0:
        if m % 400 == 0:
            y = True
        else:
            y = False
    else:
        y = True
if y:
    kunlar_soni = d
    print('Kabisa yilida', kunlar_soni)
else:
    kunlar_soni = d
    print('Kabisa yilida', kunlar_soni)


# 9 - masala
# Case9. Ikkita butun son berilgan D (kun) va M (oy). (Kabisa bo' imagan yil sanasi kiritiladi). Berilgan
# sanadan keyingi sanani ifodalovchi programma tuzilsin.
d = int(input('kunni kiriting: '))
m = int(input('oyni kiriting: '))
y = int(input('yilni kiriting: '))
if m > 12 or m < 1:
    print('Notogri raqam kiritildi')
else:
    if m in [1, 3, 5, 7, 8, 10, 12]:
        max_kun = 31
    elif m in [4, 6, 9, 11]:
        max_kun = 30
    else:
        if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
            max_kun = 29
        else:
            max_kun = 28

    if d > max_kun or d < 1:
        print("Noto'g'ri kun raqami kiritildi.")
    else:
        if m == 12 and d == 31:
            d = 1
            m = 1
            y += 1
        elif d == max_kun:
            d = 1
            m += 1
        else:
            d += 1

        print(f"Keyingi sana: {d} kun - {m} oy - {y} yil")


# 10 - masala
# Case10. Robot fagat to rtta tomonga ko cha oladi("s" -shimol, "T"-janub, "q"-sharq. "g"-g'arb) va uchta
# raqamli kamanda: 0-harakni davom ettir, 1-chapga buril, 2-o'ngga buril. Y - robot yo'nalishi va K -
# kamanda berilgan. Berilgan kamanda bajarilgandan keying robot holatini aniqlovchi programma tuzilsin
Y = input('Robot yonalishini kiriting: ("s" - shimol, "j" - janub, "q" - sharq, "g" - garb): ')
K = int(input('Komanda raqamani kiriting: (0 - Harakatni davom ettir, 1 - Chapga buril, 2 - Onga buril): '))

if K == 0:
    keyingi_yonalish = Y
    print(f"Keyingi yonalish: {keyingi_yonalish}")
if K == 1:
    if Y == "s":
        keyingi_yonalish = "g"
    elif Y == "g":
        keyingi_yonalish = "q"
    elif Y == "q":
        keyingi_yonalish = "j"
    else:
        keyingi_yonalish = "s"
    print(f"Keyingi yonalish: {keyingi_yonalish}")
if K == 2:
    if Y == "s":
        keyingi_yonalish = "j"
    elif Y == "j":
        keyingi_yonalish = "q"
    elif Y == "q":
        keyingi_yonalish = "g"
    else:
        keyingi_yonalish = "s"

    print(f"Keyingi yonalish: {keyingi_yonalish}")


# 11 - masala
#Case11. Lokatr dunyoni bir tomoniga qaratilgan ("s" -shimol, "T"-janub, "q"-sharq. "g"-g'arb) va uchta
# raqamli kamanda: 0-ongga buril, 1-chapga buril, 2-burilish 180`. C - lokatrni boshlangich holati
# K1, K2 komandalari berilgan. Berilgan komanda bajarilgandan keyingi lokatr holatini aniqlovchi programma tuzilsin
C = input('Robot yonalishini kiriting: ("s" - shimol, "j" - janub, "q" - sharq, "g" - garb): ')
K1 = int(input('Komanda raqamani kiriting: (0 - Onga buril, 1 - Chapga buril, 2 - Burilish 180`C.): '))
K2 = int(input('Komanda raqamani kiriting: (0 - Onga buril, 1 - Chapga buril, 2 - Burilish 180`C.): '))

if K1 == 0:
    if C == "s":
        keyingi_lokatr = "j"
    elif C == "j":
        keyingi_lokatr = "q"
    elif C == "q":
        keyingi_lokatr = "g"
    else:
        keyingi_lokatr = "s"
elif K1 == 1:
    if C == "s":
        keyingi_lokatr = "g"
    elif C == "g":
        keyingi_lokatr = "q"
    elif C == "q":
        keyingi_lokatr = "j"
    else:
        keyingi_lokatr = "s"

elif K1 == 2:
    if C == "s":
        keyingi_lokatr = "g"
    elif C == "g":
        keyingi_lokatr = "s"
    elif C == "q":
        keyingi_lokatr = "s"
    else:
        keyingi_lokatr = "q"
    if C == "j":
        keyingi_lokatr = "g"
    elif C == "g":
        keyingi_lokatr = "j"
    elif C == "q":
        keyingi_lokatr = "j"
    else:
        keyingi_lokatr = "q"
print(f'Keyingi K1 lokatr holati: {keyingi_lokatr}')

if K2 == 0:
    if C == "s":
        keyingi_lokatrs = "j"
    elif C == "j":
        keyingi_lokatrs = "q"
    elif C == "q":
        keyingi_lokatrs = "g"
    else:
        keyingi_lokatrs = "s"
elif K2 == 1:
    if C == "s":
        keyingi_lokatrs = "g"
    elif C == "g":
        keyingi_lokatrs = "q"
    elif C == "q":
        keyingi_lokatrs = "j"
    else:
        keyingi_lokatrs = "s"

elif K2 == 2:
    if C == "s":
        keyingi_lokatrs = "g"
    elif C == "g":
        keyingi_lokatrs = "s"
    elif C == "q":
        keyingi_lokatrs = "s"
    else:
        keyingi_lokatrs = "q"
    if C == "j":
        keyingi_lokatrs = "g"
    elif C == "g":
        keyingi_lokatrs = "j"
    elif C == "q":
        keyingi_lokatrs = "j"
    else:
        keyingi_lokatrs = "q"

print(f'Keyingi K2 lokatr holati: {keyingi_lokatrs}')

# 12 - masala
# Case12. Doiraning elementiari quyidagi tartibda nomerlangan. 1-radius R, 2-diametr D = 2.R, 3.
# uzunligi L=2-z-R, 4-doiraning yuzasi S = 7- R'. Shu elementlardan bittasi berlganda golganlarini
# topuvchi programma tuzilsin. * = 3.14
R = float(input("Doirani kiriting: "))
p = 3.14
D = 2 * R
L = 2 * p * R
S = p * pow(R, 2)

element_nomeri = int(input("Element nomerini kiriting (1-radius R, 2-diametr D = 2*R, 3-uzunligi L=2*p*R, 4-yuzasi S = p * R**2'): "))

if element_nomeri == 1:
    qolgan = R
    r = 'Radiusi'
elif element_nomeri == 2:
    qolgan = D
    r = 'Diametri'
elif element_nomeri == 3:
    qolgan = L
    r = 'Uzunligi'
elif element_nomeri == 4:
    qolgan = S
    r = 'Yuzasi'

print(f"Qolganlari : {qolgan} ning {r}")

# 13-masala
# Case13. Tengyonli uchburchakning elementlari quyidagi tartibda nomerlangan. 1-katet a, 2-gipotenuza
# C = a * ildizni ichida 2
# 3.gepotenuzaga tushirilgan baladik h=c/2, 4-yuzasi S=c*h/2
# Shu elementlardan bittasi
# berilganda golganiarini topuvchi programma tuzilsin.
from math import sqrt
a = float(input("Teng yonlini uchburchakni kiriting: "))

k = a
c = a * sqrt(2)
h = c / 2
S = (c * h) // 2
element_nomeri = int(input("Element nomerini kiriting (1-katet a, 2-gipotenuza c=a*sqrt(2),"
                           " 3- gipotenuzaga tushirlgan balandlik h=c/2, 4-yuzasi S=(c*h)//2: "))

if element_nomeri == 1:
    qolgani = k
    s = "Kateti"
elif element_nomeri == 2:
    qolgani = c
    s = "Gipotenuzasi"
elif element_nomeri == 3:
    qolgani = h
    s = "Gipotenuzaga tushirilgan balandligi"
elif element_nomeri == 4:
    qolgani = S
    s = "Yuzasi"

print(f"Qolganlari: {qolgani} ning {s}")

# 14 - masala
# Case14. Tengtomonli uchburchakning elementlari quyidagi tartibda nomerlangan. 1-tomoni a, 2-ichki
# chizilgan aylananing radiusi R1 = a* ildizni ichida3/6 3. tashqi chizilgan avlananing radiusi R2 = 2*R1. 4- yuzasi
# S = a kvadrat ildizni ichida 3/4. Shu elementlardan bittasi berilganda golganlarini topuvchi programma tuzilsin
from  math import sqrt
a = float(input("Tomonni kiriting: "))

t = a
R1 = a * sqrt(3/6)
R2 = 2 * R1
S = pow(a, 2) * sqrt(3/4)

element_nomeri = int(input("Element nomerini kiriting (1-Tomon a, 2-Ichki chizilgan aylananing radiusi R1=a*sqrt(3/6),\n"
                           "3-tashqi chizilgan avlananing radiusi R2=2*R1, 4-vuzasi S =a**2*sqrt(3/4): "))

if element_nomeri == 1:
    qolgan = t
    e = 'Tomoni'
elif element_nomeri == 2:
    qolgan = R1
    e = 'Ichki chizilgan aylananing radiusi'
elif element_nomeri == 3:
    qolgan = R2
    e = 'Tashqi chizilgan avlananing radiusi'
elif element_nomeri == 4:
    qolgan = S
    e = 'Yuzasi'
print(f"Qolganlari: {qolgan} ning {e}")

# 15 - masala
# Case15. O' yin kartasi turlari berilgan 1-g isht, 2-olma, 3-chillak, 4-qarg a. 10 lik kartadan katta kartalar
# quyidagi qiymatlarni ozlashtirgan: 11-valet, 12-dama, 13-qirol, 14-tuz. Ikkita butun son berilgan N-karta
# qiymati (6 <= N <= 14), M-karta turi(1 <= M <= 4) kiritilganda karta nomlarini (masalan: "olti qarg a") chigarib
# beruvchi programma tuzilsin.
n = int(input("Kartani qiymatini kiriting (6-14): "))
m = int(input("Kartani turini kiriting (1-g isht, 2-olma, 3-chillak, 4-qarg'a): "))


kartani_turlar = {1: "g'isht", 2: "olma", 3: "chillak", 4: "qarg'a"}
kartani_qiymatlar = {6: "olti", 7: "yetti", 8: "sakkiz", 9: "to'qqiz", 10: "o'n", 11: "valet", 12: "dama", 13: "karol", 14: "tuz"}

kartani_turi = kartani_turlar[m]

if n in kartani_qiymatlar:
    kartani_qiymat = kartani_qiymatlar[n]
    kartani_nomi = f"{kartani_qiymat} {kartani_turi}"
    print(kartani_nomi)
else:
    print("Noto'g'ri karta qiymati kiritildi.")

# 16 - masala
# Case16. Yoshni villarda aniqlovchi 20-69 gacha butun son berilgan. Son kiritilganda unga mos
# so'zlarda ifodalovchi programma tuzilsin. ("vigirma yosh", '"qirg uch yosh" va h.k.)
y = int(input("Yoshni kiriting (20-69 oralig'ida): "))
birliklar = ['', "bir", "ikki", "uch", "to'r", "besh", "olti", "yetti", "sakkiz", "to'qqiz"]
onliklar = ['', "", "yigirma", "ottiz", "qiriq", "ellik", "oltmish"]

if y > 70 or y < 19:
    print('Notogri son kiritildi')
else:
    onlik = (y % 100) // 10  # 4
    birlik = y % 10  # 1

    yoshi = onliklar[onlik] + " " + birliklar[birlik]
    print('Sizning yoshingiz', yoshi)

# 17 - masala
# Case17. O'quv masalalarini aniglovchi 10-40 gacha butun son berilgan. Son kiritilganda unga mos
# sozlarda ifodalovchi programma tuzilsin. ( "yigirmata masala", "o'n uchta masala" va h.k.)
y = int(input("Masalani kiriting (10-40 gacha): "))
birliklar = ['', "bitta", "ikkita", "uchta", "to'rta", "beshta", "oltita", "yettita", "sakkizta", "to'qqizta"]
onliklar = ['', "on", "yigirma", "ottiz", "qiriq"]

if y > 40 or y < 10:
    print('Notogri son kiritildi')
else:
    onlik = (y % 100) // 10  # 4
    birlik = y % 10  # 1

    masala = onliklar[onlik] + " " + birliklar[birlik]
    print('Sizning ishlagan masalez:', f"{masala} masala")

# 18 - masala
# Case18. 100-999 gacha oraligdagi sonlarni so'zlarda ifodalovchi programma tuzilsin. (masalan: 123-
# "bir yuz yigirma uch").
son = int(input("Sonni kiriting (100-999 oralig'ida): "))

birliklar = ["", "bir", "ikki", "uch", "to'rt", "besh", "olti", "yetti", "sakkiz", "to'qqiz"]
onliklar = ["", "o'n", "yigirma", "o'ttiz", "qirq", "ellik", "oltmish", "yetmish", "sakson", "to'qson"]
yuzliklar = ["", "bir yuz", "ikki yuz", "uch yuz", "to'rt yuz", "besh yuz", "olti yuz", "yetti yuz", "sakkiz yuz", "to'qqiz yuz"]

if son < 100 or son > 999:
    print("Noto'g'ri son kiritildi")
else:
    yuzlik = son // 100
    onlik = (son % 100) // 10
    birlik = son % 10

    soz = yuzliklar[yuzlik] + " " + onliklar[onlik] + " " + birliklar[birlik]
    print(soz)

# 19 - masala
# Case19. Sharg kalendarida 60 illik davr qabul qilingan. Yil muchali 5 ta rang (yashil, qizil, sariq, oq va
# qora) va 12 ta hayvon (sichgon, sigir, yolbars, quyon, ajdar, ilon, ot, go'y, maymun, tovuq, it va
# to'ngizlardan) nomlaring kombinatsiyasidan kelib chigadi. Yilning raqamiga qarab uning muchalini
# aniqlovchi programma tuzilsin. 1984-davr boshi: "Yashil sichgon vili"
yil = int(input('Yilingizni kiriting: '))
ranglar = ["yashil", "qizil", "sariq", "oq", "qora"]
hayvonlar = ["sichgon", "sigir", "yo'lbars", "quyon", "ajdar", "ilon", "ot", "qo'y", "maymun", "tovuq", "it", "to'ngizlar"]

raqam = (yil - 1984) % 60
print(raqam)
mucha_rang = ranglar[raqam // 12]
print(mucha_rang)
muchani_hayvon = hayvonlar[raqam % 12]
print(muchani_hayvon)

print(f"{mucha_rang} {muchani_hayvon} yili")

# 20 - masala
# Case20. Ikkita burj vaqtlarini aniqlovchi butun son berilgan: D(kun), M(oy).
# Berilgan sana gaysi buriga kirishini aniqlovchi programma tuzilsin.
# "Qovga" (20.1-18.2)'. "Baliq (19.2-20.3)', "Qo'ÿ (21.3-19.4)', "Buzoq (20.4-20.5)', "Egizaklar (21.5.21.6),
# "Qisqichbaga (22.6-22.7). "Arsion (23.7-22.8). "Parizod (23.8-22.9), "Tarozi (23.9-22.10)*
# "Chayon (23.10-22.11), "Oqotar (23.11-21. 12), "Echki (22.12-19.1)°
d = int(input('Kunni kiritining: '))
m = int(input('Oyni kiriting: '))
if d >= 32 or m >= 13:
    print('Siz notogri kun va oyni kiritdingiz')
elif (d >= 20 and m == 1) or (d <= 18 and m == 2):
    burj = "Qovg'a"
elif (d >= 19 and m == 2) or (d <= 20 and m == 3):
    burj = "Baliq"
elif (d >= 21 and m == 3) or (d <= 19 and m == 4):
    burj = "Qo'y"
elif (d >= 20 and m == 4) or (d <= 20 and m == 5):
    burj = "Buzoq"
elif (d >= 21 and m == 5) or (d <= 21 and m == 6):
    burj = "Egizak"
elif (d >= 22 and m == 6) or (d <= 22 and m == 7):
    burj = "Qisqichbaqa"
elif (d >= 23 and m == 7) or (d <= 22 and m == 8):
    burj = 'Arslon'
elif (d >= 23 and m == 8) or (d <= 22 and m == 9):
    burj = "Parizod"
elif (d >= 23 and  m == 9) or (d <= 22 and m == 10):
    burj = 'Tarozi'
elif (d >= 23 and m == 10) or (d <= 22 and m == 11):
    burj = 'Chayon'
elif (d >= 23 and m == 11) or (d <= 21 and m == 12):
    burj = "O'qatar"
elif (d >= 22 and m == 12) or (d <= 19 and m == 1):
    burj = "Echki"

print('Sizning burchingiz', burj)
