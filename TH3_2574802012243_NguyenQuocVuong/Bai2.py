def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

a = [5, 1, 4, 2, 8]
print("Mảng trước khi sắp xếp:", a)

ket_qua = bubble_sort(a)
print("Mảng sau khi sắp xếp tăng dần:", ket_qua)