# 10 - Mavzu. Bir o'lcahmli massivla bilan ishlash

# 1. Massiveni hosil qilish va elementlarini kiritish



# 1 - masala
# n natural soni berilgan. Dastlabki n ta toq sondan tashkil topgan massivni hosil qiling va
# elementlarini chiqaring.
n = 5
odd_array = []
num = 1

while len(odd_array) < n:
    odd_array.append(num)
    num += 2

print(odd_array)


# 2 - masala
# n natural soni berilgan. 2 sonining dastlabki n ta darajasidan tashkil topgan massivni hosil
# qiling va elementlarini chiqaring. (1, 2, 4, 8, ....)
# with arr
n = int(input('Daraja son kiriting: '))
arr = []
s = 1
for i in range(n):
    result = 2 ** i
    arr.append(result)
print('Result', arr[-1:])

# without array
n = int(input('Daraja son kiriting: '))
s = 1
for i in range(1, n):
    s *= 2
    print(s)
print('Result', s)



# 3 - masala
# n natural soni va arifmetik progressiyaning dastlabki hadi A va ayirmadi D berilgan. Arifmetik
# progressiyaning dastlabki n ta hadidan tashkil topgan massivni hosil qiling va elementlarini chiqaring.
# Ai = Ai-1 + D
n = int(input('N: '))  # 5
A = int(input('A: '))  # 1
D = int(input('D: '))  # 3
progression_array = [A]

for i in range(1, n):
    next_a = progression_array[i-1] + D
    progression_array.append(next_a)

print(progression_array)


# 4 - masala
#  n natural soni va geometrik progressiyaning dastlabki hadi A va maxraji D berilgan. Geometrik
# progressiyaning dastlabki n ta hadidan tashkil topgan massivni hosil qiling va elementlarini chiqaring.
# Ai = Ai-1 * D
n = int(input('N: '))
A = int(input('A: '))
D = int(input('D: '))
progression_arr = [A]

for i in range(1, n):
    next_a = progression_arr[i-1] * D
    progression_arr.append(next_a)

print(progression_arr)


# 5 - masala
# n natural soni berilgan. Dastlabki n ta Fibonachchi sonlaridan tashkil topgan massivni hosil
# qiling va elementlarini chiqaring.
# FO = 1; F1 = 1; F[k] = F[k-1] + F[k-2], k = 2, 3, 4, ...
#
n = int(input('N: '))
fib = [1, 1]
for i in range(2, n):
    print('i', i)
    fib.append(fib[i-1] + fib[i-2])
    print('fib[i-1]', fib[i-1] + fib[i-2])
    print('fib', fib)

print('Fibonachi:', fib[:n])


# 6 - masala
# n natural soni va A, B butun sonlari berilgan (n > 2). a[0] = A; a[1] = B; boshqa elementlari
# o'zidan oldingi barcha elementlari yig' indisiga teng bo'lgan massivni hosil qiling va elementlarini
# chiqaring.
n = int(input('N: '))
A = int(input('A: '))
B = int(input('B: '))
arr = [A, B]
for i in range(2, n):
    arr.append(sum(arr[:i]))
    print('arr[:i]', arr[:i])

print('Yegindisi:', arr)

# solve without sum libraries
n = int(input('N: '))
A = int(input('A: '))
B = int(input('B: '))
arr = [A, B]
s = 0

for i in range(2, n):
    s = 0
    print('ssss', s)
    for j in range(i):
        print('j', j)
        s += arr[j]
        print('s', s)
    arr.append(s)
print('arr', arr)


# 7 - masala
#  n ta elementdan tashkil topgan massiv berilgan. Uning elementlarini teskari tartibda
# chiqaruvchi programma tuzilsin.
n = int(input('N: '))
arr = []

for i in range(n):
    element = int(input(f"{i+1}- chi elementni kiriting: "))
    arr.append(element)

# arr.reverse()

# for i in arr:
#     # print('i', i)
#     print('Teskari tartib - ', arr)

# solve without revelese library
for i in range(n-1, -1, -1):
    # print('i', i)
    print('Teskari tartib - ', arr[i])


# 8 - masala False
# n ta elementdan tashkil topgan massiv berilgan. Massiv elementlari orasidan toglarini
# indekslari o'sish tartibida chiqaruvchi va ularning sonini chigaruvchi programma tuzilsin.
# Massiv elementlar: 4 5 7 8 6 9
# Natija: 5 7 9 toglar soni = 3
n = int(input('N: '))
toqlar = []

for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    toqlar.append(element)

count = 0




# 9 - masala
# n ta elementdan tashkil topgan massiv berilgan. Massiv elementlari orasidan juftlarini indekslari
# kamayish tartibida chiqaruvchi va ularning sonini chiqaruvchi programma tuzilsin.
# Massiv elementlar: 4 5 7 8 6 9
# Natija: 6 8 4 juftlar soni = 3
n = int(input('N: '))
juft = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    juft.append(element)


count = 0
for i in range(n-1, -1, -1):
    if juft[i] % 2 == 0:
        print(juft[i], end=" ")
        count += 1


print('Juftliklar soni:', count)


# 10 - masala

n = int(input('N: '))
arr = []

for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    arr.append(element)


toqlar = []
juftlar = []

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        juftlar.append(arr[i])
        print('juft-', juftlar)
    else:
        toqlar.append(arr[i])
        print('toqlar-', toqlar)

natija = juftlar + toqlar[::-1]
print('toq', toqlar[::-1])


print("Natija:", ' ', natija)



# 11 - masala solve without ::

n = int(input('N: '))
K = int(input('K: '))
arr = []

for i in range(n):
    element = int(input(f"{i+1}-chi element: "))
    arr.append(element)

result = arr[K-1::K]
print('result-', result)


# solve without [::]
n = int(input('N: '))
K = int(input('K: '))
arr = []

for i in range(n):
    element = int(input(f"{i+1}-chi element: "))
    arr.append(element)

result = []
index = K - 1
print('index', index)

while index < n:
    result.append(arr[index])
    print('result', result)
    index += K
    print('in', index)

print('result', result)


# 12 - masala Falsce without ::
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f"{i+1}-chi element juftlarini kiriting: "))
    arr.append(element)

result = arr[::2]
print('Result:', result)

# 13 - masala False without ::
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f"{i+1}-chi element toqlarini kiriting: "))
    arr.append(element)

result = arr[::-2]
print('Result:', result)


# 14 - masala False ::
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    arr.append(element)

result = arr[1::2] + arr[::2]

print('result', result)


# 15 - masala False ::
n = int(input('N:'))
arr = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    arr.append(element)


result = arr[::2] + arr[-1::-2]
print('arr', arr[::2])
print('arr2', arr[-1::-2])

print('result', result)


# 16 - masala True
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f'{i+1}-chi elementni kiriting: '))
    arr.append(element)

result = [arr[0], arr[n-1], arr[1], arr[n-2], arr[2], arr[n-3]]

#
print('Result:', result)


# 17 - masala True
n = int(input('N: '))
A = []
for i in range(n):
    element = int(input(f'{i+1}-chi elementni kiriting: '))
    A.append(element)

output = [A[0], A[1], A[n-1], A[n-2], A[3], A[4], A[n-3], A[n-4]]
print(output)

# 2. Massive elementlarini taxlil qilish

# 18 - masala

# 18 - masala
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    arr.append(element)

if len(arr) > 1:
    result = min(arr[:-1])
else:
    result = 0

print('Result:', result)


# 19 - masala
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f"{i+1}-cho elementni kiriting: "))
    arr.append(element)

if len(arr) > 2:
    natija = max(i for i in range(1, len(arr)-1) if arr[i] > arr[0] and arr[i] < arr[-1])
else:
    natija = 0

print("Result:", natija)


# 20 - masala
n = int(input('N: '))
K, L = int(input('K: ')), int(input('L: '))
arr = []
for i in range(n):
    element = int(input(f"{i+1}'s enter element > "))
    arr.append(element)


sum_element = sum(arr[K:L+1])
print('ar', arr[K:L])
print('sum', sum_element)


# 21 - masala
n = int(input('N: '))
K, L = int(input('K: ')), int(input('L: '))
arr = []
for i in range(n):
    element = int(input(f"{i+1}'s enter element > "))
    arr.append(element)

sum_element = 0
count = 0
for i in range(K, L+1):
    sum_element += arr[i]
    print('sum-', sum_element)
    count += 1
    print('count', count)

orta_arifmettika = sum_element / count
print(orta_arifmettika)


# 22 - masala
n = int(input('N: '))
K, L = int(input('K: ')), int(input('L: '))
arr = []
for i in range(n):
    element = int(input(f"{i+1}'s enter element > "))
    arr.append(element)


sum_element = sum(arr[:K]) + sum(arr[L+1:])
print('sum1', sum(arr[:K]), 'sum2', sum(arr[L+1:]))
print('sum_elemt tashqari: ', sum_element)


# 23 - masala
n = int(input('N: '))
K, L = int(input('K: ')), int(input('L: '))
arr = []
for i in range(n):
    element = int(input(f"{i+1}'s enter element > "))
    arr.append(element)


s = arr[K+1:L]
print(s)
orta_arifmetika = sum(s) / len(s)

print('orta arifmetika:', orta_arifmetika)


# 24 - masala
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f"{i+1}'s enter element > "))
    arr.append(element)

diff = arr[1] - arr[0]
aks_holda = diff < 0
if aks_holda:
    diff *= -1
else:
    diff = 0

print(diff)


# 25 - masala
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f"{i+1}'s enter element > "))
    arr.append(element)

maxraj = arr[1] / arr[0]
aks_holda = maxraj < 1
if aks_holda:
    maxraj = 0

print(maxraj)


# 26 - masala 50/50
n = int(input("N: "))
array = []

for i in range(n):
    num = int(input("Enter element {}: ".format(i+1)))
    array.append(num)


ketmaket = True
for i in range(n-1):
    if array[i] % 2 == array[i+1] % 2:
        print('arr[i]%2', array[i] % 2 == array[i+1] % 2)
        ketmaket = False
        print('js', ketmaket)
        break

if ketmaket:
    print("0")
else:
    for i in range(n-1):
        print('i', i)
        if array[i] % 2 == array[i+1] % 2:
            print("Birinchi buzilgan index elementi", i+1)
            break


# 27 - masala
n = int(input("N: "))
array = []

for i in range(n):
    num = int(input("Enter element {}: ".format(i+1)))
    array.append(num)


# manfiy va musbat arrayni ketma ketlik tekshirish
ketmaket = True
for i in range(n-1):
    print('i', i)
    if array[i] >= 0 and array[i+1] >= 0:
        print('arr[i]arr[i+1]', array[i] >= 0 and array[i+1] >= 0)
        ketmaket = False
        break

    if array[i] < 0 and array[i+1] < 0:
        print('arr<0 arr[i+1]<0', array[i] < 0 and array[i+1] < 0)
        ketmaket = False
        break

if ketmaket:
    print('0')
else:
    for i in range(n-1):
        if(array[i] >= 0 and array[i+1] >= 0) or (array[i] < 0 and array[i+1] < 0):
            print('ketma ketlikni buzgan birinchi element indeksi', i+1)
            break



# 28 - masala
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input('Enter element {}: ' .format(i+1)))
    arr.append(element)

min_value = float('inf')
for i in range(0, n, 2):
    if arr[i] < min_value:
        min_value = arr[i]
print('Result', min_value)


# 29 - masala

n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input('Enter element {}: ' .format(i+1)))
    arr.append(element)

max_value = float('-inf')
for i in range(1, n, 2):
    if arr[i] > max_value:
        max_value = arr[i]

print('Max number', max_value)


# 30 - masala True
n = int(input("N: "))
array = []


for i in range(n):
    num = int(input("Butun son kiriting {}: ".format(i+1)))
    array.append(num)

max_index = -1
max_count = 0


for i in range(n):
    if array[i] > array[max_index]:
        max_index = i
        max_count = 1
    elif array[i] == array[max_index]:
        max_count += 1


for i in range(n):
    if array[i] == array[max_index]:
        print(i)

print("Maksimum element:", max_count)


# 31 - masala
n = int(input('N: '))
arr = []

for i in range(n):
    element = int(input(f"{i+1}-chi element: "))
    arr.append(element)

max_index = -1
max_element = float('-inf')
count = 0

for i in range(n):
    if arr[i] > max_element:
        max_element = arr[i]
        max_index = i
        count = 1
    elif arr[i] == max_element:
        count += 1

result = []
for i in range(max_index - 1, -1, -1):
    if arr[i] == arr[max_index]:
        result.append(i)

result.sort()
print("Indeks kamayish tartibida:", result)
print("Ularning soni:", len(result))


# 32 - masala
n = int(input('N: ')) # 7
arr = []

for i in range(n):
    element = int(input(f"{i+1}-chi element: ")) # 65,432,24,56,645,213,53 --> 24
    arr.append(element)

index = -1
for i in range(1, n-1):
    print('i', i)
    if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
        print('arr[i-1]', arr[i-1])
        index = i
        print('index', index)
        break
print('Local minimum index:', index)


# 33 - masala
n = int(input('N: ')) # 7
arr = []

for i in range(n):
    element = int(input(f"{i+1}-chi element: ")) # 65,432,24,56,645,213,53 --> 24
    arr.append(element)

index = -1
for i in range(1, n-1):
    print('i', i)
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        print('arr[i-1]', arr[i-1])
        index = i
        print('index', index)
print('Local minimum index:', index)


# 34 - masala True
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f'{i+1} - '))
    arr.append(element)

largest_local_min = None

for i in range(1, len(arr) - 1):
    if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
        if largest_local_min is None or arr[i] > largest_local_min:
            largest_local_min = arr[i]
if largest_local_min is not None:
    print("Katta local minimum:", largest_local_min)
else:
    print("local minimum topilamdi.")

# 35 - masala True
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f"{i+1} - > "))
    arr.append(element)

larget_local_max = None

for i in range(1, n-1):
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        if larget_local_max is None or arr[i] < larget_local_max:
            larget_local_max = arr[i]
            print('max', larget_local_max)

if larget_local_max is not None:
    print("Katta local maximum:", larget_local_max)
else:
    print("local maximum topilamdi.")
print("Katta lokal maksimum:", larget_local_max)


# 36 - masala
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f'{i+1} -- > '))
    arr.append(element)

katta_element = arr[1]

for i in range(1, n):
    if arr[i] > katta_element:
        katta_element = arr[i]

kichik_element = arr[-1]

for i in range(n):
    if arr[i] != kichik_element:
        if katta_element is None or arr[i] > kichik_element:
            s = arr[i]

if kichik_element is None:
    s = 0

print("Katta lokal extrem:", s)


# 37 - masala
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f"{i+1} --> ")) # 4,5,7,2,6,1,8,3
    arr.append(element)

increase = 0

for i in range(1, len(arr) - 1):
    if (arr[i] > arr[i-1] and arr[i] > arr[i+1]) or (arr[i] < arr[i-1] and arr[i] < arr[i+1]): # 5>4,5>7 or 5<4,5<7 = 7>5,7>2=2>7
        increase += 1
print("Monoton o'suvchi oraliqlar soni:", increase)


# 38 - masala
n = int(input('N: '))
arr = []
for i in range(n):
    elemenet = int(input(f"{i+1} -- > "))
    arr.append(elemenet)

count = 0
kamayuvchi = False

for i in range(1, len(arr)):
    if arr[i] < arr[i - 1]: # 5<4,7<5,2<7,6<2,1<6,8<1,3<8 = 3
        if not kamayuvchi:
            count += 1
            kamayuvchi = True
    else:
        kamayuvchi = False

print('Moton sonlar orasida kamayuvchis', count)


# 39 - masala
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f"{i+1} - > "))
    arr.append(element)

count = 0
oraliq = None

if len(arr) >= 2:
    oraliq = arr[1] - arr[0]
    print('oraliq', oraliq)

for i in range(2, len(arr)):
    new_trend = arr[i] - arr[i - 1]
    print('new_trend', new_trend)

    if new_trend != oraliq:
        count += 1
        print('coutn', count)
        oraliq = new_trend
        print('oraliq', oraliq)

print('Monoton oraliq soni', count)



# 40 - masala
n = int(input('N: '))
R = int(input('R: '))
arr = []
for i in range(n):
    element = int(input(f"{i+1} - "))
    arr.append(element)


yaqin_son = float('inf')
for num in arr:
    print('num', num)
    diff = abs(num - R)
    print('diff', diff)
    if diff < yaqin_son:
        yaqin_son = diff
        print('yaqin', yaqin_son)

print('Yaqin son', yaqin_son)

a = float('-inf')
b = float('inf')
c = 50
if c < a:
    print(a)
elif c > b:
    print(b)


# 41 - masala 50/50
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f"{i+1} --> "))
    arr.append(element)

max_number = max(arr)
element1 = None
element2 = None
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        s = arr[i] + arr[j]
        print('s', s)
        if s > max_number:
            max_number = s
            element1 = arr[i]
            element2 = arr[j]

if element1 is not None and element2 is not None:
    print("Ikkita elementni orasidagi yegindisi eng katta element qoshnisi:", element1, 'va', element2, '=', s)
else:
    print("Element topilmadi")


# 42 - masala
n = int(input('N: '))
R = int(input('R: '))
arr = []
for i in range(n):
    element = int(input(f"{i+1} --> "))
    arr.append(element)

closest_sum = max(arr)
element1 = 0
element2 = 0

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        current_sum = arr[i] + arr[j]
        diff = abs(current_sum - R)
        if diff < abs(closest_sum - R):
            closest_sum = current_sum
            element1 = arr[i]
            element2 = arr[j]

if element1 is not None and element2 is not None:
    print("Ikkita elementni R ni yegindisga yaqin 2 ta qoshni", R, "soniga:", element1, "va", element2)
else:
    print("Element topilmadi")


# 43 - masala
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f"{i+1} -- > "))
    arr.append(element)

count = 0
elements = None
for element in arr:
    if element != elements:
        count += 1

    elements = element
    print('element', elements)

print('Har hil qiymatdagi elementni soni', count)


# 44 - masala
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f'{i+1} --> '))
    arr.append(element)

index1 = None
index2 = None

for i in range(len(arr)): # 0,4

    for j in range(i+1, len(arr)): #1,5

        if arr[i] == arr[j]:
            index1 = i
            index2 = j
            break
    if index1 is None:
        break

print('2ta bir hil qiymat indekslar', index1, 'va', index2)


# 45 - masala
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f'{i+1} -- > '))
    arr.append(element)


min_element = min(arr)
qoshnilari = []
for i in range(len(arr) - 1):
    s = abs(arr[i+1] - arr[i])

    if s < min_element:
        print('s', s)
        min_element = s
        print('min_ele', min_element)
        qoshnilari = [i, i + 1]
        print('qosh', qoshnilari)
    elif s == min_element:
        print('sss',s)
        qoshnilari.append(i)
        print('qoshnilar', qoshnilari)
        qoshnilari.append(i + 1)
        print('qoshnilar2', qoshnilari)

print('Bir biriga eng yaqin qoshnilar indeksi', qoshnilari)


# 46 - masala
n = int(input('N:'))
R = int(input('R: '))
arr = []
for i in range(n):
    element = int(input(f'{i+1} -- > '))
    arr.append(element)


index1 = None
index2 = None

min_elem = max(arr)
min_elem1 = max(arr)

for i in range(len(arr)):
    s = abs(arr[i] - R)
    print('s', s)

    if s < min_elem:
        min_elem1 = min_elem
        index2 = index1
        print('index2', index2)
        min_elem = s
        print('min_elem', min_elem)
        index1 = i
        print('index1', i)
    elif s < min_elem1:
        min_elem1 = s
        index2 = i

print('R soni yegindisiga eng yaqin 2ta index', index1, 'va', index2)


# 47 - masala
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f'{i+1} -- > '))
    arr.append(element)


elements = []

for i in arr:
    if i not in elements:
        print('i', i)
        elements.append(i)
        print('element', elements)

for i in elements:
    print(i, end=' ')


# 48 - masala
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f'{i+1} -- > '))
    arr.append(element)

counts = 0
elements = None

for i in arr:
    count = arr.count(i)
    if count > counts:
        counts = count
        elements = i
        print('element', elements)


print('Eng kop qatnashgan bir hil qiymatli element soni:', counts)


# 49 - masala
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f'{i+1} -- > '))
    arr.append(element)


for i in range(len(arr)):
    if arr[i] != i + 1:
        print(i)
        break
else:
    print(0)


# 50 - masala

n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f'{i+1} -- > '))
    arr.append(element)

count = 0
for i in range(len(arr) - 1):
    if arr[i] > arr[i+1]:
        count += 1

print(count)


# 51 - masala
n = int(input('N: '))
print('A massive kiriting:')
a = []
for i in range(n):
    element = int(input(f'{i+1} - > '))
    a.append(element)

print('B massive kiriting:')
b =[]
for i in range(n):
    element = int(input(f'{i+1} -- > '))
    b.append(element)

for i in range(n):
    a[i], b[i] = b[i], a[i]

print('A massive', a)
print('B massive', b)
c = a
a = b
b = c

print('a', a)
print('b', b)


# 52 - masala
n = int(input('N: '))

print('A massive kiriting:')
a = []
for i in range(n):
    element = int(input(f'{i+1} -- > '))
    a.append(element)

print('B massive kiriting:')
b = []
for i in range(len(a)):
    if a[i] < 5:
        b.append(2 * a[i])
    else:
        b.append(a[i] / 2)

print('Result B massive', b)


# 53 - masala
n = int(input('N: '))
print('A massive kiriting:')
a = []
for i in range(n):
    element = int(input(f'{i+1} -- > '))
    a.append(element)

print('B massive kiriting:')
b = []
for i in range(n):
    element = int(input(f'{i+1} -- > '))
    b.append(element)

c = [max(a[i], b[i]) for i in range(len(a))]

print('Result C: ', c)


# 54 - masala
n = int(input('N: '))
a = []
for i in range(n):
    element = int(input(f'{i+1} --> '))
    a.append(element)

b = []
for i in range(1, len(a)):
    if i % 2 == 0:
        b.append(i)

print('Result B massive juftlari', b)


# 55 - masala
n = int(input('N: '))
a = []
for i in range(n):
    element = int(input(f'{i+1} -- > '))
    a.append(element)

b = []
for i in range(1, len(a)+1, 2):
    b.append(i)

print('B', b)


# 56 - masala
n = int(input('N: '))
a = []
for i in range(n):
    element = int(input(f'{i+1} --> '))
    a.append(element)

b = []
n = len(a)
i = 0
while i < n:
    b.append(i)
    i += 3

c = len(b)
print('Elementni soni: ', c)
print('B massive: ', b)


# 57 - masala 50/50
n = int(input('N: '))
a = []
for i in range(n):
    element = int(input(f'{i+1} --> '))
    a.append(element)

b = []
for i in range(2, len(a), 3):
    b.append(i)

print('Massive B', b)


# 58 - masala 50/50
n = int(input('N: '))
a = []
for i in range(n):
    element = int(input(f'{i+1} --> '))
    a.append(element)

b = [0] * n
print('b', b)

b[0] = a[0]
print('bbbb', b[0])

for k in range(1, n):
    print('k', k)
    b[k] = b[k-1] + a[k]
    print('b[k]', b[k])

print(b)


# 59 - masala 50/50
n = int(input('N: '))
a = []
for i in range(n):
    element = int(input(f'{i+1} --> '))
    a.append(element)

b = [0] * n
print('b', b)

b[0] = a[0]
print('bbbb', b[0])

for k in range(1, n):
    print('k', k)
    b[k] = b[k-1] + a[k] / k
    print('b[k]', b[k])

print(b)


# 60 - masala 50/50
n = int(input('N: '))
a = []
for i in range(n):
    element = int(input(f'{i+1} --> '))
    a.append(element)

b = []
for i in range(n):
    s = 0
    for j in range(i, n):
        print('j', j)
        s += a[j]
        print('sss', s)
    b.append(s)

print('B Massive:', b)


# 61 - masala
n = int(input('N: '))
a = []
for i in range(n):
    element = int(input(f'{i+1} --> '))
    a.append(element)

b = []
for k in range(n):
    arr = a[k:]
    s = sum(arr)
    orta_arif = s / len(a)
    b.append(orta_arif)

print("Array b:", b)


# 62 - masala
n = int(input('N: '))
a = []
for i in range(n):
    element = int(input(f'{i+1} -- > '))
    a.append(element)

b = []
for i in a:
    if i > 0:
        b.append(i)

c = []
for i in a:
    if i < 0:
        c.append(i)

print('B massivni element soni:', len(b))
print('B massivni element:', b)

print('C massivni element soni:', len(c))
print('C massivni element:', c)


# 63 - masala
n = int(input('N: '))

print('A massive element kiriting:')
a = []
for i in range(n):
    element = int(input(f'{i+1} --> '))
    a.append(element)

print('B massive element kiriting:')
b = []
for i in range(n):
    element = int(input(f'{i+1} --> '))
    b.append(element)

c = []

for element in a:
    c.append(element)


for element in b:
    c.append(element)


n = len(c)
for i in range(n - 1):
    for j in range(n - i - 1):
        if c[j] > c[j + 1]:
            print('c[j]', c[j])
            c[j], c[j + 1] = c[j + 1], c[j]
            print('c[j]', c[j], 'va', c[j+1])

print('c', c)


# 64 - masala
n = int(input('N: '))
a = []
for i in range(n):
    element = int(input(f'{i+1} --> '))
    a.append(element)

b = []
for i in range(n):
    element = int(input(f'{i+1} --> '))
    b.append(element)

c = []
for i in range(n):
    element = int(input(f'{i+1} --> '))
    c.append(element)

d = []
for a in a:
    d.append(a)
for b in b:
    d.append(b)
for c in c:
    d.append(c)

n = len(d)
for i in range(n - 1):
    for j in range(n - i - 1):
       if d[j] > d[j+1]:
           d[j], d[j+1] = d[j+1], d[j]

print('d=', d)


# 4. Massive elementlarni o'zgartirish


# 65 - masala
n = int(input("Massiv uzunligini kiriting: "))
k = int(input("Elementni o'rnatish uchun k ni kiriting: "))

massiv = []
for i in range(n):
    massiv.append(int(input(f"massiv[{i}]= ")))

massiv[-1] += k

print("Natija:", massiv)


# 66 - masala
n = int(input("N: "))
a = []
for i in range(n):
    a.append(int(input(f"{i+1}-chi elementni kiriting: ")))

juft = False
for i in range(n):
    if a[i] % 2 == 0:
        a[i] += 2
        print('a[i]', a[i])
        juft = True
        break

if juft:
    print("Ortirilgan birinchi son:", a)
else:
    print("Juft son topilmadi.")


# 67 - masala
n = int(input("N: "))
a = []
for i in range(n):
    a.append(int(input(f"{i+1}-chi elementni kiriting: ")))

Toq = False
last_index = -1
for i in range(n):
    if a[i] % 2 != 0:
        last_index = i
        print('last_index', last_index)
        Toq = True


if Toq:
    a[last_index] += 1
    print("Ortirilgan oxirgi son::", a)
else:
    print("Toq son topilmadi.")


# 68 - masala
n = int(input('N: '))
a = []
for i in range(n):
    element = int(input(f'{i+1} - > '))
    a.append(element)

min_index = 0
max_index = 0

for i in range(1, n):
    if a[i] < a[min_index]:
        min_index = i
    elif a[i] > a[max_index]:
        max_index = i

a[min_index], a[max_index] = a[max_index], a[min_index]

print('Orni almashtirilgan', a)


# 69 - masala
n = int(input('N: '))
a = []
for i in range(n):
    element = int(input(f"{i+1} --> "))
    a.append(element)


for i in range(0, n, 2):
    print('i', i)
    a[i], a[i+1] = a[i+1], a[i]

print('a', a)


# 70 - masala
n = int(input('N: '))
a = []
for i in range(n):
    element = int(input(f'{i+1} --> '))
    a.append(element)

half = n // 2
print('half', half)
for i in range(half):
    a[i], a[i+half] = a[i+half], a[i]
    print('a[i]', a[i], 'va', a[i+half])

print('Massivni birinchi yarmi va ikkinchi yarmi qiymati almashtirilsin', a)


# 71 - masala
n = int(input("N: "))
a = []
for i in range(n):
    a.append(int(input(f"{i+1}-chi elementni kiriting: ")))

for i in range(n // 2):
    print('i', i)
    a[i], a[n - i - 1] = a[n - i - 1], a[i]
    print('a[i]', a[i], 'va', 'a[n-i-1]', a[n-i-1])

print("Yangilangan massiv:", a)


# 72 - masala
n = int(input("N: "))
a = []
for i in range(n):
    a.append(int(input(f"{i+1}-chi elementni kiriting: ")))

k = int(input("k ni kiriting: "))
h = int(input("h ni kiriting: "))
print(a[k-1], a[h-1])
a[k-1], a[h-1] = a[h-1], a[k-1]
print('a[k-1]', a[k-1], 'va', 'a[h-1]', a[h-1])

print("Yangilangan massiv:", a)


# 73 - masala
n = int(input('N: '))
a = []
for i in range(n):
    element = int(input(f'{i+1} -- > '))
    a.append(element)

k = int(input("k ni kiriting: "))
h = int(input("h ni kiriting: "))

s = a[k]
a[k] = a[h]
a[h] = s

print('Massive a[k] va a[h] orasida qiymat:', a)


# 74 - masala
n = int(input("N: "))
a = []
for i in range(n):
    a.append(int(input(f"{i+1}-chi elementni kiriting: ")))

min = a[0]
max = a[0]
min_index = 0
max_index = 0

for i in range(1, n):
    if a[i] < min:
        min = a[i]
        min_index = i
        print('min_index', min_index)
    if a[i] > max:
        max = a[i]
        max_index = i
        print('max_index', max_index)

if min_index != max_index:
    a[min_index] = 0
    a[max_index] = 0

print("Yangilangan massiv:", a)


# 75 - masala
n = int(input('N: '))
a = []
for i in range(n):
    element = int(input(f'{i+1} --> '))
    a.append(element)

min_a = a[0]
max_a = a[0]
max_index = 0
min_index = 0

for i in range(1, n):
    if a[i] < min_a:
        min_a = a[i]
        max_index = i
        print('max', max_index)
    elif a[i] > min_a:
        min_a = a[i]
        min_index = i
        print('min', min_index)
a[min_index], a[max_index] = a[max_index], a[min_index]

print('Result', a)


# 76 - masala
n = int(input("N: "))
a = []
for i in range(n):
    a.append(int(input(f"{i+1}-chi elementni kiriting: ")))

for i in range(1, n - 1):
    print('i', i)
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        a[i] = 0

print("Local maksimum:", a)



# 77 - masala
n = int(input("N: "))
a = []
for i in range(n):
    a.append(int(input(f"{i+1}-chi elementni kiriting: "))) # 23,54,35,67,23

for i in range(1, n - 1):
    if a[i] < a[i - 1] and a[i] < a[i + 1]:
        print('aa', a[i])
        a[i] = a[i] ** 2 # 35**2 = 1225
        print('a[i]', a[i])

print("Massive eng kichkina soning darajasi:", a)


# 78 - masala
n = int(input("N: "))
a = []
for i in range(n):
    a.append(int(input(f"{i+1}-chi elementni kiriting: ")))

for i in range(n):
    if i < n - 1:
        print('i', i)
        orta_arifmetika = (a[i] + a[i + 1]) / 2
        a[i] = orta_arifmetika
        print('a', a[i])
    else:
        orta_arifmetika = (a[i] + a[0]) / 2
        a[i] = orta_arifmetika
        print('aa', a[i])

print("Orta arifmetika:", a)


# 79 - masala
n = int(input("n: "))
a = []
for i in range(n):
    a.append(int(input(f"{i+1}-chi elementni kiriting: ")))

last_element = a[-1]
for i in range(n-1, 0, -1):
    print('i', i)
    a[i] = a[i-1]
    print('a[i]', a[i])
a[0] = 0
print('a[0]', a[0])

print("Result:", a)


# 80 - masala
n = int(input('N: '))
a = []
for i in range(n):
    element = int(input(f'{i+1} --> '))
    a.append(element)


for i in range(n-2, -1, -1):
    print('i', i)
    a[i+1] = a[i]
    print('a[i+1]', a[i+1])
a[0] = 0

print('Result', a)


# 81 - masala 50/50cFALSE
n = int(input('N: '))
a = []
for i in range(n):
    element = int(input(f'{i+1} --> '))
    a.append(element)

K = int(input('K: '))
#
# for i in range(K):
#     a[i] = 0

for i in range(K, n):
    a[i] = a[i - K]
    print('a[i]', a[i])
print('Result', a)


# 82 - masala
n = int(input('N: '))
a = []
for i in range(n):
    element = int(input(f'{i+1} -> '))
    a.append(element)

k = int(input('K:'))
for i in range(n-k, n):
    print('i', i)
    a[i] = a[i - n + k]
    print('a[i]', a[i])

for i in range(k):
    a[i] = 0

print('Result', a)


# 83 - masala
n = int(input('N: '))
a = []
for i in range(n):
    element = int(input(f'{i+1} --> '))
    a.append(element)

last_value = a[n-1]

for i in range(n-1, 0, -1):
    print('i', i)
    a[i] = a[i-1]
    print('a[i]', a[i])

a[0] = last_value

print('Result', a)


# 84 - masala
n = int(input('N: '))
a = []
for i in range(n):
    element = int(input(f'{i+1} -- > '))
    a.append(element)

last_index = a[n - 1]

for i in range(n - 1, 0, -1):
    a[i] = a[i - 1]

a[0] = last_index

print('Result', a)


# 85 - masala 50/50 FAlse
n = int(input("N: "))
a = []
for i in range(n):
    a.append(int(input(f"{i+1} -->: ")))

k = int(input("k: "))

s = a[-k:] + a[:-k]

for i in range(n):
    a[i] = s[i]

print("Result:", a)


# 86 - masala 50/50 False
n = int(input("N: "))
a = []
for i in range(n):
    a.append(int(input(f"{i+1}  --> : ")))

k = int(input("k: "))

s = a[n-k:] + a[:n-k]

for i in range(n):
    a[i] = s[i]

print("Yangilangan massiv:", a)



# 87 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} -- > ')))

birinchi_element = a[0]

for i in range(n-1, 0, -1):
    a[i] = a[i-1]

a[0] = birinchi_element

print("Result:", a)


# 88 - masala
n = int(input("N: "))
a = []
for i in range(n):
    a.append(int(input(f"{i+1} --> ")))

last_element = a[n-1]

for i in range(n-1, 0, -1):
    a[i] = a[i-1]

a[0] = last_element

print("Yangilangan massiv:", a)


# 89 - masala 50/50
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f"{i+1} --> ")))

max_index = a.index(max(a))

for i in range(n-1, 0, -1):
    a = a[max_index + 1:] + a[:max_index + 1]

print("Yangilangan massiv:", a)


# 5. Massivga element qo'shish va o'chirish


# 90 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} --> ')))

k = int(input('K: '))

a.pop(k)

print('Result:', a)


# 91 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} --> ')))

k = int(input('K: '))
m = int(input('M: '))


if k > 0 or k >= n or k >= m:
    print('Error indeks')
else:
    result = []
    for i in range(k, m + 1):
        print('i', i)
        result.append(a[i])
        print('result')

    print('Elementlar soni:', len(result))
    print("Elements: ", end="")
    for element in result:
        print(element, end=' ')


# 92 - masala
n = int(input("N: "))
arr = []

for i in range(n):
    arr.append(int(input(f"{i + 1} -- >  ")))

result = []
for element in arr:
    if element % 2 != 0:
        result.append(element)

print(f"Element soni: {len(result)}")
print("Elements: ", end="")
for element in result:
    print(element, end=" ")


# 93 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} -- > ')))

result = []
i = 1
while i < n:
    result.append(a[i])
    i += 2

print('Element soni', len(result))
print('Elements:', end='')
for element in result:
    print(element, end=' ')


# 94 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} --> ')))

result = []
i = 0
while i < n:
    result.append(a[i])
    i += 2

print('Element soni:', len(result))
print('Element:', end='')
for ekement in result:
    print(ekement, end=' ')


# 95 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} -- > ')))

x = int(input('X: '))

found = False
result = []
for element in a:
    if element == x and not found:
        found = True
    else:
        result.append(element)

if found:
    print(f"Element soni: {len(result)}")
    print("Elements: ", end="")
    for element in result:
        print(element, end=" ")
else:
    print("Element arr ni ichidan topilmadi.")


# 96 - masala

n = int(input("N: "))
arr = []

for i in range(n):
    arr.append(int(input(f"{i + 1} --> ")))

result = []
s = []
for element in arr:
    if element not in s:
        print(element)
        s.append(element)
        result.append(element)

print(f"Element soni: {len(result)}")
print("Elements: ", end="")
for element in result:
    print(element, end=" ")


# 97 - masala
n = int(input("N: "))
arr = []

for i in range(n):
    arr.append(int(input(f"{i + 1} --> ")))

last_number = {}
result = []
for i in range(n):
    element = arr[i]
    print('element', element)
    last_number[element] = i
    print('last_numer[element]', last_number[element])

for i in range(n):
    element = arr[i]
    print('ele', element)
    if i == last_number[element]:
        print('i==last_numver', i == last_number)
        result.append(element)
        print('result', result)

print(f"Number of elements: {len(result)}")
print("Elements: ", end="")
for element in result:
    print(element, end=" ")


# 98 - masala
n = int(input("N: "))
arr = []

for i in range(n):
    arr.append(int(input(f"{i + 1} --> "))) # 1,2,3,4,5,3,6,7,3

element_counts = {}
for element in arr:
    if element in element_counts:
        element_counts[element] += 1
    else:
        element_counts[element] = 1

result = []
for element in arr:
    if element_counts[element] >= 3:
        result.append(element)

print(f"Elementlar soni {len(result)}")
print("Elements: ", end="")
for element in result:
    print(element, end=" ")


# 99 - masala
n = int(input("N: "))
arr = []

for i in range(n):
    arr.append(int(input(f"{i + 1} --> ")))

s = {}
for element in arr:
    if element in s:
        print('element:', element)
        s[element] += 1
        print('s', s[element])
    else:
        s[element] = 1
        print('ss', s[element])

result = []
for element in arr:
    if s[element] <= 2:
        result.append(element)

print(f"Element soni {len(result)}")
print("Elements: ", end="")
for element in result:
    print(element, end=" ")


# 100 - masala
n = int(input("N: "))
arr = []

for i in range(n):
    arr.append(int(input(f"{i + 1} --> ")))

s = {}
for element in arr:
    if element in s:
        s[element] += 1
    else:
        s[element] = 1

result = []
for element in arr:
    if s[element] == 2:
        result.append(element)

print(f"Element soni: {len(result)}")
print("Elements: ", end="")
for element in result:
    print(element, end=" ")


# 101 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} --> '))) # 1,2,3,4,5

k = int(input('K: ')) # 3
if k < 0 or k >= n:
    print('Error number')
else:
    result = []
    for i in range(n):
        if i == k: # 4,3 = 1,2,3,0,4,5
            result.append(0)
        result.append(a[i])



    print(f"Element soni: {len(result)}")
    print("Elements: ", end="")
    for element in result:
        print(element, end=" ")


# 102 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} --> '))) # 1,2,3,4,5


k = int(input('K: ')) # 3
if k < 0 or k >= n:
    print('Error number')
else:
    result = []
    for i in range(n):
        result.append(a[i])
        if i == k: # 4,3 = 1,2,3,4,0,5
            result.append(0)

    print(f"Element soni: {len(result)}")
    print("Elements: ", end="")
    for element in result:
        print(element, end=" ")


# 103 - masala
n = int(input("N: "))
a = []

for i in range(n):
    a.append(int(input(f"{i + 1} --> ")))

min_index = 0
max_index = 0

for i in range(1, n):
    if a[i] < a[min_index]:
        min_index = i
        print('min_index', min_index)
    if a[i] > a[max_index]:
        max_index = i
        print('max_index', max_index)

result = []
for i in range(n):
    result.append(a[i])
    if i == min_index:
        result.append(0)
    elif i == max_index:
        result.insert(i, 0)
        print('result', result)

print(f"Element soni: {len(result)}")
print("Elements: ", end="")
for element in result:
    print(element, end=" ")


# 104 - masala
n = int(input("N: "))
a = []

for i in range(n):
    a.append(int(input(f"{i + 1} --> ")))

k = int(input("K: "))
m = int(input("M: "))

if k < 0 or k >= n:
    print("Error number!")
elif m < 1 or m > 10:
    print("Error enter number!")
else:
    result = []
    for i in range(n):
        if i == k:
            result.extend([0] * m)
        result.append([i])

    print(f"Elementlar soni: {len(result)}")
    print("Elements: ", end="")
    for element in result:
        print(element, end=" ")


# 105 - masala
n = int(input("N: "))
a = []

for i in range(n):
    a.append(int(input(f"{i + 1} --> ")))

k = int(input("K: "))
m = int(input("M: "))

if k < 0 or k >= n:
    print("Error number!")
elif m < 1 or m > 10:
    print("Error enter number!")
else:
    result = []
    for i in range(n):
        result.append(a[i])
        if i == k:
            result.extend([0] * m)

    print(f"Elementlar soni: {len(result)}")
    print("Elements: ", end="")
    for element in result:
        print(element, end=" ")


# 106 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} --> '))) #1,2,3,4,5

result = []

for i in range(0, len(a), 2):
    if i + 1 < len(a):
        result.append(a[i] + a[i+1]) #0,2 = 1+2,3+4 =3,7
        print('result', result)

print(result)


# 107 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} --> ')))

result = []
for indeks, qiymat in enumerate(a):
    print('indeks', indeks, 'qiymat', qiymat)
    if indeks % 2 != 0:
        print('indek', indeks)
        result.append(qiymat)
        print('result1', result)
        result.append(qiymat)
        print('result2', result)
print('result', result)


# 108 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} --> ')))

result = [0]
for i in a:
    if i > 0:
        result.append(0)
    result.append(i)
print(result)


# 109 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} --> ')))

result = [0]
for i in a:
    result.append(i)
    if i < 0:
        result.append(0)
print(result)


# 110 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} --> ')))

result = []
for i in range(len(a)):
    if i % 2 == 0:
        if i + 1 < len(a):
            print('i+1=', i + 1)
            result.append(a[i] + a[i+1])
            print('result1', result)
        else:
            result.append(a[i])
            print('result2', result)

print(result)


# 111 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} --> ')))

result = []
for i in range(len(a)):
    if i % 2 != 0:
        result.extend([a[i]] * 2)
        print('result', result)
print(result)




# 6. Massivni saralash


# 112 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append((int(input(f'{i+1} --> '))))

for i in range(len(a)):
    print('i', i)
    for j in range(i+1, len(a)):
        print('j', j)
        if a[j] < a[i]:
            a[i], a[j] = a[j], a[i]
print(a)


# 113 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} --> ')))

for i in range(len(a)):
    eng_kichik_indeks = i
    print('eng_kichik', eng_kichik_indeks)
    for j in range(i+1, len(a)):
        print('j', j)
        if a[j] < a[eng_kichik_indeks]:
            eng_kichik_indeks = j
            print('kichik engg', eng_kichik_indeks)
    a[i], a[eng_kichik_indeks] = a[eng_kichik_indeks], a[i]
print(a)


# 114 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} --> ')))

for i in range(1, len(a)):
    print('i', i)
    j = i
    while j > 0 and a[j] < a[j-1]:
        print('j', j, 'va', a[j])
        a[j], a[j-1] = a[j-1], a[j]
        print('a[j]', a[j], 'va', a[j-1])
        j -= 1
        print('j', j)
print(a)


# 115 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} --> ')))

arr = list(range(len(a)))
print('arr', arr)

for i in range(len(arr)):
    print('i', i)
    for j in range(i+1, len(arr)):
        print('j', j)
        if a[arr[j]] < a[arr[i]]:
            arr[i], arr[j] = arr[j], arr[i]
print('arr', arr)
natija = [a[i] for i in arr]
print('natija', natija)
print(natija)



# 7. Butun sonlar seriyasi

# 116 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} --> '))) #2,4,4,6,6,6,1,1,8,8,8,8,5

b = []
c = []

i = 0
while i < len(a): # 13
    element = a[i]
    print('element', element)
    seriya_uzunligi = 1

    while i + 1 < len(a) and a[i] == a[i+1]:
        seriya_uzunligi += 1
        print('seriya uzunligi', seriya_uzunligi)
        i += 1

    b.append(seriya_uzunligi)
    c.append(element)

    i += 1

print('B massive: ', b)
print('C massive', c)



# 117 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} -- > ')))


result = []
for i in a:
    result.append(i)
    print('result', result)
    if i == 0:
        result.append(0)

print(result)


# 118 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} --> '))) #0,1,2,3,0,4,5,6,0,7,8,9,0,10

result = []

for i in range(n - 1):
    print('i', i)
    if a[i] == 0:
        print('a[i]', a[i])
        if i + 1 < n:
            result.append(a[i+1])

print('Result:', result)


# 119 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} --> '))) #1,2,3,4,5,6,7,8,9,10

result = []

for i in range(n - 1):
    result.append(a[i])
    if a[i] != a[i + 1]:
        print('a[i] != a[i+1]', a[i], a[i+1])
        result.append(a[i])
        print('result', result)


result.append(a[-1])
print('a[-1]', a[-1])

print("Result:", result)


# 120 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} --> '))) #1,2,2,3,4,4,4,5,5,5,6,6,6,6

result = []


count = 1
for i in range(1, n):
    if a[i] == a[i - 1]:
        count += 1
    else:
        for j in range(count - 1):
            print('j1', j)
            result.append(a[i - 1])
            print('res', result)

        count = 1
        print('count', count)

for j in range(count - 1):
    print('j2', j)
    result.append(a[n - 1])


print("Result:", result)


# 121 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} -- > ')))

k = int(input('K: '))

result = []
count = 1
for i in range(1, n):
    if a[i] == a[i - 1]:
        count += 1
        print('count', count)
    else:
        if count < k:
            print('c', count)
            for j in range(count):
                print('j', j)
                result.append(a[i-1])
                print('resultttt', result)
        else:
            for j in range(2 * count):
                print('jjjjjj', j)
                result.append(a[i - 1])
                print('ressss', result)


        count = 1

if count < k:
    for i in range(count):
        result.append(a[n - 1])
else:
    for j in range(2 * count):
        result.append(a[n - 1])

print('Result:', result)



# 122 - masala
n = int(input('N: '))
a = []
for i in range(n):
    a.append(int(input(f'{i+1} --> '))) #1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5

K = int(input("K: "))
count = 0

i = 0
while i < len(a) - K + 1:
    is_series = True
    for j in range(i, i + K - 1):
        if a[j] != a[j + 1]:
            is_series = False
            break
    if is_series:
        count += 1
        for j in range(i, i + K):
            a[j] = -1
        i += K
    else:
        i += 1

a = [x for x in a if x != -1]

print('Result:', a)
print('count ', count)



# 123 - masala 50/50
# n = int(input('N: '))
# a = []
# for i in range(n):
#     a.append(int(input(f'{i+1} --> ')))
#
# K = int(input("K: "))


# 124 - masala False
# n = int(input('N: '))
# a = []
# for i in range(n):
#     a.append(int(input(f'{i+1} --> ')))
#
# K = int(input("K: "))
# series_count = 0
# start_index = 0
# for i in range(1, len(a)):
#     if a[i] - a[i-1] != 1:
#         series_count += 1
#         if series_count == K:
#             start_index = i
#     if series_count > K:
#         break
#
# if series_count < K:
#     print("K dan kichkina bolish kerak")
# else:
#     end_index = len(a) - 1
#     for i in range(start_index, len(a)):
#         if a[i] - a[i-1] != 1:
#             end_index = i - 1
#             break
#
#     a[start_index], a[end_index] = a[end_index], a[start_index]
#     print("Modified Array:", a)

