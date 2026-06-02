def checkCows(vi_tri_chuong, so_bo, khoang_cach_toi_thieu):
    so_bo_da_dat = 1  
    vi_tri_cu_the = vi_tri_chuong[0]
    
    for i in range(1, len(vi_tri_chuong)):
        if vi_tri_chuong[i] - vi_tri_cu_the >= khoang_cach_toi_thieu:
            so_bo_da_dat += 1
            vi_tri_cu_the = vi_tri_chuong[i]
            if so_bo_da_dat >= so_bo:
                return True
    return False

def aggressiveCows(vi_tri_chuong, so_bo):
    vi_tri_chuong.sort()
    can_duoi = 1
    can_tren = vi_tri_chuong[-1] - vi_tri_chuong[0]
    ket_qua = 0
    
    while can_duoi <= can_tren:
        giua = (can_duoi + can_tren) // 2
        if checkCows(vi_tri_chuong, so_bo, giua):
            ket_qua = giua  
            can_duoi = giua + 1
        else:
            can_tren = giua - 1
            
    return ket_qua

print(aggressiveCows([1, 2, 4, 8, 9], 3))