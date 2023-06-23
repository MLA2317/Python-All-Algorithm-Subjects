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

# 3 - masala 50/50
#For3.  a va b butun sonlar berilgan (a < b). a va b sonlar orasida barcha butun sonlar (a va b dan tashqari)
# kamiyishi tartibida chiqaruvchi va chiqarilgan sonlar sonini chiqaruvchi progma tuzilsin.
a = int(input('a butun son kiriting: '))
b = int(input('b butun son kiriting: '))

count = 0

if a < b:
    for i in range(a + 1, b):
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