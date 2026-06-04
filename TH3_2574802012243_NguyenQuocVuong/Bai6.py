def get_last_element_after_one_pass(arr):
    n = len(arr)
    # Thực hiện đúng một lượt duyệt từ trái sang phải
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            # Hoán đổi nếu sai thứ tự tăng dần
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            
    # Trả về giá trị nằm ở vị trí cuối cùng a[n-1] sau 1 lượt
    return arr[n - 1]

# --- Chạy thử nghiệm với ví dụ trong bài ---
a = [4, 2, 7, 1, 3]
print("Mảng ban đầu:", a)

gia_tri_cuoi = get_last_element_after_one_pass(a)
print("Giá trị nằm ở vị trí cuối cùng sau 1 lượt:", gia_tri_cuoi)