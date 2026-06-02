def vi_tri_chen(a, x):
    left, right = 0, len(a) - 1
    ket_qua = len(a)
    while left <= right:
        mid = (left + right) // 2
        if a[mid] >= x:
            ket_qua = mid
            right = mid - 1
        else:
            left = mid + 1
    return ket_qua

print(vi_tri_chen([1, 3, 5, 6], 4))