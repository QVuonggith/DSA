"""
Bài 12: Selection sort ổn định
Sửa selection sort thành ổn định: thay vì swap, hãy dịch chuyển phần tử
nhỏ nhất về vị trí đúng và đẩy phần còn lại. Kiểm chứng tính ổn định.

Ví dụ: giữ nguyên thứ tự phần tử cùng khóa
"""


def stable_selection_sort(a, key=lambda x: x):
    a = a[:]
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if key(a[j]) < key(a[min_idx]):
                min_idx = j

        if min_idx == i:
            continue

        min_val = a[min_idx]
        # Dịch các phần tử từ vị trí i đến min_idx-1 sang phải 1 ô
        for k in range(min_idx, i, -1):
            a[k] = a[k - 1]
        a[i] = min_val
    return a


if __name__ == "__main__":
    print(stable_selection_sort([3, 1, 2]))  # [1, 2, 3]

    # Kiểm chứng tính ổn định với dữ liệu có khóa trùng (xem bài 11)
    original = [(2, 'a'), (2, 'b'), (1, 'c')]
    result = stable_selection_sort(original, key=lambda x: x[0])
    print("Ban đầu :", original)
    print("Sau sort:", result)
    # Sau sort: [(1, 'c'), (2, 'a'), (2, 'b')]
    # -> 'a' vẫn đứng trước 'b' như ban đầu => ổn định
