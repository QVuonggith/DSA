def vi_tri_cuoi_cung(a, x):
    left, right = 0, len(a) - 1
    ket_qua = -1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            ket_qua = mid
            left = mid + 1
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return ket_qua

print(vi_tri_cuoi_cung([1, 2, 2, 2, 3], 2))