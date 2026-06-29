def bubble_sort_toi_uu(arr):
    n = len(arr)
    pass_count = 0  #
    
    for i in range(n):
        swapped = False  
        pass_count += 1  #
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Đã có hoán đổi xảy ra
                
        # Nếu đi hết 1 lượt duyệt mà không có hoán đổi nào -> dừng ngay
        if not swapped:
            break
            
    return pass_count

# Test ví dụ
print("  mảng a =[1, 2, 3, 4] :", bubble_sort_toi_uu([1, 2, 3, 4]), "lượt.")  # Kết quả: 1 lượt