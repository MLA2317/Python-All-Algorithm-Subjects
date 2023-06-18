# 1 - masala
# Integer1. Uzunlik L santimetrda berilgan. Undagi to'liq metrlar sonini aniqlovchi programma tuzilsin.
# (1m=100cm)

L = int(input("Santimetrni kiriting: "))

m = L / 100
print('Metr: ', m)


# 2 - masala
# Lazizbek, [6/14/2023 11:28 PM]
# Integer2. Og irlik M kilogramda berilgan. Undagi to'lig tonnalar sonini aniqlovchi programma tuzilsin.
# (1t=1000kg)

M = int(input('Kilogram kiriting: '))
t = M / 1000
print('Tonna:', t)


# 3 - masala
# Integer3. Fayining hajmi baytlarda berilgan. Bo'lib butunni olish operatsiyasidan foydalanib fayl
# hajmining to'lig kilobaytlarda ifodalovchi programma tuzilsin. (1 Kb=1024 bavt)
bayt = int(input('Bayt ni kiriting: '))
k = bayt // 1000
print('Kb:', k)



# 4 - masala
# Integer4. A va B (A > B) musbat sonlari berilgan. A kesmada, B kesmani necha marta joylashtirish
# mumkinligini aniqlovchi programma tuzilsin.
A = int(input('A sonni kiriting: '))
B = int(input('B sonni kiriitng: '))
if A > B:
    count = A // B
    print('Nechi marta kesmda joylashgani: ', count)
else:
    print('A kotta bolish kerak')


# 5 - masala
# Integer5. A va B (A > B) musbat sonlar berilgan. A kesmada B kesmani necha marta joylashtirish
# mumkin. A kesmada B kesmaning joylashmagan qismini aniqlovchi programma tuzilsin.

A = int(input('A sonni kiriting: '))
B = int(input('B sonni kiriitng: '))
if A > B:
    remainder = A % B
    print('Kesmaning Joylashmagan qismi: ', remainder)
else:
    print('A kotta bolish kerak')



# 6 - masala
# Integer6. Ikki xonali son berilgan. Oldin uning o'nliklar xonasidagi raqamni, so'ng birlar xonasidagi
# raqamni chiqaruvchi programma tuzilsin

son = int(input('Ikki honali son kiriting >> '))
onlik_son = son // 10
birlik_son = son % 10
print('Onlik xonasi:', onlik_son)
print('Birlik xonasi:', birlik_son)


# 7 - masala
#Integer7. Ikki xonali son berilgan. Uning raqamlari yig indisini aniqlovchi programma tuzilsin.

son = int(input('Ikki honali son kiriting >> '))
onlik_son = son // 10
birlik_son = son % 10
yegindi = onlik_son + birlik_son
print('Yegindisi: ', yegindi)



# 8 - masala
# Integer8. Ikki xonali son berilgan. Uning raqamlari o'rini almashtirishdan hosil bo' lgan sonni aniqlovchi
# programma tuzilsin.

son = int(input('Ikki honali son kiriting >> '))
onlik_son = son // 10 # 12 - > 1
birlik_son = son % 10 # 12 - > 2
print(onlik_son)
print(birlik_son)
birlik = onlik_son
onlik = birlik_son
print('onlik:', onlik)
print('birlik:', birlik)


# 9 - masala
# Integer9. Uch xonali son berilgan. Uning yuzlar xonasidagi q aniglovchi programma tuzilsin.

n = int(input('Uch xonali son kiriting: '))
yuzlar_xonasi = (n // 100) % 10 # 321 -> 3
print('Yuzlar xonasi: ', yuzlar_xonasi)


# 10 - masala
# Integer10. Uch xonali son berilgan. Oldin uni birliklar xonasidagi raqamni so'ng o'nliklar xonasidagi
# ragamni chigaruvchi programma tuzilsin.

n = int(input('Uch xonali son kiriting: '))
onlik_xonasi = n // 10 # 321 - > 2
yuzlar_xonasi = (n // 100) % 10 # 321 - > 3
print('Onlik xonalar: ', onlik_xonasi)
print('Yuzlik xonalar: ', yuzlar_xonasi)


# 11 - masala

# Integer11. Uch xonali son berilgan. Uning raqamlar yig indisini aniqlovchi programma tuzilsin.

n = int(input('Uch xonali son kiriting: '))
birlik_son = n % 10 # # 321 - > 1
onlik_xonasi = (n // 10) % 10 # 321 - > 2
yuzlar_xonasi = (n // 100) % 10 # 321 - > 3

yegindi = birlik_son + onlik_xonasi + yuzlar_xonasi
print("Yeg'indisi: ", yegindi)


# 12 - masala
# Integer12. Uch xonali son berilgan. Uning raqamlarini teskari tartibda yozishdan hosil bo lgan sonni
# aniglovchi program tuzilsin.


n = int(input('Uch xonali son kiriting: '))
birlik_son = n % 10 # # 321 - > 1
onlik_xonasi = (n // 10) % 10 # 321 - > 2
yuzlar_xonasi = (n // 100) % 10 # 321 - > 3
a = birlik_son
b = onlik_xonasi
c = yuzlar_xonasi
print('teskarisi: ', a, b, c)


# 13 - masala
# Integer13. Uch xonali son berilgan. Uning chapdan birinchi raqamini o'chirib o'ng tarafiga yozishdan
# hosil bo'lgan sonni aniglovchi programma tuzilsin.

n = int(input('Uch xonali son kiriting: '))
birliklar_xonasi = n % 10 # 321 - > 1

onliklar_xonasi = (n // 10) % 10 # 321 - > 2

yuzlar_xonasi = n // 100 # 321 - > 3


chap_birinchi_ochir = birliklar_xonasi * 100 + onliklar_xonasi * 10 + yuzlar_xonasi


print("Natija:", chap_birinchi_ochir)


# 14 - masala
# Integer14. Uch xonali son berilgan. Uning o'ngdan birinchi raqamini o'chirib chap tarafiga yozishdan
# hosil bo' lgan sonni aniqlovchi programma tuzilsin.


n = int(input('Uch xonali son kiriting: '))
birliklar_xonasi = n % 10 # 321 - > 1

onliklar_xonasi = (n // 10) % 10 # 321 - > 2

yuzlar_xonasi = n // 100 # 321 - > 3


ong_birinchi_ochir = onliklar_xonasi * 100 + birliklar_xonasi * 10 + yuzlar_xonasi


print("Natija:", ong_birinchi_ochir)


# 15 - masala
# Integer15. Uch xonali son berilgan. Uning o'nliklar xonasidagi raqam bilan yuzliklar xonasidagi raqamni
# almashtirishdan hosil bo lgan sonni aniqlovchi programma tuzilsin. (Kirish =123; Natija = 213)


n = int(input('Uch xonali son kiriting: '))
birliklar_xonasi = n % 10 # 123 - > 3

onliklar_xonasi = (n // 10) % 10 # 123 - > 2

yuzlar_xonasi = n // 100 # 123 - > 1

almashtirish = onliklar_xonasi * 100 + yuzlar_xonasi * 10 + birliklar_xonasi

print('Onlik va Yuzlik xonadagi sonlar almashtirilgan: ', almashtirish)


# 16 - masala
# Integer16. Uch xonali son berilgan. Uning o'nliklar xonasidagi raqam bilan birliklar xonasidagi raqamni
# almashtirishdan hosil bo 'lgan sonni aniqlovchi programma tuzilsin. (Kirish = 123; Natija = 132)


n = int(input('Uch xonali son kiriting: '))
birliklar_xonasi = n % 10 # 123 - > 3

onliklar_xonasi = (n // 10) % 10 # 123 - > 2

yuzlar_xonasi = n // 100 # 123 - > 1

almashtirish = yuzlar_xonasi * 100 + birliklar_xonasi * 10 + onliklar_xonasi

print('Onlik va Birlik xonadagi sonlar almashtirilgan: ', almashtirish)


# 17 - masala
# Integer17.  999 dan katta bo'lgan son berilgan. Bir marta bo'lib butunni va bo'lib goldigni olish
# operatsiyasidan foydalanib berilgan sonni yuzliklar xonasidagi sonni aniglovchi programma tuzilsin.

n = int(input('999 dan katta son kiriting: '))
b = n // 100
print(b)
yuzliklar_son = (n // 100) % 10
print('Yuzliklar sonlari: ', yuzliklar_son)


# 18 - masala
# Integer18. 999 dan katta bo lgan son berilgan. Bir marta bo'lib butunni va bo'lib goldiqni olish
# operatsiyasidan fordalanib berilgan sonni mingliklar xonasidagi sonni aniglovchi programma tuzilsin.

# 18 - masala
n = int(input('999 dan katta son kiriting: '))
b = n // 100
print(b)
yuzliklar_son = (n // 1000) % 10
print('Yuzliklar sonlari: ', yuzliklar_son)


# 19 - masala
# Integer19. Kun boshidan boshlab N sekund vaqt o'tti. Kun boshidan boshlab qancha minut to'la o'tganligini aniqlovchi programma tuzilsin.

n = int(input('N sekund ni kiriting: '))
minut = (n // 60) % 60
print('Minut:', minut)


# # 20 - masala
# Integer20. Kun boshidan boshlab N sekund vagt o'tti. Kun boshidan boshlab qancha to'la soat otganligini aniglovchi programma tuzilsin.

n = int(input('N sekund ni kiriting: '))
# s = n // 3600
# print(s)
# h = s % 24
# print(h)
soat = (n // 3600) % 24
print('Soat:', soat)



# 21 - masala
# Integer21. Kun boshidan boshlab N sekund vagt o'tti. Kun boshidan boshlab gancha minut va sekund o'tganini aniqlovchi programma tuzilsin.

n = int(input('N sekund ni kiriting: '))
minut = (n // 60) % 60
sekund = n % 60
print('Minut va Sekund: ', f"{minut} min", 'va', f"{sekund} sek")


# 22 - masala
# Integer22. Kun boshidan boshlab N sekund vaqt o'tti. Kun boshidan boshlab qancha soat va sekund o'tganini aniqlovchi programma tuzilsin.

n = int(input('N sekund ni kiriting: '))
soat = (n // 3600) % 24
sekund = n % 60
print('Soat va Sekund: ', f"{soat} soat", 'va', f"{sekund} sekund")



# 23 - masala
# Integer23. Kun boshidan boshlab N sekund vagt o'tti. Kun boshidan boshlab gancha soat, minut va sekund o tganini aniglovchi programma tuzilsin.

n = int(input('N sekund ni kiritng: '))
sekund = n % 60
minut = (n // 60) % 60
soat = (n // 3600) % 24

print('Soat va minut va sekund: ', f"{soat}h:{minut}m:{sekund}s")

# 24 - masala
# Integer24. Hafta kunlari quyidagicha tartibda berilgan. 0-yakshanba, 1-dushanba, 2-seshanba, 3.
# chorshanba, 4-payshanba, 5-juma, 6-shanba. 1-365 oraliqda yotuvchi K soni berilgan. Agar 1-yanvar
# dushanba bo'lsa, kiritilgan K - kun haftaning qaysi kuniga to'g'ri kelishini aniqlovchi programma tuzilsin.


K = int(input('1 - 365 oraligida son kiriting >> '))

hafta = ['yakshanba', 'dushanba', 'seshanba', 'chorshanba', 'payshanba', 'juma', 'shanba']
sana = (K + 0) % 7
print('sana:', hafta[sana],'kuni')


# 25 - masala
# Integer25. Hafta kunlari quyidagicha tartibda berilgan. 0-yakshanba, 1-dushanba, 2-seshanba, 3-
# chorshanba, 4-payshanba, 5-juma, 6-shanba. 1-365 oraliqda yotuvchi K soni berilgan. Agar 1-yanvar
# payshanba bo'lsa, kiritilgan K - kun haftaning qaysi kuniga to'g'ri kelishini aniqlovchi programma
# tuzilsin.

K = int(input('1 - 365 oraligida son kiriting >> '))

hafta = ['yakshanba', 'dushanba', 'seshanba', 'chorshanba', 'payshanba', 'juma', 'shanba']
sana = (K + 3) % 7
print('sana:', hafta[sana],'kuni')


# 26 - masala
# Integer26. Hafta kunlari quyidagicha tartibda berilgan. 1-dushanba, 2-seshanba, 3-chorshanba, 4-
# payshanba, 5-juma, 6-shanba, 7-yakshanba. 1-365 oraliqda yotuvchi K soni berilgan. Agar 1-yanvar
# seshanba bo'lsa, kiritilgan K - kun haftaning qaysi kuniga to'g ri kelishini aniqlovchi programma tuzilsin.

K = int(input('1 - 365 oraligida son kiriting >> '))
hafta = ['yakshanba', 'dushanba', 'seshanba', 'chorshanba', 'payshanba', 'juma', 'shanba']
sana = (K + 1) % 7
print('sana:', hafta[sana],'kuni')


# 27 - masala
# Integer27. Hafta kunlari quyidagicha tartibda berilgan. 1-dushanba, 2-seshanba, 3-chorshanba, 4.
# payshanba, 5-juma, 6-shanba, 7-yakshanba. 1-365 oraliqda yotuvchi K soni berilgan. Agar 1-yanvar
# yakshanba bo'lsa, kiritilgan K - kun haftaning qaysi kuniga to'g'ri kelishini aniqlovchi programma
# tuzilsin.


K = int(input('1 - 365 oraligida son kiriting >> '))
hafta = ['yakshanba', 'dushanba', 'seshanba', 'chorshanba', 'payshanba', 'juma', 'shanba']
sana = (K - 1) % 7
print('sana:', hafta[sana],'kuni')


# 28 - masala
# Integer28.Hafta kunlari quyidagicha tartibda berilgan. 1-dushanba, 2-seshanba, 3-chorshanba, 4.
# payshanba, 5-juma, 6-shanba, 7-yakshanba(N 1-7gacha bo lgan hafta kunlari soni). 1-365 oraligda
# yotuvchi K soni berilgan. Agar 1-yanvar N chi kunga to'g'ri kelsa, kiritilgan K - kun haftaning qaysi
# kuniga to g ri kelishini aniglovchi programma tuzilsin

K = int(input('1 - 365 oraligida son kiriting >> '))
N = int(input('1 - 7 gacha hafta kunlari soni kiriting >> '))

hafta = ['dushanba', 'seshanba', 'chorshanba', 'payshanba', 'juma', 'shanba', 'yakshanba',]
sana = ((K - N) % 7)
print('sana:', hafta[sana], 'kuni')


# 29 - masala
# Integer29. A,B,C butun sonlar berilgan. Tomonlari A va B bo'lgan to giri to rtburchakka tomoni C bo'lgan kvadrat eng ko°p joylashtirilsin. To'g' rito'rt burchakka eng ko'p joylashgan kvadratlar soni va joylashmay golgan qismi yuzasini aniglovchi programma tuzilsin.

A = int(input('A ni kiriting >> '))
B = int(input('B ni kiriting >> '))
C = int(input('C ni kiriting >> '))

min_tomon = min(A, B) # 3, 2 -> 2
print(min_tomon)
max_kvadrat_soni = (min_tomon // C)**2 #C = 4 , 2 // 4 = 0.5**2 = 0
print(max_kvadrat_soni)
joylashmagan_tomoni = min_tomon % C # 2 % 4
print(joylashmagan_tomoni)
print('Eng kop joylashgan tomoni: ', max_kvadrat_soni)
print('Joylashmay qolgan yuzasi: ', joylashmagan_tomoni)


# Integer30. Qasidir yil berilgan. Berilgan yilning qaysi yuz yillikka kirishini aniqlovchi programma tuzilsin.
# (Masalan: 20 - yuz yillikning boshi 1901 yil).