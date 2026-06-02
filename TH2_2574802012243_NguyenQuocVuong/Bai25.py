def checkMagnets(vi_tri_ro, so_nam_cham, luc_tu_toi_thieu):
    dem_nam_cham = 1
    vi_tri_truoc = vi_tri_ro[0]
    
    for i in range(1, len(vi_tri_ro)):
        if vi_tri_ro[i] - vi_tri_truoc >= luc_tu_toi_thieu:
            dem_nam_cham += 1
            vi_tri_truoc = vi_tri_ro[i]
            if dem_nam_cham >= so_nam_cham:
                return True
    return False

def maxDistanceMagneticForce(vi_tri_ro, so_nam_cham):
    vi_tri_ro.sort()
    can_duoi = 1
    can_tren = vi_tri_ro[-1] - vi_tri_ro[0]
    ket_qua = 0
    
    while can_duoi <= can_tren:
        giua = (can_duoi + can_tren) // 2
        if checkMagnets(vi_tri_ro, so_nam_cham, giua):
            ket_qua = giua
            can_duoi = giua + 1
        else:
            can_tren = giua - 1
            
    return ket_qua

print(maxDistanceMagneticForce([1, 2, 3, 4, 7], 3))