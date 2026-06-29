def mang_xap_xep_gan_k(arr):
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
    return arr, pass_count

# --- In kết quả chạy thử ---
# Mảng có độ lệch các phần tử so với vị trí đúng không quá k = 2
a = [2, 1, 4, 3, 6, 5] 
sorted_arr, total_passes = mang_xap_xep_gan_k(a)
print(f"Bài 22: Mảng sau sort: {sorted_arr} | Số lượt chạy thực tế: {total_passes} lượt.")
