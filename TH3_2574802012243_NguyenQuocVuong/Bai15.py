def sap_xep_doi_tuong_nhieu_khoa(hocsinh):
    n = len(hocsinh)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if hocsinh[j][0] > hocsinh[j + 1][0]:
                hocsinh[j], hocsinh[j + 1] = hocsinh[j + 1], hocsinh[j]
                
    for i in range(n):
        for j in range(0, n - i - 1):
            if hocsinh[j][1] < hocsinh[j + 1][1]:
                hocsinh[j], hocsinh[j + 1] = hocsinh[j + 1], hocsinh[j]
                
    return hocsinh

a = [('An', 8), ('Ba', 9), ('Cu', 8)]
print(sap_xep_doi_tuong_nhieu_khoa(a))  