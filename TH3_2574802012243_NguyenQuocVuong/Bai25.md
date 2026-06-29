Bài 25. Chứng minh tính đúng đắn (loop invariant)

1. Phát biểu bất biến vòng lặp (Loop Invariant):
Tại điểm bắt đầu của mỗi vòng lặp ngoài với biến đếm i (chạy từ 0 đến n-1), đoạn mảng con gồm i phần tử tính từ cuối mảng a[n-i : n] đã được sắp xếp đúng vị trí và đây chính là i phần tử lớn nhất của toàn bộ mảng ban đầu.

2. Chứng minh qua 3 bước quy nạp:

- Bước 1: Khởi tạo (Initialization)
Trước khi vòng lặp bắt đầu (i = 0), đoạn mảng con ở cuối a[n:n] là một mảng rỗng. Mảng rỗng hiển nhiên luôn đúng vì không chứa phần tử nào sai quy tắc. Khẳng định bất biến hoàn toàn đúng.

- Bước 2: Duy trì (Maintenance)
Giả sử bất biến đúng trước lượt chạy thứ i, tức là i phần tử lớn nhất đã nằm cố định và đúng thứ tự ở cuối mảng.
Trong lượt chạy tiếp theo, vòng lặp trong liên tục so sánh và hoán đổi các cặp liền kề a[j] > a[j+1] từ chỉ số 0 đến n-i-2. Tiến trình này hoạt động theo cơ chế "sủi bọt", liên tục đẩy giá trị lớn nhất trong số các phần tử còn lại sang bên phải.
Khi vòng lặp trong kết thúc, phần tử lớn nhất của đoạn chưa sắp xếp sẽ bị đẩy tới vị trí ngay sát vách mảng đã xếp trước đó (vị trí a[n-i-1]).
Khi biến i tăng lên thành i+1, đoạn mảng ở cuối tăng lên thành i+1 phần tử sắp xếp đúng. Tính bất biến được duy trì.

- Bước 3: Điều kiện dừng (Termination)
Vòng lặp ngoài kết thúc khi i = n - 1.
Thế giá trị vào biểu thức bất biến, ta có đoạn mảng con a[1:n] gồm n-1 phần tử lớn nhất của mảng đã được sắp xếp chính xác.
Vì n-1 phần tử lớn nhất đã nằm gọn gàng đúng thứ tự ở phía sau, phần tử duy nhất còn sót lại ở vị trí đầu tiên a[0] bắt buộc phải là phần tử nhỏ nhất mảng.

Kết luận: Toàn bộ n phần tử của mảng đã được sắp xếp chính xác theo thứ tự tăng dần. Thuật toán dừng và chứng minh hoàn toàn đúng đắn.