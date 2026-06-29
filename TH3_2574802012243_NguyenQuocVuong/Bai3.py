def bubble_sort_descending(arr):
    n = len(arr)
    # Vòng lặp bên ngoài
    for i in range(n):
        # Vòng lặp bên trong để thực hiện từng lượt duyệt
        for j in range(0, n - i - 1):
            # CHỈ CẦN ĐỔI DẤU > THÀNH DẤU <
            # Nếu phần tử đứng trước nhỏ hơn phần tử đứng sau -> đổi chỗ để đưa số lớn lên trước
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# --- Chạy thử nghiệm với ví dụ trong bài ---
a = [5, 1, 4, 2, 8]
print("Mảng trước khi sắp xếp:", a)

ket_qua = bubble_sort_descending(a)
print("Mảng sau khi sắp xếp giảm dần:", ket_qua)