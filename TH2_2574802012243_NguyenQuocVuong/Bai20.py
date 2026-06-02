def checkBooks(sach, so_hoc_sinh, so_trang_toan_da):
    hoc_sinh_hien_tai = 1
    tong_so_trang_nhom = 0
    
    for so_trang in sach:
        if tong_so_trang_nhom + so_trang > so_trang_toan_da:
            hoc_sinh_hien_tai += 1
            tong_so_trang_nhom = so_trang
            if hoc_sinh_hien_tai > so_hoc_sinh:
                return False
        else:
            tong_so_trang_nhom += so_trang
            
    return True

def bookAllocation(sach, so_hoc_sinh):
    if len(sach) < so_hoc_sinh:
        return -1
        
    can_duoi = max(sach)
    can_tren = sum(sach)
    ket_qua = can_tren
    
    while can_duoi <= can_tren:
        giua = (can_duoi + can_tren) // 2
        if checkBooks(sach, so_hoc_sinh, giua):
            ket_qua = giua
            can_tren = giua - 1
        else:
            can_duoi = giua + 1
            
    return ket_qua

print(bookAllocation([12, 34, 67, 90], 2))