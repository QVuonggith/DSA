def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

# Nhập dữ liệu và chạy chương trình
a = [int(i) for i in input("Nhập mảng: ").split()]
x = int(input("Nhập x: "))

print("Kết quả:", linear_search(a, x))