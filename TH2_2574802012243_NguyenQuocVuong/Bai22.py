def findMedianSortedArrays(mang_a, mang_b):
    if len(mang_a) > len(mang_b):
        mang_a, mang_b = mang_b, mang_a
        
    m, n = len(mang_a), len(mang_b)
    can_duoi, can_tren = 0, m
    
    while can_duoi <= can_tren:
        cat_a = (can_duoi + can_tren) // 2
        cat_b = (m + n + 1) // 2 - cat_a
        
        trai_a = float('-inf') if cat_a == 0 else mang_a[cat_a - 1]
        phai_a = float('inf') if cat_a == m else mang_a[cat_a]
        
        trai_b = float('-inf') if cat_b == 0 else mang_b[cat_b - 1]
        phai_b = float('inf') if cat_b == n else mang_b[cat_b]
        
        if trai_a <= phai_b and trai_b <= phai_a:
            if (m + n) % 2 != 0:
                return float(max(trai_a, trai_b))
            return (max(trai_a, trai_b) + min(phai_a, phai_b)) / 2.0
        elif trai_a > phai_b:
            can_tren = cat_a - 1
        else:
            can_duoi = cat_a + 1

print(findMedianSortedArrays([1, 3], [2]))
print(findMedianSortedArrays([1, 2], [3, 4]))