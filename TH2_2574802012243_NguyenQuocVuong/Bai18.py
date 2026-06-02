def phan_tu_thu_k_bi_thieu(a, k):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        so_bi_thieu = a[mid] - (mid + 1)
        if so_bi_thieu < k:
            left = mid + 1
        else:
            right = mid - 1
    return left + k

print(phan_tu_thu_k_bi_thieu([2, 3, 4, 7, 11], 5))