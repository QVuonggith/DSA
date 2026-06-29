def sort_by_absolute_value(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            # So sánh trị tuyệt đối của hai phần tử liền kề
            if abs(arr[j]) > abs(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Test ví dụ
a = [-3, 1, -2, 2]
print(sort_by_absolute_value(a))  