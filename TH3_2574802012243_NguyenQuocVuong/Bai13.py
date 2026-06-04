def tinh_on_dinh(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Test ví dụ
a = [(2, 'a'), (1, 'b'), (2, 'c')]
print( tinh_on_dinh(a))  