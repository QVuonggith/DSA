def cocktail_shaker_sort(arr):
    n = len(arr)
    start = 0
    end = n - 1
    swapped = True
    
    while swapped:
        swapped = False
        
        for j in range(start, end):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
            
        end -= 1
        swapped = False
        
        for j in range(end - 1, start - 1, -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        start += 1
        
    return arr

a = [5, 1, 4, 2, 8]
print(cocktail_shaker_sort(a)) 