def koko_an_chuoi(piles, h):
    def tinh_thoi_gian(toc_do):
        tong_gio = 0
        for p in piles:
            tong_gio += (p + toc_do - 1) // toc_do
        return tong_gio

    left, right = 1, max(piles)
    ket_qua = right
    while left <= right:
        mid = (left + right) // 2
        if tinh_thoi_gian(mid) <= h:
            ket_qua = mid
            right = mid - 1
        else:
            left = mid + 1
    return ket_qua

print(koko_an_chuoi([3, 6, 7, 11], 8))