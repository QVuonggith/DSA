def phan_tu_nho_nhat_mang_xoay(a):
    left, right = 0, len(a) - 1
    while left < right:
        mid = (left + right) // 2
        if a[mid] > a[right]:
            left = mid + 1
        else:
            right = mid
    return a[left]

print(phan_tu_nho_nhat_mang_xoay([3, 4, 5, 1, 2]))