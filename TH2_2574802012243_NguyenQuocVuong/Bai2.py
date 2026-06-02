def kiem_tra_ton_tai(a, x):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return True
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False

print(kiem_tra_ton_tai([2, 4, 6, 8], 5))