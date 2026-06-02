import math

# Định nghĩa hàm tìm kiếm nhị phân với đầu vào là mảng 'arr' và giá trị cần tìm 'key'
def binary_search(arr, key): 
    mid = 0                   # Khởi tạo biến lưu chỉ mục ở giữa
    left = 0                  # Chỉ mục biên trái (bắt đầu từ 0)
    right = len(arr) - 1      # Chỉ mục biên phải (phần tử cuối cùng của mảng)
    step = 0                  # Biến đếm số bước (số lần lặp)
    
    # Vòng lặp tiếp tục khi khoảng tìm kiếm còn hợp lệ (biên trái chưa vượt quá biên phải)
    while (left <= right):    
        step = step + 1       # Tăng số bước lặp lên 1
        mid = (left + right) // 2  # Tìm chỉ mục ở chính giữa khoảng hiện tại
        
        # Nếu tìm thấy key tại vị trí mid, trả về chỉ mục mid ngay lập tức
        if (key == arr[mid]): 
            return mid
            
        # Nếu key nhỏ hơn phần tử ở giữa, thu hẹp phạm vi tìm kiếm sang nửa bên trái
        if (key < arr[mid]):  
            right = mid - 1
        # Ngược lại, nếu key lớn hơn phần tử ở giữa, thu hẹp phạm vi sang nửa bên phải
        else:
            left = mid + 1
            
    return -1                 # Trả về -1 nếu đã duyệt hết mảng mà không tìm thấy key

arr = [0, 4, 5, 9, 13, 15, 18, 24, 28, 29, 35]
key = 40  # Giá trị cần tìm

result = binary_search(arr, key)
print("Vi tri tim kiem thu i la:", result)