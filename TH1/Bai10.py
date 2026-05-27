def vi_tri_cuoi_cung(a, x):
    # Duyệt ngược từ cuối mảng về đầu
    for i in range(len(a) - 1, -1, -1):
        if a[i] == x:
            return i
    return -1