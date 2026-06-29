def insertion_sort_k_bounded(arr):
    shifts = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            shifts += 1
        arr[j + 1] = key
        if j + 1 != i:
            shifts += 1
    return arr, shifts

k_arr = [2, 1, 4, 3, 6, 5, 8, 7] 
_, total_shifts = insertion_sort_k_bounded(k_arr)
print(f"Mảng độ lệch k=3 -> Tổng số shift thực tế: {total_shifts} (Rất nhỏ so với n^2)")