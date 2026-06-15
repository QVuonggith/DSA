"""
Bài 8: Tìm chỉ số nhỏ nhất trong đoạn [i, n)
Viết hàm trả về chỉ số phần tử nhỏ nhất trong đoạn từ vị trí i tới cuối
- bước lõi của selection sort.

Ví dụ: a = [9, 3, 7, 1, 5], i = 1 -> chỉ số 3
"""


def find_min_index_in_range(a, i):
    n = len(a)
    min_idx = i
    for j in range(i + 1, n):
        if a[j] < a[min_idx]:
            min_idx = j
    return min_idx


if __name__ == "__main__":
    print(find_min_index_in_range([9, 3, 7, 1, 5], 1))  # 3
