def tim_kiem_linh_canh(arr, x):
    arr.append(x)
    i = 0
    while arr[i] != x:
        i += 1
    arr.pop()
    if i < len(arr):
        return i
    return -1

a = [10, 22, 28, 29, 40]
print("Vị trí tìm thấy:", tim_kiem_linh_canh(a, 29))