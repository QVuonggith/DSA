def dem_so_lan_so_sanh(arr):
    n = len(arr)
    sosanh = 0  
    
    for i in range(n):
        for j in range(0, n - i - 1):
            sosanh += 1  
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return sosanh  

a = [1, 2, 3]
print("Mảng ban đầu:", a)

so_lan_so_sanh = dem_so_lan_so_sanh(a)
print(f"Tổng số lần so sánh: {so_lan_so_sanh} lần")