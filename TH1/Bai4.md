Giả sử một mảng có n phần tử. Số phép so sánh (A[i] == x) trong các trường hợp như sau:

(a) Trường hợp tốt nhất:
Xảy ra khi phần tử cần tìm nằm ngay vị trí đầu tiên của mảng. Thuật toán chỉ cần so sánh đúng 1 lần là tìm thấy.
=> Số phép so sánh: 1

(b) Trường hợp xấu nhất:
Xảy ra khi phần tử cần tìm nằm ở vị trí cuối cùng của mảng hoặc không tồn tại trong mảng. Thuật toán bắt buộc phải duyệt và so sánh qua tất cả phần tử.
=> Số phép so sánh: n

(c) Trường hợp trung bình (khi phần tử chắc chắn có trong mảng):
Vì phần tử có thể nằm ở bất kỳ vị trí nào từ 1 đến n với xác suất như nhau, số phép so sánh trung bình sẽ là trung bình cộng của các vị trí: (1 + 2 + ... + n) / n = (n + 1) / 2.
=> Số phép so sánh: (n + 1) / 2

Kết luận về độ phức tạp thời gian theo ký hiệu O lớn:

Độ phức tạp thời gian của thuật toán tìm kiếm tuyến tính được tính dựa trên trường hợp xấu nhất. Vì số phép so sánh ở trường hợp xấu nhất tỷ lệ thuận bậc nhất với n (bằng n), nên độ phức tạp thời gian theo ký hiệu O lớn là:
=> O(n)