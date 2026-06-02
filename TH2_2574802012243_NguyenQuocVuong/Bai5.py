def dem_so_lan_xuat_hien(a, x):
    left, right = 0, len(a) - 1
    vi_tri_dau = -1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            vi_tri_dau = mid
            right = mid - 1
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    if vi_tri_dau == -1:
        return 0

    left, right = 0, len(a) - 1
    vi_tri_cuoi = -1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            vi_tri_cuoi = mid
            left = mid + 1
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return (vi_tri_cuoi - vi_tri_dau) + 1

print(dem_so_lan_xuat_hien([1, 2, 2, 2, 3], 2))