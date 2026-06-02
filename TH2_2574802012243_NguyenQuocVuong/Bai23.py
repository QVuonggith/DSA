def countLessEqual(ma_tran, gia_tri_muc_tieu):
    dem = 0
    n = len(ma_tran)
    hang = n - 1
    cot = 0
    
    while hang >= 0 and cot < n:
        if ma_tran[hang][cot] <= gia_tri_muc_tieu:
            dem += (hang + 1)
            cot += 1
        else:
            hang -= 1
    return dem

def kthSmallest(ma_tran, k):
    n = len(ma_tran)
    can_duoi = ma_tran[0][0]
    can_tren = ma_tran[n-1][n-1]
    ket_qua = can_duoi
    
    while can_duoi <= can_tren:
        giua = (can_duoi + can_tren) // 2
        if countLessEqual(ma_tran, giua) >= k:
            ket_qua = giua
            can_tren = giua - 1
        else:
            can_duoi = giua + 1
            
    return ket_qua

ma_tran_mau = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
print(kthSmallest(ma_tran_mau, 8))