def binary_search_position(a, key, start, end, comparisons_ref):
    low = start
    high = end
    
    while low <= high:
        comparisons_ref[0] += 1  
        mid = (low + high) // 2
        
        if key == a[mid]:
            return mid + 1
        elif key > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
            
    return low

def binary_insertion_sort(a):
    comparisons = [0] 
    shifts = 0
    
    for i in range(1, len(a)):
        key = a[i]
        
        pos = binary_search_position(a, key, 0, i - 1, comparisons)
        
        j = i - 1
        while j >= pos:
            a[j + 1] = a[j]
            shifts += 1
            j -= 1
            
        a[pos] = key
        
    print(f"Mảng sau sắp xếp: {a}")
    print(f"Số lần so sánh: {comparisons[0]}")
    print(f"Số lần dịch chuyển (shift): {shifts}")

a = [3, 2, 1]
binary_insertion_sort(a)