def dem_so_luot_can_thiet(arr):
    n = len(arr)
    pass_count = 0  
    
    for i in range(n):
        swapped = False
        pass_count += 1
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        if not swapped:
            break
            
    return pass_count

print("a = [2, 1, 3, 4] :", dem_so_luot_can_thiet([2, 1, 3, 4]), "lượt.")