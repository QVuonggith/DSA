def tim_trong_mang_xoay(a, x):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        if a[left] <= a[mid]:
            if a[left] <= x < a[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if a[mid] < x <= a[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

print(tim_trong_mang_xoay([4, 5, 6, 7, 0, 1, 2], 0))