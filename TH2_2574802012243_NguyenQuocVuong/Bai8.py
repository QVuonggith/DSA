def can_bac_hai_nguyen(n):
    left, right = 0, n
    ket_qua = 0
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= n:
            ket_qua = mid
            left = mid + 1
        else:
            right = mid - 1
    return ket_qua

print(can_bac_hai_nguyen(8))