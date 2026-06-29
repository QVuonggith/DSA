def min_passes_nearly_sorted(arr):
    sorted_arr = sorted(arr)
    max_left_shift = 0
    
    for current_index, value in enumerate(arr):
        correct_index = sorted_arr.index(value)
        if current_index > correct_index:
            shift = current_index - correct_index
            if shift > max_left_shift:
                max_left_shift = shift
                
    
    return max(1, max_left_shift + 1)

# Test ví dụ
print, min_passes_nearly_sorted([1, 2, 3, 5, 4])
