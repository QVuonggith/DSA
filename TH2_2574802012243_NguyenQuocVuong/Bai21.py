def checkSplit(mang, so_doan, tong_lon_nhat_cho_phep):
    so_doan_hien_tai = 1
    tong_doan_hien_tai = 0
    
    for phan_tu in mang:
        if tong_doan_hien_tai + phan_tu > tong_lon_nhat_cho_phep:
            so_doan_hien_tai += 1
            tong_doan_hien_tai = phan_tu
            if so_doan_hien_tai > so_doan:
                return False
        else:
            tong_doan_hien_tai += phan_tu
    return True

def splitArray(mang, so_doan):
    can_duoi = max(mang)
    can_tren = sum(mang)
    ket_qua = can_tren
    
    while can_duoi <= can_tren:
        giua = (can_duoi + can_tren) // 2
        if checkSplit(mang, so_doan, giua):
            ket_qua = giua
            can_tren = giua - 1
        else:
            can_duoi = giua + 1
            
    return ket_qua

print(splitArray([7, 2, 5, 10, 8], 2))