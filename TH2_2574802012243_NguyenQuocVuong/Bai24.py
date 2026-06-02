def checkGasStations(vi_tri_tram, so_tram_them_toi_da, khoang_cach_muc_tieu):
    so_tram_da_them = 0
    for i in range(len(vi_tri_tram) - 1):
        khoang_cach_goc = vi_tri_tram[i+1] - vi_tri_tram[i]
        if khoang_cach_goc > khoang_cach_muc_tieu:
            so_tram_da_them += int(khoang_cach_goc / khoang_cach_muc_tieu)
            
    return so_tram_da_them <= so_tram_them_toi_da

def minimizeMaxDistance(vi_tri_tram, so_tram_them):
    can_duoi = 0.0
    can_tren = vi_tri_tram[-1] - vi_tri_tram[0]
    
    for _ in range(100):
        giua = (can_duoi + can_tren) / 2.0
        if checkGasStations(vi_tri_tram, so_tram_them, giua):
            can_tren = giua
        else:
            can_duoi = giua
            
    return round(can_duoi, 6)

print(minimizeMaxDistance([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))