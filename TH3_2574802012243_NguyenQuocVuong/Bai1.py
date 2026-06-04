def bubble_sort_one_pass(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

a = [5, 1, 4, 2, 8]
print("Mảng ban đầu:", a)

ket_qua = bubble_sort_one_pass(a)
print("Mảng sau 1 lượt:", ket_qua)