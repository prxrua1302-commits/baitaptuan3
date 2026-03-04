Ex1
subjects = ["Toán", "Lý", "Hóa", "Tin"]

print("Số lượng môn học:", len(subjects))

for subject in subjects:
    print(subject)

Ex2
friends = ["An", "Bình", "Cường"]
print("Ban đầu:", friends)

friends.append("Dũng")
print("Sau khi thêm:", friends)

friends.pop(1)
print("Sau khi xóa vị trí thứ hai:", friends)

Ex3
colors = ["Red", "Blue", "Green", "Yellow", "Black"]

try:
    colors.remove("Green")
except ValueError:
    print("Không tìm thấy Green")

print("Danh sách sau khi xử lý:", colors)

Ex4
numbers = [5, 2, 9, 1, 5, 6]

numbers.sort()
print("Tăng dần:", numbers)

numbers.reverse()
print("Đảo ngược:", numbers)

print("Số lần xuất hiện của 5:", numbers.count(5))

Ex5
numbers = list(map(float, input("Nhập các số cách nhau bởi khoảng trắng: ").split()))

for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1

    while j >= 0 and numbers[j] < key:   # giảm dần
        numbers[j + 1] = numbers[j]
        j -= 1

    numbers[j + 1] = key

print("Danh sách sau khi sắp xếp:", numbers)

Ex6
numbers = list(map(int, input("Nhập các số: ").split()))
swap_count = 0

n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swap_count += 1

print("Danh sách sau khi sắp xếp:", numbers)
print("Số lần hoán đổi:", swap_count)

Ex7
numbers = list(map(int, input("Nhập các số: ").split()))
x = int(input("Nhập số cần tìm: "))

found = -1
for i in range(len(numbers)):
    if numbers[i] == x:
        found = i
        break

if found != -1:
    print("Tìm thấy tại vị trí:", found)
else:
    print("Không tìm thấy")

Ex8
numbers = list(map(int, input("Nhập các số: ").split()))

found = False
for num in numbers:
    if num > 10:
        print("Số đầu tiên > 10 là:", num)
        found = True
        break

if not found:
    print("Không có số nào > 10")

Ex9
numbers = list(map(int, input("Nhập các số: ").split()))

print("Các số lẻ:")
for num in numbers:
    if num % 2 != 0:
        print(num)

  Ex10
numbers = list(map(int, input("Nhập các số: ").split()))

total = 0
print("Các số chẵn:")

for num in numbers:
    if num % 2 == 0:
        print(num)
        total += num

print("Tổng các số chẵn:", total)

Ex11
numbers = list(map(int, input("Nhập các số: ").split()))

total = 0
print("Các số chẵn:")

for num in numbers:
    if num % 2 == 0:
        print(num)
        total += num

print("Tổng các số chẵn:", total)

Ex12
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

A = []
B = []

print("Nhập ma trận A:")
for i in range(m):
    row = list(map(int, input().split()))
    A.append(row)

print("Nhập ma trận B:")
for i in range(m):
    row = list(map(int, input().split()))
    B.append(row)

C = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Ma trận tổng:")
for row in C:
    print(row)

Ex13
s = input("Nhập chuỗi: ")

if s == s[::-1]:
    print("Là Palindrome")
else:
    print("Không phải Palindrome")

Ex14
def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

s = input("Nhập chuỗi: ")
print("Số nguyên âm:", count_vowels(s))

Ex15
s = input("Nhập chuỗi: ")
reverse = ""

for char in s:
    reverse = char + reverse

print("Đảo ngược (không slicing):", reverse)
