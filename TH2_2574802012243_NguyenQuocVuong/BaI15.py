def k_phan_tu_gan_nhat(a, k, x):
    left, right = 0, len(a) - k
    while left < right:
        mid = (left + right) // 2
        if x - a[mid] > a[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return a[left : left + k]

print(k_phan_tu_gan_nhat([1, 2, 3, 4, 5], 4, 3))