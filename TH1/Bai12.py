def tim_min_max(a):
    min_val = max_val = a[0]
    min_idx = max_idx = 0
    
    for i in range(1, len(a)):
        if a[i] < min_val:
            min_val = a[i]
            min_idx = i
        if a[i] > max_val:
            max_val = a[i]
            max_idx = i
            
    print(f"Min: {min_val} tại vị trí {min_idx}")
    print(f"Max: {max_val} tại vị trí {max_idx}")