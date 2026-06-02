def tim_dinh(a):
    left, right = 0, len(a) - 1
    while left < right:
        mid = (left + right) // 2
        if a[mid] < a[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left

print(tim_dinh([1, 2, 3, 1]))