def tim_phan_tu_gan_nhat(arr, x):
    vi_tri_gan_nhat = 0
    khoang_cach_nho_nhat = abs(arr[0] - x)
    for i in range(1, len(arr)):
        khoang_cach_hien_tai = abs(arr[i] - x)
        if khoang_cach_hien_tai < khoang_cach_nho_nhat:
            khoang_cach_nho_nhat = khoang_cach_hien_tai
            vi_tri_gan_nhat = i
    return arr[vi_tri_gan_nhat], vi_tri_gan_nhat

a = [10, 22, 28, 29, 40]
x = 26
gia_tri, vi_tri = tim_phan_tu_gan_nhat(a, x)
print("Gần nhất là", gia_tri, "tại vị trí", vi_tri)