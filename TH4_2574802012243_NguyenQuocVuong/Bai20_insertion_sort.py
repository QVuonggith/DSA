def shell_sort(arr, gap_sequence_type="n/2"):
    n = len(arr)
    shifts = 0
    
    if gap_sequence_type == "n/2":
        gaps = []
        g = n // 2
        while g > 0:
            gaps.append(g)
            g //= 2
    elif gap_sequence_type == "knuth":
        gaps = []
        g = 1
        while g < n:
            gaps.append(g)
            g = g * 3 + 1
        gaps = gaps[::-1] 

    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                shifts += 1
            arr[j] = temp
            if j != i:
                shifts += 1 
                
    return arr, shifts

b = [9, 1, 5, 8, 3, 7, 4, 6]
print(f"Mảng gốc: {b}")
_, shifts_n2 = shell_sort(b.copy(), "n/2")
_, shifts_knuth = shell_sort(b.copy(), "knuth")
print(f"Shell Sort (n/2) -> Tổng số shift: {shifts_n2}")
print(f"Shell Sort (Knuth) -> Tổng số shift: {shifts_knuth}")