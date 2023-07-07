# 10 - Mavzu. Bir o'lcahmli massivla bilan ishlash

# 1. Massiveni hosil qilish va elementlarini kiritish


# 1 - masala
n = 5
odd_array = []
num = 1

while len(odd_array) < n:
    odd_array.append(num)
    num += 2

print(odd_array)


# 2 - masala
n = int(input('Butun son kiriting: '))
daraja_array = []

for i in range(n):
    daraja_array.append(2 ** i)

print(daraja_array)



# 3 - masala

n = int(input('N: '))  # 5
A = int(input('A: '))  # 1
D = int(input('D: '))  # 3
progression_array = [A]

for i in range(1, n):
    next_a = progression_array[i-1] + D
    progression_array.append(next_a)

print(progression_array)


# 4 - masala

n = int(input('N: '))
A = int(input('A: '))
D = int(input('D: '))
progression_arr = [A]

for i in range(1, n):
    next_a = progression_arr[i-1] * D
    progression_arr.append(next_a)

print(progression_arr)


# 5 - masala

n = int(input('N: '))
fib = [1, 1]
for i in range(2, n):
    print('i', i)
    fib.append(fib[i-1] + fib[i-2])
    print('fib[i-1]', fib[i-1] + fib[i-2])
    print('fib', fib)

print('Fibonachi:', fib[:n])


# 6 - masala

n = int(input('N: '))
A = int(input('A: '))
B = int(input('B: '))
arr = [A, B]
for i in range(2, n):
    arr.append(sum(arr[:i]))
    print('arr[:i]', arr[:i])

print('Yegindisi:', arr)


# 7 - masala

n = int(input('N: '))
arr = []

for i in range(n):
    element = int(input(f"{i+1}- chi elementni kiriting: "))
    arr.append(element)

arr.reverse()

for i in arr:
    # print('i', i)
    print('Teskari tartib - ', arr)
#
# for i in range(n-1, -1, -1):
#     # print('i', i)
#     print('Teskari tartib - ', arr[i])


# 8 - masala False

n = int(input('N: '))
toqlar = []

for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    toqlar.append(element)

count = 0




# 9 - masala
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



# 11 - masala

n = int(input('N: '))
K = int(input('K: '))
arr = []

for i in range(n):
    element = int(input(f"{i+1}-chi element: "))
    arr.append(element)

result = arr[K-1::K]
print('result-', result)


# 12 - masala
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f"{i+1}-chi element juftlarini kiriting: "))
    arr.append(element)

result = arr[::2]
print('Result:', result)

# 13 - masala
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f"{i+1}-chi element toqlarini kiriting: "))
    arr.append(element)

result = arr[::-2]
print('Result:', result)


# 14 - masala
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    arr.append(element)

result = arr[1::2] + arr[::2]

print('result', result)


# 15 - masala
n = int(input('N:'))
arr = []
for i in range(n):
    element = int(input(f"{i+1}-chi elementni kiriting: "))
    arr.append(element)


result = arr[::2] + arr[-1::-2]
print('arr', arr[::2])
print('arr2', arr[-1::-2])

print('result', result)


# 16 - masala 50/50
n = int(input('N: '))
arr = []
for i in range(n):
    element = int(input(f'{i+1}-chi elementni kiriting: '))
    arr.append(element)


# for i in range(len(arr)):
result = arr[arr // 2] + arr[-((arr // 2) + 1)]
result = [arr[i // 2] if i % 2 == 0 else arr[-((i // 2) + 1)] for i in range(len(arr))] # True

print('Result: ', result)


# 17 - masala


# 2. Massive elementlarini taxlil qilish

# 18 - masala

