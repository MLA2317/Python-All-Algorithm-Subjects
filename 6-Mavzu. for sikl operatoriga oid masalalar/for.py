# 6 - Mavzu for sikl operatoriga oid masalalar

# 1 - masala
# n = int(input('Butun n son kiriting: '))
# k = int(input('Butun k son kiriting: '))
# if n > 0:
#     for i in range(n):
#         print(k)

# 2 - masala
# a = int(input('a butun son kiriting: '))
# b = int(input('b butun son kiriting: '))
#
# if a < b:
#     for i in range(a, b + 1):
#         print('a and b among numbers', i)

# 3 - masala 50/50
# a = int(input('a butun son kiriting: '))
# b = int(input('b butun son kiriting: '))
#
# count = 0
#
# if a < b:
#     for i in range(a + 1, b):
#         print(i)
#         count += 1
# print("Chiqarilgan sonlar soni: ", count)

# 4 - masala
# narxi = float(input('1 kg konfetni narxini kiriting: '))
#
# for kg in range(1, 11):
#     total_price = narxi * kg
#     print(f"{kg} - kg, konfetni narxi - {total_price}")

# 5 - masala
# narxi = float(input('1 kg konfetni narxini kiriting: '))
# for kg in range(1, 11):
#     total_price = kg * narxi / 10
#     print(f"{kg / 10} - kg, konfetni narxi - {total_price}")

# 6 - masala
# narxi = float(input('1 kg konfetni narxini kiriting: '))
# for kg in range(12, 21, 1):
#     total_price = kg / 10 * narxi
#     print(f"{(kg / 10)} - kg, konfetni narxi - {total_price}")

# 7 - masala
# a = int(input('a butun son kiriting: '))
# b = int(input('b butun son kiriting: '))
# S = 0
# if a < b:
#     for i in range(a, b+1):
#         print(i)
#         S += i
# print("Yegindisi: ", S)

# 8 - masala
# a = int(input('a butun son kiriting: '))
# b = int(input('b butun son kiriting: '))
# S = 1
# if a < b:
#     for i in range(a, b+1):
#         print(i)
#         S *= i
# print("Yegindisi: ", S)

# 9 - masala
# a = int(input('a butun son kiriting: '))
# b = int(input('b butun son kiriting: '))
# S = 0
# if a < b:
#     for i in range(a, b+1):
#         S += pow(i, 2)
#         print(S)
# print("Yegindisi: ", S)


# 10 - masala
# n = int(input("Enter number n: "))
# sum = 0
#
# for i in range(1, n+1):
#     sum += 1 / i
#     print(sum)
#
# sum += i
#
# print(f"The sum S = {sum}")