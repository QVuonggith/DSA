def dem_so_lan_hoan_doi(arr):
    n = len(arr)
    count = 0  
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1  
                
    return count  

a = [3, 2, 1]
print("Mảng ban đầu:", a)

so_lan_swap = dem_so_lan_hoan_doi(a)
print(f"Tổng số lần hoán đổi (swap): {so_lan_swap} lần")