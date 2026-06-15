"""
Bài 11: Tính KHÔNG ổn định
Đưa ra ví dụ cho thấy selection sort không ổn định: hai phần tử cùng
khóa bị đảo thứ tự sau khi sắp xếp.

Ví dụ: [(2,'a'),(2,'b'),(1,'c')] có thể đổi thứ tự a, b
"""


def selection_sort_by_key(a):
    """Selection sort thông thường (dùng swap), sắp theo a[i][0]."""
    arr = a[:]
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j][0] < arr[min_idx][0]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    original = [(2, 'a'), (2, 'b'), (1, 'c')]
    result = selection_sort_by_key(original)
    print("Ban đầu :", original)
    print("Sau sort:", result)
    # Sau sort: [(1, 'c'), (2, 'b'), (2, 'a')]
    # -> hai phần tử cùng khóa 2 là 'a' và 'b' đã bị đảo thứ tự
    #    (ban đầu 'a' trước 'b', sau khi sort 'b' lại trước 'a')
