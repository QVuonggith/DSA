def gnome_sort(arr):
    i = 0
    comparisons = 0
    swaps = 0
    n = len(arr)
    
    while i < n:
        if i == 0:
            i += 1
        else:
            comparisons += 1
            if arr[i] >= arr[i - 1]:
                i += 1
            else:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swaps += 1
                i -= 1
                
    return arr, comparisons, swaps

a = [3, 2, 1]
sorted_a, comp, sw = gnome_sort(a.copy())
print(f"Mảng sau khi xếp: {sorted_a}")
print(f"Gnome Sort -> Số lần so sánh: {comp}, Số lần đổi chỗ: {sw}")