def dem_so_lan_hoan_doi(arr):
    n = len(arr)
    inversions = 0
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                inversions += 1
                
    return inversions

a = [2, 3, 1]
print(dem_so_lan_hoan_doi(a) ) 
