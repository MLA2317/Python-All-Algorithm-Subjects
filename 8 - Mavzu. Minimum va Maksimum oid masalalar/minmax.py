#  8 - Mavzu. Minimum va Maksimum oid masalalar

# 1 - masala
#Minmax1. N natural soni va n ta sonlar to'plami berilgan.
# Kiritilgan to'plamdagi eng katta va eng kichik sonni topuvchi programma tuzilsin.
m = int(input('Son kiriting min va max uchun: '))
n = int(input('N butun son kiriting: '))
max_num = m
min_num = m
for i in range(n):
    num = int(input("Toplam sonlarni kiriting: "))
    if num < min_num:
        min_num = num
        print(min_num)
    if num > max_num:
        max_num = num


print(f"Eng katta son: {max_num}")
print(f"Eng kichik son: {min_num}")


# 2 - masala
# Minmax2. N natural soni va n ta to'g'ri burchakli to'rtburchak tomonlarining (a, b) to'plami berilgan.
# Kiritilgan to' plamdagi eng kichik yuzali to'rtburchakni topuchi programma tuzilsin.

m = float(input('Area ni kiritng: '))
n = int(input('N butun son kiriting: '))

for i in range(n):
    a = float(input('a ni kiriting: '))
    b = float(input('b ni kiriting: '))

    area = a * b
    if area < m:
        min_area = area
print(f'Eng kichik area: {min_area}')


# 3 - masala
# Minmax3. N natural soni va n ta to'g'ri burchakli to'rtburchak tomonlarining (a, b) to'plami berilgan.
# Kiritilgan to'plamdagi eng katta perimetri to'rtburchakni topuvchi programma tuzilsin.

p = float(input('Perimetrni kiriting: '))
n = int(input('N butun son kiriting: '))

for i in range(n):
    a = int(input('A ni kiriting: '))
    b = int(input('B ni kiriting: '))
    perimetr = 2 * (a + b)
    if perimetr > p:
        p = perimetr

print('Eng katta togri tortburchak perimetr: ', p)


# 4 - masala
# Minmax4. N natural soni va n ta sonlar to'plami berilgan. Kiritilgan to'plamdagi eng kichik element
# o'rnini aniqlovchi programma tuzilsin.

n = input("To'plamni kiriting: ")
n = list(map(int, n.split()))

eng_kichik = n[0]  # Boshlang'ich qiymatni eng kichik deb olamiz
for element in n:
    if element < eng_kichik:
        eng_kichik = element

# Eng kichik elementni chiqarish
print("Eng kichik element:", eng_kichik)


# 5 - masala
# Minmax5. N natural soni va n ta (m, v) sonlar juftligi to'plami berilgan. (m - og'irlik, v - haim). Kiritilgan
# to'plamdagi eng katta zichlikni aniqlovchi programma tuzilsin. Zichlik - og'irlikni haimga nisbatiga teng.

n = int(input('N juftlik son kiriting: '))
toplam = []
for i in range(n):
    m = int(int(input('Ogirlikni kiriting: ')))
    v = int(input('Xajmini kiriting: '))
    toplam.append((m, v))
    print('toplam m va v:', toplam)

s = 0 # eng katta zichlik
for m, v in toplam:
    zichlik = m / v
    print('Zichligi', zichlik)
    if zichlik > s:
        s = zichlik
print('Eng katta zichlik:', s)


# 6 - masala
# Minmax6. N natural soni va N ta butun sondan iborat to'plam berilgan. Birinchi uchragan eng kichik va
# oxirgi uchragan eng katta element tartib raqamini aniqlovchi programma tuzilsin.

n = int(input('Butun son kiriting: '))
toplam = []
for i in range(n):
    element = int(input(f"{i+1}-chi element kiriting: "))
    toplam.append(element)
    print('toplam_apend:', toplam)

max_el = 0
min_el = 0
for i in range(1, n):
    print('bu i', i)
    if toplam[i] < toplam[min_el]:
        min_el = i
        print('min_el:', min_el)
    if toplam[i] > toplam[max_el]:
        max_el = i
        print('max_el:', max_el)

print("Birinchi uchragan eng kichik element tartib raqami:", min_el + 1)
print("Oxirgi uchragan eng katta element tartib raqami:", max_el + 1)


# 7 - masala
# Minmax7. N natural soni va N ta butun sondan iborat to'plam berilgan. Birinchi uchragan eng katta va
# oxirgi uchragan eng kichik element tartib raqamini aniqlovchi programma tuzilsin.

n = int(input('Butun son kiriting: '))
toplam = []
for i in range(n):
    element = int(input(f"{i+1}-chi element kiriting: "))
    toplam.append(element)
    print('toplam_apend:', toplam)

max_el = 0
min_el = 0
for i in range(1, n):
    print('bu i', i)
    if toplam[i] > toplam[max_el]:
        max_el = i
        print('min_el:', max_el)
    if toplam[i] < toplam[min_el]:
        min_el = i
        print('max_el:', min_el)

print("Birinchi uchragan eng katta element tartib raqami:", max_el + 1)
print("Oxirgi uchragan eng kichik element tartib raqami:", min_el + 1)


# 8 - masala
# Minmax8. N natural soni va N ta butun sondan iborat to' plam berilgan. Birinchi va oxirgi uchragan eng
# kichik element tartib raqamini aniqlovchi programma tuzilsin.

n = int(input('Butun son kiriting: '))
toplam = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    toplam.append(element)
    print('toplam_element: ', toplam)

min_el = 0
max_el = n - 1
print('max_el1, ', max_el)
for i in range(1, n):
    print('bu i', i)
    if toplam[i] < toplam[min_el]:
        print('Nima edi bu min, ', toplam[min_el])
        print('bu i min,', toplam[i])
        min_el = i
        print('bu min', min_el)
    if toplam[i] < toplam[max_el]:
        print('Nima edi bu max, ', toplam[min_el])
        print('bu i max ,', toplam[i])
        max_el = i
        print('bu max', max_el)

print('Birinchi uchragan eng kichik element tartib raqami: ', min_el)
print('Oxirgi uchragan eng kich element tartib raqami: ', max_el)


# 9 - masala
# Minmax9. N natural soni va N ta butun sondan iborat to'plam berilgan. Birinchi va oxirgi uchragan eng
# katta element tartib raqamini aniqlovchi programma tuzilsin.

n = int(input('Butun son kiriting: '))
toplam = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    toplam.append(element)
    print('toplam_element: ', toplam)


max_el = 0
print('max_el1, ', max_el)
for i in range(1, n):
    print('bu i', i)
    if toplam[i] > toplam[max_el]:
        print('Nima edi bu max, ', toplam[max_el])
        print('bu i max,', toplam[i])
        max_el = i
        print('bu min', max_el)
print('Birinchi uchragan eng katta element tartib raqami: ', max_el + 1)
print('Oxirgi uchragan eng katta element tartib raqami: ', n)


# 10 - masala
# Minmax10. N natural soni va N ta butun sondan iborat to'plam berilgan. Birinchi uchragan ekstremal
# element tartib ragamini aniqlovchi programma tuzilsin. Ekstremal element deb eng katta yoki eng kichik
# elementga aytiladi
n = int(input('n butun son kiriting: '))
toplam = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    toplam.append(element)
    print('Bu toplam_el', toplam)

ekstremal_element = 0
for i in range(1, n):
    if toplam[i] > toplam[ekstremal_element] or toplam[i] > toplam[ekstremal_element]:
        ekstremal_element = i

print("Birinchi uchragan ekstremal element tartib raqami:", ekstremal_element + 1)


# 11 - masala
# Minmax11. N natural soni va N ta butun sondan iborat to'plam berilgan. Oxirgi uchragan ekstremal
# element tartib ragamini aniglovchi programma tuzilsin. Ekstremal element deb eng katta yoki eng kichik
# elementga avtiladi.

n = int(input('N butun son kiriting: '))
toplam = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    toplam.append(element)

ekstremal_element = max(toplam)
print('Bu ekstremal element: ', ekstremal_element)
last_element = 0
for i in range(len(toplam)-1, -1, -1):
    print('Bu i loop: ', i)
    if toplam[i] == ekstremal_element:
        print('bu toplam[i]: ', toplam[i], 'ekstremal_element:', ekstremal_element)
        last_element = i + 1
        print('Bu last_element:', last_element)
        # break
print('Oxirgi ekstremal elementi :', last_element)

# toplam = [123, 324, 563, 12, 34, 543, 134]
# ekstremal_element = max(toplam)
# print('Bu ekstremal element: ', ekstremal_element)
# last_element = 0
# for i in range(len(toplam)-1, -1, -1): # agar -1 1ta bolsa - oxirgi indeksni chiqarmidi
#     print('Bu i loop: ', i) # agar -1 3 ta bolsa - teskari tartibda chiqaradi



# 12 - masala
# Minmax12. N natural soni va N ta butun sondan iborat to'plam berilgan. Eng kichik musbat sonni
# aniqlovchi programma tuzilsin. Agar musbat son bo'lmasa nol chiqarilsin.

n = int(input('N butun son kiriting: '))
toplam = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    toplam.append(element)

eng_kichik = 0
print('bu eng_kichik: ',eng_kichik)
for i in toplam:
    print('bu i loop,', i)
    if i > 0 or i < eng_kichik:
        eng_kichik = i
        print('bu eng_kichigini oladi:', i)

if eng_kichik < 0:
    print(f"musbat son emas {0}")
else:
    print('Eng kichik musbat soni:', eng_kichik)



# 13 - masala
# Minmax13. N natural soni va N ta butun sondan iborat to'plam berilgan. Birinchi uchragan eng katta toq
# element tartib ragamini aniglovchi programma tuzilsin. Agar toq son bo'lmasa nol chigarilsin.
n = int(input('N butun son kiriting: '))
toplam = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    toplam.append(element)

eng_katta_toqson = 0
index = 0
for i in range(len(toplam)):
    print('bu i', i)
    if toplam[i] % 2 != 0:
        print('Bu toplam[i]', toplam[i])
        eng_katta_toqson = toplam[i]
        print('eng_katta_toqson,', eng_katta_toqson)
        index = i
        break

if eng_katta_toqson % 2 == 0:
    print(f'Toq son emas {0}')
else:
    print('Birinchi uchragan eng katta toq son', index)



# 14 - masala XATO False
# Minmax14. B soni va 10 ta butun sondan tashkil topgan musbat sonlar to'plami berilgan. Shu
# to'plamda B sonidan katta bo'lgan, eng kichik elementni tartib raqamini chiqaruvchi programma tuzilsin.
# Agar berilgan to'plamda B sonidan katta son topilmasa, ikkita 0 chigarilsin.

b = int(input('Butun son kiriting: '))
toplam = []
for i in range(10):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    toplam.append(element)

eng_kichik_element = float('inf')
k = 0
for i in range(len(toplam)):
    print('Bu i', i)
    if toplam[i] > b and toplam[i] < eng_kichik_element:
        print('BU toplam[i],', toplam[i], 'bu eng_kichik,', eng_kichik_element)
        eng_kichik_element = toplam[i]
        print('BU qoldq eng kich el:', eng_kichik_element)
        index = i + 1
        print('Bu index: ', index)
        break
if eng_kichik_element == float('inf'):
    print(0, 0)
else:
    print('B sonidan katta bolgani. Eng kichik tartib raqami:', k)



# 15 - masala
# Minmax15. B, C sonilari va 10 ta butun sondan tashkil topgan to'plam berilgan (0 < B < C). Shu
# to'plamda (B, C) oraligdagi eng katta elementni tartib ragamini chigaruvchi programma tuzilsin. Agar
# berilgan to'plamda (B, C) oraliqda son topilmasa, ikkita 0 chiqarisin

b = int(input('B butun son kiriting: '))
c = int(input("C butun son kiriting: "))
toplam = []
for i in range(10):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    toplam.append(element)

eng_katta_son = 0
k = 0
for i in range (len(toplam)):
    if toplam[i] > b and toplam[i] < c:
        print('toplam[i],', toplam[i], 'bu c', c)
        eng_katta_son = i
        print('eng katta son:', eng_katta_son)
        k = i + 1
        print('k', k)
if eng_katta_son < 0:
    print(0, 0)
else:
    print('B va C ni orasidagi eng katta son:', k)


# 16 - masala 50/50
# Minmax16. N natural soni va N ta butun sondan iborat to'plam berilgan. Birinchi uchragan eng kichik
# elementgacha bo' lgan elementiar sonini aniglovchi programma tuzilsin.
n = int(input('N butun son kiriting: '))
toplam = []
for i in range(n):
    element = int(input(f'{i+1}-chi elementni kiriting: '))
    toplam.append(element)

eng_kichik_el = min(toplam)
print('Bu eng kichik el:', eng_kichik_el)
s = []
for i in range(2, eng_kichik_el + 1):
    print('Bu i,', i)
    is_s = True
    for j in range(2, int(i ** 0.5) + 1):
        print('bu j,', j)
        if i % j == 0:
            print('bu i va j', i, j)
            is_s = False
            print('Bu is_s,', is_s)
            break
    if is_s:
        s.append(i)
        print('bu s: ', s)
print('Birinchi eng kichik elelementi: ', s)


# 17 - masala False XATO
# Minmax17. N natural soni va N ta butun sondan iborat to'plam berilgan. Oxirgi uchragan eng katta
# elementdan keyin turgan elementlar sonini aniqlovchi programma tuzilsin.
n = int(input('N butun son kiriting: '))
toplam = []
for i in range(n):
    element = int(input(f'{i+1}-chi elementni kiriting: '))
    toplam.append(element)

eng_katta_el = toplam[-1]
print('Bu eng katta el:', eng_katta_el)
s = 0
for i in toplam:
    if i > eng_katta_el:
        s += 1
print("Elementlani soni", s)


# 18 - masala
# Minmax18. N natural soni va N ta butun sondan iborat to'plam berilgan. Birinchi va oxirgi uchragan eng
# katta element orasida turgan elementlar sonini aniqlovchi programma tuzilsin. Agar to'plamda fagat
# bitta eng katta element bo'lsa, nol chigarilsin.

n = int(input('N butun son kiriting: '))
toplam = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiritng: "))
    toplam.append(element)

largest_number = max(toplam)
print('Largest number', largest_number)
first_index = toplam.index(largest_number)
print('first_index', first_index)
last_index = len(toplam) - 1 - toplam[::-1].index(largest_number)
print('last_index', last_index, '\n', 'bu toplam.index', toplam.index(largest_number), '\n', 'bu len(toplam)', len(toplam))
count = last_index - first_index - 1
print('count', count)

if count < 1:
    print("0")
else:
    print('Birinchi va Oxirgi uchragan eng katta element orasida turgan element:', count)


# 19 - masala
# Minmax19. N natural soni va N ta butun sondan iborat to'plam berilgan. To'plamdagi eng kichik
# elementlar sonini aniqlovchi programma tuzilsin.

n = int(input('N butun son kiriting: '))
toplam = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    toplam.append(element)

smallest_element = min(toplam)

print('Eng kichik element soni:', smallest_element)


# 20 - masala  50/50
# Minmax20. N natural soni va N ta butun sondan iborat to'plam berilgan. To'plamdagi ekstremal
# elementlar sonini aniqlovchi programma tuzilsin. Ekstremal element deb eng katta yoki eng kichik
# elementga aytiladi.

n = int(input('N butun son kiriting: '))
toplam = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    toplam.append(element)


ekstremal_katta = float('inf')
ekstremal_kichik = float('-inf')

for i in toplam:
    if i > ekstremal_katta:
        ekstremal_katta = i
    if i < ekstremal_kichik:
        ekstremal_kichik = i

print(f"Ekstremal sonlar soni: {toplam.count(ekstremal_katta) + toplam.count(ekstremal_kichik)}")



# 21 - masala
# Minmax21. N natural soni va N ta butun sondan iborat to'plam berilgan (N > 2). To'plamning o'rtacha
# qiymatini aniqlovchi programma tuzilsin. O'rtacha qiymatni hisoblashda eng katta va eng kichik
# qiymatlar hisobga olinmasin.
n = int(input('N - butun son kiriting: '))
toplam = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    toplam.append(element)

total = sum(toplam)
print('total,', total)

eng_katta = max(toplam)
print('eng_katta:', eng_katta)
eng_kichik = min(toplam)
print('eng_kichik:', eng_kichik)

ortacha = (total - eng_katta - eng_kichik) / (n / 2)
print('ortacha', ortacha)


# 22 - masala
# Minmax22. N natural soni va N ta butun sondan iborat to'plam berilgan (N > 2). To'plamdagi eng kichik
# 2 ta qiymatni aniqlovchi programma tuzilsin.
# Masalan: N = 5; 123 4 5
# Natija: 1 2
n = int(input('N butun son kiriting: '))
toplam = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    toplam.append(element)

eng_kichik1 = min(toplam)
toplam.remove(eng_kichik1)

eng_kichik2 = min(toplam)

print('Eng kichik 2 ta qiymat', eng_kichik1, 'va', eng_kichik2)


# 23 - masala
# Minmax23. N natural soni va N ta butun sondan iborat to'plam berilgan (N > 3), To'plamdagi eng katta
# 3 ta qiymatni aniglovchi programma tuzilsin.
# Masalan: N = 5; 1234 5
# Natija: 5 4 3

n = int(input('N butun son kiriting: '))
toplam = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    toplam.append(element)

eng_katta1 = max(toplam)
toplam.remove(eng_katta1)

eng_katta2 = max(toplam)
toplam.remove(eng_katta2)

eng_katta3 = max(toplam)

print('Eng katta 3 ta qiymat', eng_katta1, 'va', eng_katta2, 'va', eng_katta3)


# 24 - masala
# Minmax24. N natural soni va N ta butun sondan iborat to'plam berilgan (N > 1). Ikkita go'shni son
# yig'indisining eng katta giymatni aniglovchi programma tuzilsin.

n = int(input('N butun son kiriting: '))
toplam = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting:" ))
    toplam.append(element)

max_yegin = 0
for i in range(n - 1):
    print('bu i:', i)
    for j in range(i + 1, n):
        print('bu j:', j)
        yegindi = toplam[i] + toplam[j]
        print('bu yegindi', yegindi)
        if yegindi > max_yegin:
            max_yegin = yegindi

print('Ikkita qoshni sonni yegindisi:', max_yegin)


# 25 - masala
# Minmax25. N natural soni va N ta butun sondan iborat to'plam berilgan (N > 1). Ko'paytmasi eng kichik
# bo'ladigan ikkita go'shni element indekslarini aniglovchi programma tuzilsin.
n = int(input('N butun son kiriting: '))
toplam = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    toplam.append(element)

eng_kichik_kopaytmasi = 0


# 26 - masala
# Minmax26. N natural soni va N ta butun sondan iborat to'plam berilgan. To'plamda ketma - ket
# keladigan juft elementlar maksimal sonini aniqlovchi programma tuzilsin. Agar to'plamda juft sonlar
# bo'lmasa, 0 chiqarilsin.


n = int(input('N butun son kiritng: '))
toplam = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    toplam.append(element)

max_element = 0
juft_element = False
for i in range(n):
    print('bu i:', i)
    for j in range(i + 1, n):
        print('bu j', j)
        if toplam[i] % 2 == 0 and toplam[j] % 2 == 0:
            if toplam[i] * toplam[j] > max_element:
                print('bu toplam i,', toplam[i], '\n', 'bu toplam j,', toplam[j])
                max_element = toplam[i] * toplam[j]
                print('bu max_element: ', max_element)
                juft_element = True

if juft_element:
    print('Maksimal juft sonini elementlari:', max_element)
else:
    print(0)



# 27 - masala
# Minmax27. N natural soni va N ta nol va birdan iborat to plam berilgan. Bir xil sonlar ketma - ketligi eng
# uzun bo'ladigan oraliq boshlangan element indeksini va ketma - ketlikdagi elementlar sonini aniqlovchi
# programma tuzilsin.

n = int(input('N butun son kiritng: '))
toplam = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiritng: "))
    toplam.append(element)

max_lenth = 0
max_index = 0
current_lenth = 1
for i in range(1, n):
    if toplam[i] == toplam[i-1]:
        print('bu toplam i:', toplam[i], 'and', toplam[i-1])
        current_lenth += 1
        print('current', current_lenth)
    else:
        if current_lenth > max_lenth:
            max_lenth = current_lenth
            print('max_lenth:', max_lenth)
            max_index = i - max_lenth
            print('max_index', max_index)
        current_lenth = 1
        print('current_lenth:', current_lenth)

if current_lenth > max_lenth:
    max_lenth = current_lenth
    print('bu max lenth:', max_lenth)
    max_index = n - max_lenth
    print('bu n max_index:', max_index)

if max_lenth > 1:
    print('Eng uzun ketma ketlik boshlangan indeksi: ', max_index)
    print('Ketma ketlikdagi elementlar soni:', max_lenth)
else:
    print('Ketma ketlik topilmadi!')



# 28 - masala
# Minmax28. N natural soni va N ta nol va birdan iborat to'plam berilgan. Bir soni ketma - ketligi eng
# uzun bo'ladigan oraliq boshlangan element indeksini va ketma - ketlikdagi elementlar sonini aniglovchi
# programma tuzilsin. Agar toplamda bir soni uchramasa nol chigarilsin.

n = int(input('N butun son kiritng: '))
toplam = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiritng: "))
    toplam.append(element)

max_lenth = 0
max_index = 0
current_lenth = 1

for i in range(1, n):
    if toplam[i] == toplam[i-1]:
        print('bu toplam[i]', toplam[i], 'and', 'bu toplam[i-1]', toplam[i-1])
        current_lenth += 1
    else:
        if current_lenth > max_lenth:
            max_lenth = current_lenth
            max_index = i - max_lenth
        current_lenth = 1

if current_lenth > max_lenth:
    max_lenth = current_lenth
    max_index = n - max_lenth

if max_lenth > 1:
    print('Eng uzun ketma ketlik boshlangan indeksi: ', max_index)
    print('Ketma ketlikdagi elementlar soni:', max_lenth)
else:
    print(0)



# 29 - masala
# Minmax29. N natural soni va N ta butun sondan iborat to'plam berilgan.
# To'plamdagi ketma - ket keladigan eng kichik elementlarning maksimal sonini aniqlovchi programma
# tuzilsin.
n = int(input('N butun son kiriting: '))
toplam = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    toplam.append(element)

min_index = float('inf')
max_number = 0
for i in range(n - 1):
    print('bu i:', i)
    for j in range(i + 1, n):
        print('bu j:', j)
        index = abs(toplam[i] - toplam[j])
        print('bu index:', index)
        number = toplam[i] * toplam[j]
        print('bu number:', number)
        if index < min_index or (index == min_index and number > max_number):
            min_index = index
            print('min_index:', min_index)
            max_number = number
            print('max_number:', max_number)

if min_index != float('inf'):
    print('Ketma ket keladigan eng kichik elementlarni maksimal soni:', max_number)
else:
    print('Ketma ket keladigan element topilmadi!')


# 30 - masala
# Minmax30. N natural soni va N ta butun sondan iborat to'plam berilgan. To'plamdagi ketma - ket
# keladigan eng katta elementlarning minimal sonini aniglovchi programma tuzilsin.

n = int(input('N butun son kiriting: '))
toplam = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: " ))
    toplam.append(element)

max_index_minim = 0

for i in range(n - 1):
    print('bu i-', i)
    s = abs(toplam[i] - toplam[i+1])
    print('bu abs-', abs(toplam[i] - toplam[i+1]))
    print('bu s-', s)
    if s > max_index_minim:
        max_index_minim = s
        print('bu max-', max_index_minim)

print('Ketma ket keladigan eng katta elementning minimal soni:', max_index_minim)
