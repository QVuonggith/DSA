Đếm số phép so sánh:

(a) Với x = 7:
Số 7 nằm ngay đầu tiên nên thuật toán chỉ cần so sánh 1 lần là tìm thấy.
=> Số phép so sánh: 1

(b) Với x = 1:
Số 1 nằm ở cuối cùng của mảng nên thuật toán phải so sánh lần lượt qua cả 7 phần tử.
=> Số phép so sánh: 7

(c) Với x = 100:
Số 100 không có trong mảng nên thuật toán phải so sánh qua toàn bộ tất cả phần tử để chắc chắn không có nó.
=> Số phép so sánh: 7

Nhận xét:

Phần tử cần tìm nằm càng gần đầu mảng thì số phép so sánh càng ít (tìm kiếm càng nhanh). Ít nhất là 1 phép so sánh khi số cần tìm nằm ngay đầu mảng.

Phần tử cần tìm nằm ở cuối mảng hoặc không có trong mảng thì số phép so sánh là nhiều nhất và bằng đúng số lượng phần tử của mảng (trong bài này là 7 lần).