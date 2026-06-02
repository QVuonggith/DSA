def suc_chua_tau_hang(w, D):
    def kiem_tra_suc_chua(suc_chua):
        so_ngay = 1
        trong_luong_hien_tai = 0
        for kien_hang in w:
            if trong_luong_hien_tai + kien_hang > suc_chua:
                so_ngay += 1
                trong_luong_hien_tai = kien_hang
            else:
                trong_luong_hien_tai += kien_hang
        return so_ngay <= D

    left, right = max(w), sum(w)
    ket_qua = right
    while left <= right:
        mid = (left + right) // 2
        if kiem_tra_suc_chua(mid):
            ket_qua = mid
            right = mid - 1
        else:
            left = mid + 1
    return ket_qua

print(suc_chua_tau_hang([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))